# Croma TV Scraper & Product Explorer

## Overview
This project is an end-to-end backend system that scrapes LED TV product data from the Croma website, stores it in a MySQL database, and displays it through a responsive PHP-based web interface with advanced filtering and sorting.

The focus of this project is **reliability, clean data flow, and backend problem-solving**, rather than just UI.

---

## Key Features
- Dynamic web scraping using Selenium (handles JavaScript-rendered content)
- MySQL database with duplicate prevention
- Re-scraping safe using unique constraints and upsert logic
- PHP backend APIs returning JSON
- Search, filters, sorting, and pagination
- High-tech, responsive UI using HTML, CSS, and JavaScript
- Server-side filtering for scalability

---

## Tech Stack
- **Backend:** Python (Selenium), PHP
- **Database:** MySQL
- **Frontend:** HTML, CSS, JavaScript
- **Tools:** XAMPP, Git
- **Architecture:** API-based data flow

---

## Project Architecture
UI (HTML/CSS/JS)
↓
PHP Backend API
↓
MySQL Database
↑
Python Selenium Scraper

yaml
Copy code

---

## Database Design
**Table: `tvs`**
- id (Primary Key)
- product_name
- brand
- price
- rating
- screen_size
- discount
- catalog_rank
- image_url
- product_url (UNIQUE)
- created_at
- updated_at

Unique constraint on `product_url` ensures no duplicate products during re-scraping.

---

## How Scraping Works
- Selenium loads the Croma website as a real browser
- Handles dynamic JavaScript content and scrolling
- Extracts product details such as name, price, brand, and URL
- Inserts or updates data safely using unique keys

Selenium was chosen over basic HTTP scraping due to **CDN restrictions and client-side rendering**.

---

## Backend Logic
- PHP APIs handle data fetching
- Filters (price, rating, catalog rank, brand, screen size) are applied server-side
- Pagination is implemented using SQL `LIMIT` and `OFFSET`
- JSON responses are consumed by frontend JavaScript

---

## How to Run Locally
1. Install XAMPP and start Apache & MySQL
2. Create database `croma_scraper` and import schema
3. Run the Selenium scraper (Python)
4. Place project folder inside `htdocs`
5. Open in browser:
http://localhost/WEB_SCRAPPER/public/index.php

yaml
Copy code

---

## Error Handling & Reliability
- Handles partial scraper failures safely
- Database acts as source of truth
- Re-running scraper updates existing data instead of duplicating
- Pagination prevents large memory usage

---

## Learnings
- Handling dynamic websites and CDN restrictions
- Designing scalable backend APIs
- Database indexing and performance optimization
- End-to-end debugging and environment setup
- Writing production-style backend logic as a fresher

---

## Future Improvements
- Move scraper to background scheduled jobs
- Add caching for faster API responses
- Implement role-based access
- Use official APIs if available

---

## Disclaimer
This project is created for **educational and learning purposes only**.  
In real-world applications, official APIs or permission-based data access should be preferred.

---

## Author
**Omkar Keny**  
Backend / Product-Oriented Developer
