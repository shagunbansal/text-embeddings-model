# Text Embedding Large Language Model with FastAPI Web App

This repository contains a web app built using Python FastAPI that leverages a text embedding large language model to generate text embeddings. Users can interact with the model using a simple `curl` command, and the underlying environment is powered by the popular and secure Docker image `bitnami/python:3.11`.

## Usage

To generate text embeddings using the text embedding large language model, you can make POST requests to the following endpoint using `curl`:

```bash
curl --location 'http://0.0.0.0/api/text-embeddings' \
--header 'Content-Type: application/json' \
--data '{
  "inputList": ["Sample sentence", "put your long text here", "hello world"]
}'
```

- `inputList`: An array of strings where each element represents a text for which you want to generate text embeddings.

## Docker Image

The web app is deployed in a Docker container using the `bitnami/python:3.11` image. This image is chosen for its popularity and reputation for being secure and reliable.

### Docker Installation

If you don't have Docker installed, you can download and install it from the [official Docker website](https://www.docker.com/get-started).

### Build and Run the Docker Container

To build and run the Docker container for this web app, follow these steps:

1. Clone this repository to your local machine.

2. Open a terminal and navigate to the project directory.

3. Build the Docker image with the following command:

   ```bash
   docker build -t text-embedding-app .
   ```

4. Run the Docker container:

   ```bash
   docker run -p 80:80 text-embedding-app
   ```

The web app will be accessible at [http://0.0.0.0](http://0.0.0.0).

## Dependencies

The web app and its environment rely on various Python packages and the Docker image mentioned above. You can find the specific Python dependencies in the `requirements.txt` file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributions

Contributions are welcome! Feel free to open issues or pull requests if you have any improvements, suggestions, or bug reports.


Enjoy using the text embedding large language model via FastAPI!
