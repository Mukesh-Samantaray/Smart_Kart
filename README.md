# 🛒 Smart_Kart

[![GitHub issues](https://img.shields.io/github/issues/Mukesh-Samantaray/Smart_Kart)](https://github.com/Mukesh-Samantaray/Smart_Kart/issues)  
[![GitHub forks](https://img.shields.io/github/forks/Mukesh-Samantaray/Smart_Kart)](https://github.com/Mukesh-Samantaray/Smart_Kart/network)  
[![GitHub stars](https://img.shields.io/github/stars/Mukesh-Samantaray/Smart_Kart)](https://github.com/Mukesh-Samantaray/Smart_Kart/stargazers)  
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](#license)

---

## 📖 About

**Smart_Kart** is an **e-commerce web application** built with Django that provides a smooth and intelligent shopping experience.  

Customers can browse products, add them to the cart, place orders, and make secure payments.  
Admins can manage products, categories, and orders via the built-in **admin panel**.  

🚀 The project also includes a **GenAI-powered Chatbot** that assists customers with:  
- Answering product-related questions  
- Guiding users through checkout  
- Providing personalized recommendations  
- Offering support beyond normal FAQs  

---

## ✨ Features

- 🔐 **User Authentication** (Sign up, Login, Logout)  
- 📦 **Product Management** by categories  
- 🛍️ **Cart System** (add/remove/update items)  
- 🔎 **Search functionality** for products  
- 💳 **Checkout & order placement**  
- 🛠️ **Admin panel** for order & product management  
- 🤖 **AI Chatbot** for customer support & smart recommendations  
- 📱 **Responsive UI** with Bootstrap  

---

## 🛠 Tech Stack

| Component       | Technology |
|-----------------|------------|
| Backend         | Django |
| Frontend        | HTML, CSS, Bootstrap, JavaScript |
| Database        | SQLite3 (default), can switch to PostgreSQL/MySQL |
| Authentication  | Django Auth System |
| AI Chatbot      | Integrated GenAI model (LLM-powered assistant) |
| Deployment      | (Render / Heroku / Hugging Face Spaces / AWS etc.) |

---

## ⚙️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Mukesh-Samantaray/Smart_Kart.git
   cd Smart_Kart
   ```

2. **Create & activate virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create superuser (for admin panel)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**

   ```bash
   python manage.py runserver
   ```

7. **Access the app**

   - Storefront → [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  
   - Admin panel → [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)  

---

## 📸 Screenshots (Optional)

_Add screenshots of your app & chatbot interface here._

---

## 🤝 Contributing

Contributions are welcome!  

1. Fork the repository  
2. Create your feature branch: `git checkout -b feature/new-feature`  
3. Commit your changes: `git commit -m "Add some feature"`  
4. Push to the branch: `git push origin feature/new-feature`  
5. Open a Pull Request  

---

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 📧 Contact

**Mukesh Samantaray**  
GitHub: [Mukesh-Samantaray](https://github.com/Mukesh-Samantaray)  

---
