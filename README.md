# Centralized Log Monitoring & Alerting System (CLMAS)

CLMAS (Centralized Log Monitoring & Alerting System) is a full-stack application built with Java Spring Boot and React for ingesting, storing, monitoring, and generating alerts from application logs.

The system provides REST APIs for log ingestion, alert-rule management, and alert-event generation, together with a React dashboard for viewing logs and alerts.

---

## Project Overview

CLMAS follows a layered backend architecture and a component-based React frontend.

### Core Workflow

1. Application logs are submitted through the backend REST API.
2. Logs are persisted using Spring Data JPA and MySQL.
3. Configured alert rules are evaluated against incoming log messages.
4. Matching rules generate alert events.
5. The React dashboard retrieves logs and alerts through REST APIs.
6. Elasticsearch and Redis configuration are included in the repository as supporting infrastructure for future monitoring and data-processing extensions.

---

## Key Features

- REST-based log ingestion
- Persistent log storage using MySQL
- Configurable alert rules
- Automatic alert-event generation
- REST APIs for retrieving logs and alerts
- React-based monitoring dashboard
- Dedicated Logs and Alerts views
- Layered Spring Boot backend architecture
- Spring Data JPA and Hibernate integration
- Elasticsearch Docker configuration
- Redis configuration
- Separate documentation for APIs and alert rules

---

## Technology Stack

### Backend

- Java
- Spring Boot
- Spring Data JPA
- Hibernate
- REST APIs
- Maven

### Frontend

- React
- Vite
- React Router
- JavaScript
- CSS

### Database & Infrastructure

- MySQL
- Elasticsearch
- Redis
- Docker

### Development Tools

- Git
- GitHub
- Postman

---

## Architecture

```text
                         CLMAS
                           |
              +------------+------------+
              |                         |
       React Dashboard             Spring Boot API
              |                         |
              |                +--------+--------+
              |                |                 |
              |           Controllers        Services
              |                |                 |
              |                +--------+--------+
              |                         |
              |                    Repositories
              |                         |
              |                       MySQL
              |
           REST APIs
              |
        +-----+------+
        |            |
       Logs        Alerts
