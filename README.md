# Assistant OpenAI

## What is this project?

This project is a small RESTFull API made in Python to create personal Chat to be used with Assistant!

This project have the goal to help the small bussines and personal projects to build a small Assistant to help your clients or your self about any context!

## This project can be used where?

This project can be used in a lot of scenarios, how as:

- Personal Assistant to help your premium customers effectively address questions about your product or service.
- Personal Assistant to help acquire new customers by assisting in answering all questions.

## Getting Started

### Info about branchs
We currently have 3 branchs:
- `main`
  - Support K8s and Docker
- `logs/datadog`
  - Support K8s, Docker and DataDog Agent to send metrics and logs from STDOUT
- `serverless/aws_lambda`
  - Support AWS Lambda with API Gateway

### Start

These instructions will help you get Assistant OpenAI up and running on your local machine for development and testing purposes.

### First command to be executed:

```bash
# Clone this repository with the specific branch
$ git clone -b <desired-branch> https://github.com/ramonpaolo/assistant-openai.git
```

### Running Locally with Docker
```bash
# Set the environment variables
$ nano .env

# Run the docker-compose
$ docker-compose up --build -d
```

### Running Locally without Docker
```bash
# Set the environment variables
$ nano .env

# Install the dependencies
$ pip install -r requirements.txt

# Run the uvicorn
$ uvicorn main:app --reload
```

### Running with K8s
```bash
# Set the environment variables
$ nano kubernetes/secrets.yml

# Build the container image
$ docker buildx build --platform linux/amd64 -t <your-name-user>/<name-of-image>:latest .

# Upload the image do hub.docker(Image Registry)
$ docker push <your-name-user>/<name-of-image>:latest

# Apply kubernetes configs
$ kubectl apply -f kubernetes
```

### Running with AWS Lambda
_Only available to execute in CI/CD pipelines_

## Usage

Access the folder [docs](docs/) to get example of requests.

The file [context.txt](docs/context.txt) in `docs/`, is a small example of context to be used in Assistant!

## Contributing

We welcome contributions from the community! If you'd like to contribute, please follow these steps:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Make your changes and commit them: `git commit -m 'feat: Add some feature'`
4. Push to your forked repository: `git push origin feature/your-feature`
5. Create a pull request

## License

This project is licensed under the MIT - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Enjoy using Assistant OpenAI! If you have any questions or feedback, please don't hesitate to reach out to me.
