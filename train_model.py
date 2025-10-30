print("--- Script started. ---")

try:
    import tensorflow as tf
    print("--- TensorFlow imported successfully. ---")
    from tensorflow.keras.preprocessing.image import ImageDataGenerator
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
    import os
    print("--- All libraries imported. ---")

   
    IMG_WIDTH, IMG_HEIGHT = 150, 150
    TRAIN_DIR = 'dataset/train'
    VALID_DIR = 'dataset/validation'
    BATCH_SIZE = 32
    EPOCHS = 20
    print(f"--- Constants set. Training dir: {TRAIN_DIR} ---")

   
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest'
    )

    validation_datagen = ImageDataGenerator(rescale=1./255)
    print("--- Data generators created. ---")

   
    print("Loading training data...")
    train_generator = train_datagen.flow_from_directory(
        TRAIN_DIR,
        target_size=(IMG_WIDTH, IMG_HEIGHT),
        batch_size=BATCH_SIZE,
        class_mode='binary'
    )
    print("--- Training data loaded. ---")

    print("Loading validation data...")
    validation_generator = validation_datagen.flow_from_directory(
        VALID_DIR,
        target_size=(IMG_WIDTH, IMG_HEIGHT),
        batch_size=BATCH_SIZE,
        class_mode='binary'
    )
    print("--- Validation data loaded. ---")

    print(f"Class indices: {train_generator.class_indices}")

  
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
        MaxPooling2D(2, 2),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Flatten(),
        Dropout(0.5),
        Dense(512, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    print("--- Model built. ---")

   
    model.compile(loss='binary_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])
    model.summary()
    print("--- Model compiled. ---")

    if train_generator.samples == 0 or validation_generator.samples == 0:
        print("\n" + "="*50)
        print("ERROR: No images found in train or validation directories.")
        print(f"Images in {TRAIN_DIR}: {train_generator.samples} (Found {train_generator.samples} images)")
        print(f"Images in {VALID_DIR}: {validation_generator.samples} (Found {validation_generator.samples} images)")
        print("\n>>> IMPORTANT: Please copy your 'biodegradable' and 'non_biodegradable' folders")
        print(f">>> from '{TRAIN_DIR}' into '{VALID_DIR}' to fix this. <<<")
        print("="*50 + "\n")
    else:
        print("\nStarting model training...")
        history = model.fit(
            train_generator,
            steps_per_epoch=max(1, train_generator.samples // BATCH_SIZE),
            epochs=EPOCHS,
            validation_data=validation_generator,
            validation_steps=max(1, validation_generator.samples // BATCH_SIZE)
        )
        print("--- Model training finished. ---")

       
        model.save('ecovision_model.h5')
        print("\nTraining complete! Model saved as 'ecovision_model.h5'")

except Exception as e:
    print("\n" + "!"*60)
    print(f"AN ERROR OCCURRED: {e}")
    print("!"*60 + "\n")
    import traceback
    traceback.print_exc()

finally:
    print("--- Script finished. ---")