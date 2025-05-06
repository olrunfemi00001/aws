```
# AWS Django Microservice

A production-ready Django microservice that processes background tasks asynchronously using Celery and Redis. The project is containerized with Docker, deployed to AWS using Terraform (Infrastructure as Code), and powered by a GitHub Actions CI/CD pipeline.

## Features

- Django + Django REST Framework (DRF)
- Celery for background task processing
- Redis as Celery broker
- PostgreSQL as production database
- Dockerized (Django, Redis, Celery)
- GitHub Actions CI/CD pipeline
- AWS deployment using Terraform
- API endpoints:
  - `POST /api/process/` – queue a background task
  - `GET /api/status/<task_id>/` – check task status

## Bonus Features

- Swagger/OpenAPI Documentation
- Token-based authentication
- AWS CloudWatch integration
- Optional Kubernetes-ready configuration

---

## Getting Started

### Prerequisites

- Python 3.10+
- Docker & Docker Compose
- Terraform CLI
- AWS account with IAM credentials
- GitHub repo secrets: `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`

---

### Clone the Repository

```bash
git clone https://github.com/olrunfemi00001/aws.git
cd aws
````

---

### Local Development (Docker)

```bash
docker-compose up --build
```

The API will be available at:
**[http://localhost:8000/api/process/](http://localhost:8000/api/process/)**

---

## CI/CD Pipeline

The pipeline is configured to:

* Install dependencies
* Configure AWS credentials
* Run Terraform to provision infrastructure
* Deploy updated code

Located at: `.github/workflows/deploy.yml`

Trigger: Push to `main` branch

---

## Infrastructure as Code

The `terraform/` folder contains scripts to:

* Create EC2 instances or ECS clusters
* Provision security groups and networking
* Deploy the microservice to AWS

To run manually:

```bash
cd terraform
terraform init
terraform apply
```

---

## API Example

**POST** `/api/process/`

```json
{
  "email": "user@example.com",
  "message": "Hello World"
}
```

**Response:**

```json
{
  "task_id": "af1e6d34-bf4f-11ee-89e5-0242ac130002",
  "status": "queued"
}
```

---

## Author

**Daniel Olorunfemi**
[GitHub Profile](https://github.com/olrunfemi00001)

---

## License

MIT License

```

---

Let me know if you’d like me to auto-generate a `swagger.json`, add badges, or include example screenshots or video walkthroughs.
```
