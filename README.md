# Centralized Log Monitoring & Alerting System (CLMAS)

A full-stack log monitoring and alerting application built with Java, Spring Boot, JPA/Hibernate, MySQL, and React.

CLMAS is designed to collect application logs, store them centrally, evaluate configurable alert rules, and generate alert events when matching conditions are detected.

## Project Overview

The system provides a backend for:

- Ingesting application logs through REST APIs
- Persisting logs in a relational database
- Creating and managing alert rules
- Evaluating incoming logs against configured alert conditions
- Generating alert events when matching conditions are detected
- Querying stored logs
- Providing a foundation for notification and monitoring workflows

## Architecture

```text
Client / Log Source
        |
        v
   REST API
        |
        v
 Spring Boot Backend
        |
   +----+----+
   |         |
   v         v
Log Service  Alert Rule Service
   |         |
   v         v
 MySQL     Alert Rules
   |
   v
Alert Event
   |
   v
Notification Service
