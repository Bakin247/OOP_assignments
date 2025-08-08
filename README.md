# 📘 Python OOP Assignment – Smartphone Class & Polymorphism Challenge

## 📌 Overview

This repository contains **two Python programs** demonstrating **Object-Oriented Programming (OOP)** concepts:

1. **Assignment 1:** Designing a custom class (**Smartphone**) with attributes, methods, constructors, and inheritance.
2. **Activity 2:** Implementing **Polymorphism** using vehicles with the same method but different behaviors.

These examples illustrate **Encapsulation, Inheritance, and Polymorphism** in a beginner-friendly and practical way.

---

## 🚀 Assignment 1 – Smartphone Class with Inheritance

### **Description**

The `Smartphone` class represents a basic smartphone with:

* **Attributes:** brand, model, storage capacity, battery percentage.
* **Methods:**

  * `make_call()` – Simulates calling a contact.
  * `charge()` – Increases battery percentage.

The `GamingSmartphone` class **inherits** from `Smartphone` and adds:

* **Attribute:** cooling system type.
* **Method:**

  * `play_game()` – Simulates gaming while consuming battery power.

### **Code Example**

```python
# Creating objects
phone1 = Smartphone("Samsung", "Galaxy S24", 256, 80)
phone2 = GamingSmartphone("Asus", "ROG Phone 7", 512, 90, "Advanced Liquid")

# Using methods
phone1.make_call("Alice")
phone2.play_game("Call of Duty")
phone2.charge(5)
```

### **Key OOP Concepts**

* **Constructor (`__init__`)** – Initializes each object with unique values.
* **Inheritance (`super()`)** – Allows `GamingSmartphone` to reuse `Smartphone` methods.
* **Encapsulation** – Battery charging and usage are controlled by methods.

---

## 🎭 Activity 2 – Polymorphism Challenge

### **Description**

A `Vehicle` superclass defines a generic `move()` method.
Subclasses **override** this method to represent different movement behaviors:

* `Car` → Drives on the road 🚗
* `Plane` → Flies in the sky ✈️
* `Boat` → Sails on water 🚤

### **Code Example**

```python
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()
```

### **Key OOP Concepts**

* **Polymorphism** – The same method name (`move()`) behaves differently depending on the object.
* **Method Overriding** – Each subclass redefines `move()` to fit its purpose.
* **Dynamic Method Calls** – Objects are handled uniformly in a loop, but output depends on the actual class type.

---

## 🛠 How to Run the Programs

1. **Clone this repository**:

   ```bash
   git clone https://github.com/your-username/oop-assignment.git
   ```
2. **Navigate to the folder**:

   ```bash
   cd oop-assignment
   ```
3. **Run the Python files**:

   ```bash
   python smartphone.py
   python polymorphism.py
   ```

---

## 📚 Learning Outcomes

After completing these programs, you will understand:

* How to create classes with attributes and methods.
* How to use **constructors** to initialize objects.
* How to apply **inheritance** to extend functionality.
* How **polymorphism** enables the same method name to have different behaviors.

---

## 💡 Possible Extensions

* Add **more subclasses** to the Smartphone example (e.g., CameraPhone, FoldablePhone) with their own unique methods.
* Enhance the Vehicle example with **speed attributes** and **fuel consumption**.
* Implement **abstract base classes** to enforce method implementation in subclasses.

---

## 📜 License

This project is open-source and available under the MIT License.
