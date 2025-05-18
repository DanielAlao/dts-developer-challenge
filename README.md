# DTS Developer Technical Test

## Backend

- **Framework**: Built using Django REST Framework
- **Database**: Data is stored in a MySQL Server database
- **Authentication**: All API endpoints require a valid token for access using jwt
- **Validation**: API Validation
- **API Endpoints**:  
  Below is a list of endpoints:

  - `POST api/token/` – Authenticate and retrieve token
  - `GET /api/tasks/` – List all tasks
  - `GET /api/tasks/<id>` – Get single task
  - `POST /api/task/` – Create new task
  - `PUT /api/tasks/<id>/` – Update task status
  - `DELETE /api/tasks/<id>/` – Delete task

- **Screenshots**:
  ![API Response](screenshots/tasks-GET.JPG)

---

## Frontend

- **Template Engine**: Built using Django Templates
- **Frontend frameworks**: Datatables, Bootstrap
- **Authentication**: Integrated with Azure SSO
- **Features**:

  - User-friendly interface with error handling & validation
  - uses backend api

- **Screenshots**:
  ![Dashboard](screenshots/dashboard.JPG)

---

## Testing

- **API Testing**: test cases implemented for all API endpoints
- **Run Tests**:
  ```cmd
  python manage.py test
  ```
