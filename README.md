Here is a comprehensive, professional `README.md` file tailored for your GitHub repository. It highlights the progression from learning Pydantic fundamentals to implementing a full FastAPI application.

---

# FastAPI & Pydantic Patient Management System

## 📋 Overview

This repository serves as both a **learning roadmap** for Pydantic v2 and a **production-ready reference** for building REST APIs with FastAPI.

The project is structured to guide you from the basics of data validation (using standalone scripts) to a fully functional **Patient Management API**. It demonstrates how to build robust data models, handle complex validation logic, dynamically calculate health metrics (BMI), and persist data using a lightweight file-based system.


## ✨ Key Features

* **Pydantic Fundamentals:** comprehensive examples of `BaseModel`, strict type hinting, and `Field` constraints.
* **Advanced Validation Logic:**
* **Field Validators:** Custom regex and logic for specific fields (e.g., validating email domains like `hdfc.com`).
* **Model Validators:** Complex cross-field validation (e.g., enforcing emergency contacts for senior citizens).


* **Computed Fields:** Automatic calculation of derived data (e.g., real-time BMI calculation based on height/weight).
* **CRUD Operations:** A complete REST API handling Creation, Updates, and Deletion of patient records.
* **Data Persistence:** A custom JSON-based storage engine to save and retrieve patient data without a heavy database setup.

## 📂 Project Structure

The repository is organized into a **Learning Path** (Scripts 1-6) and the **Main Application**.

| File | Type | Description |
| --- | --- | --- |
| **`1.Pydantic.py`** | *Tutorial* | Introduction to `BaseModel`, `Annotated` types, and basic constraints (`gt`, `lt`). |
| **`2_field_validator.py`** | *Tutorial* | Using `@field_validator` for string transformations and domain restrictions. |
| **`3_model_validator.py`** | *Tutorial* | Using `@model_validator` to check logic across multiple fields (e.g., Age vs. Emergency Contact). |
| **`4_computed_fields.py`** | *Tutorial* | Implementing `@computed_field` to generate values like BMI automatically. |
| **`5_nested_models.py`** | *Tutorial* | Structuring complex data with nested models (e.g., `Address` inside `Patient`). |
| **`6_serialization.py`** | *Tutorial* | converting Pydantic models to dictionaries/JSON using `model_dump`. |
| **`main.py`** | **App** | **The core FastAPI application** integrating all previous concepts into a REST API. |
| **`patients.json`** | *Data* | The JSON file acting as the persistence layer (Database). |
| **`insurance.csv`** | *Data* | Supplementary dataset for health analysis. |

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.10+ installed.

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/fastapi-patient-management.git
cd fastapi-patient-management

```


2. **Install dependencies:**
```bash
pip install fastapi uvicorn pydantic email-validator

```



## 🏃‍♂️ Usage

### 1. Learning Pydantic

To understand specific features, run the standalone scripts individually:

```bash
python 2_field_validator.py
# Output: Validates email domains and transforms names to uppercase.

```

### 2. Running the API

To start the Patient Management Server:

```bash
uvicorn main:app --reload

```

The server will start at `http://127.0.0.1:8000`.

### 3. API Documentation

FastAPI provides automatic interactive documentation. Once the app is running, visit:

* **Swagger UI:** [http://127.0.0.1:8000/docs](https://www.google.com/search?q=http://127.0.0.1:8000/docs) - Test endpoints directly in your browser.
* **ReDoc:** [http://127.0.0.1:8000/redoc](https://www.google.com/search?q=http://127.0.0.1:8000/redoc) - Alternative API documentation.

## 🔌 API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `POST` | **/create** | Registers a new patient. Auto-calculates BMI and health verdict. |
| `PUT` | **/edit/{patient_id}** | Updates an existing patient's details. |
| `DELETE` | **/delete/{patient_id}** | Permanently removes a patient record. |

## 🧠 Business Logic

The application implements health logic to categorize patients automatically based on the standard BMI scale:

* **Formula:** 
* **Verdicts:**
* **Underweight:** BMI < 18.5
* **Normal:** 18.5 ≤ BMI < 25
* **Overweight:** 25 ≤ BMI < 30
* **Obese:** BMI ≥ 30



## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

*Developed with ❤️ using FastAPI and Pydantic.*
