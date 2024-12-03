FROM tensorflow/serving:2.8.0

# Salin model ke container
COPY ./outputs/serving_model /models/heart-failure-model

# Set environment variable untuk TensorFlow Serving
ENV MODEL_NAME=heart-failure-model

# Expose port untuk gRPC dan REST API
EXPOSE 8500
EXPOSE 8501

# Jalankan TensorFlow Serving
ENTRYPOINT ["/usr/bin/tensorflow_model_server", "--port=8500", "--rest_api_port=8501", "--model_name=${MODEL_NAME}", "--model_base_path=/models/${MODEL_NAME}"]
