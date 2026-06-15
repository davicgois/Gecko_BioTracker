# Gecko BioTracker

A modern full-stack web application, developed as a hands-on software engineering project to explore real-world application architecture, backend development, frontend engineering, database design, authentication systems, and deployment workflows.

## Overview

This project was created with a simple goal: understand how modern web applications are built from the ground up.

Rather than relying on low-code platforms or code generation tools, the application is being developed step by step to provide a deep understanding of:

* Web architecture
* Client-server communication
* API development
* Database modeling
* Authentication and authorization
* Frontend engineering
* Software design principles
* Deployment and infrastructure

The project follows professional software engineering practices and serves as a portfolio piece demonstrating both technical implementation and architectural reasoning.

---

## Project Goals

* Build a production-grade web application
* Learn backend development using Python
* Understand frontend and backend integration
* Design scalable APIs
* Apply clean code principles
* Implement secure authentication
* Deploy a complete application to the cloud
* Develop engineering skills aligned with industry standards

---

## Tech Stack

### Backend

* Python
* Flask / FastAPI
* SQLAlchemy
* PostgreSQL

### Frontend

* HTML5
* CSS3
* JavaScript
* React

### Infrastructure

* Docker
* Git
* GitHub Actions
* Nginx
* Cloud Deployment

---

## Architecture

The application follows a layered architecture:

```text
Client (Browser)
        │
        ▼
Frontend (React)
        │
        ▼
REST API (Python)
        │
        ▼
Service Layer
        │
        ▼
Database Layer
        │
        ▼
PostgreSQL
```

Each layer has a clear responsibility:

* Frontend handles user interaction.
* API manages communication between client and server.
* Services encapsulate business rules.
* Database stores and retrieves persistent data.

---

## Features

### User Management

* User registration
* User authentication
* Login and logout
* Session management
* JWT authentication

### Data Management

* Create records
* Read records
* Update records
* Delete records

### Security

* Password hashing
* Authentication middleware
* Protected routes
* Input validation

### User Experience

* Responsive interface
* Modern UI components
* Real-time feedback
* Mobile-friendly design

---

## Learning Objectives

This repository is also a learning journal documenting concepts such as:

### Computer Science

* Data structures
* Algorithms
* Complexity analysis

### Software Engineering

* Clean Code
* SOLID principles
* Design Patterns
* Testing strategies

### Web Development

* HTTP
* REST APIs
* Authentication
* Browser rendering
* State management

### DevOps

* Containers
* Continuous Integration
* Continuous Deployment
* Monitoring

---

## Project Structure

```text
project/
│
├── backend/
│   ├── routes/
│   ├── services/
│   ├── models/
│   ├── database/
│   └── tests/
│
├── frontend/
│   ├── components/
│   ├── pages/
│   ├── hooks/
│   └── services/
│
├── docs/
│
├── docker/
│
└── README.md
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/your-username/project-name.git
```

### Navigate to the project

```bash
cd project-name
```

### Backend setup

```bash
pip install -r requirements.txt
```

### Frontend setup

```bash
npm install
```

### Run the application

```bash
npm run dev
```

or

```bash
python app.py
```

---

## Roadmap

### Phase 1

* [x] Project planning
* [x] Requirements gathering
* [x] System architecture

### Phase 2

* [ ] Backend foundation
* [ ] Database integration
* [ ] Authentication system

### Phase 3

* [ ] Frontend development
* [ ] API integration
* [ ] Responsive design

### Phase 4

* [ ] Testing
* [ ] Performance optimization
* [ ] Security review

### Phase 5

* [ ] Dockerization
* [ ] Cloud deployment
* [ ] CI/CD pipeline

---

## Engineering Principles

This project emphasizes:

* Readability over cleverness
* Simplicity over complexity
* Maintainability over shortcuts
* Scalability over temporary solutions

Every architectural decision is documented and justified whenever possible.

---

## Future Improvements

* OAuth integration
* Role-based access control
* Caching layer
* Microservices experimentation
* Observability and monitoring
* AI-powered features

---

## Author

Developed by Davi Gois as part of a long-term journey toward becoming a world-class software engineer and building production-ready systems.

---

## License

This project is licensed under the MIT License.
