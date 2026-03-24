# DevTrack-API-project
DevTrack is a minimal backend API built using Django that allows engineering teams to track bugs and tasks efficiently—similar to a simplified issue tracking system like GitHub Issues. It also demonstrates RESTful API design, with strong OOP principles including abstraction, inheritance, and polymorphism. Data stored in JSON files instead of a DB.
##  Problem Statement

In real-world engineering teams, tracking bugs and tasks is essential. Teams need a system where:

- Bugs can be reported  
- Priorities can be assigned  
- Status can be updated  
- Work can be tracked efficiently  

DevTrack solves this by providing a simple backend API system.

###  Why OOP (Object-Oriented Programming)?

The system uses OOP to ensure clean and scalable code:

- **Abstraction** → `BaseEntity` provides a common structure  
- **Inheritance** → `Issue` → `CriticalIssue`, `LowPriorityIssue`  
- **Polymorphism** → `describe()` behaves differently based on priority  

---

###  Why JSON instead of Database?

JSON files were used because:

- No setup required  
- Simple and lightweight  
- Focus on backend logic and API design  
- Easy to debug  

---

###  Relationship Design

- One Reporter → Many Issues (1:M)  
- `reporter_id` stored inside Issue  

---

## 🏗️ Project Structure

devtrack/
│── manage.py
│
├── devtrack/
│ ├── settings.py
│ ├── urls.py
│
├── issues/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│
├── issues.json
├── reporters.json

---

## 📊 Data Model

### 👤 Reporter
- id  
- name  
- email  
- team  

### 🐞 Issue
- id  
- title  
- description  
- status (open, in_progress, resolved, closed)  
- priority (low, medium, high, critical)  
- reporter_id  
- created_at  

---

##  OOP Implementation

- **BaseEntity**
  - `validate()` → ensures correct data  
  - `to_dict()` → converts object to dictionary  

- **Issue subclasses**
  - `CriticalIssue`
  - `LowPriorityIssue`

- **Polymorphism**
- issue.describe()
