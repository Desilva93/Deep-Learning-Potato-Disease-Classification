import tensorflow as tf

model = tf.keras.models.load_model("model_potatoes.h5")

tf.saved_model.save(
    model,
    "models/potatoes_model/1"
)

print("Model exported successfully")