# House Price Prediction System

A simple Django web application where a user enters basic house details and gets an
estimated price. Every estimate is saved in a database and can be viewed on a History page.

> **Note:** This is a sample rule-based estimate calculated with a Python formula.
> It is **not** an actual market valuation and does not use Machine Learning.

## Project Overview

The user opens the website, fills in a form (location, area, BHK, bathrooms, property age
and furnishing status) and submits it. The system validates the input, calculates the
estimated price using a simple formula, saves the result in an SQLite database and shows
it on a result page. Earlier estimates can be seen on the History page.

## Technologies Used

- Python
- Django
- HTML, CSS, Bootstrap (basic)
- SQLite (default Django database)
- VS Code

## Features

- Home page with a short introduction
- Prediction form with validation (area range, BHK range, bathrooms rule)
- Result page showing the entered details and the estimated price
- History page listing previous predictions, newest first
- Admin panel to view saved records
- Responsive layout using Bootstrap

## How the Price Is Calculated

The formula is in `predictor/pricing_data.py`:

```
Price = (Area x Price per sq ft of the city)
        + (BHK x 1,00,000)
        + (Bathrooms x 50,000)

Then:  + furnishing percentage (0%, 5% or 10%)
       - age reduction (1% per year, maximum 30%)
```

The price per sq ft for each city is a rounded approximate average (as of Nov 2026) taken
from public real estate reports. All values are stored in one file, so they are easy to edit.

## Project Structure

```
House_Price_Prediction/
|-- manage.py
|-- requirements.txt
|-- db.sqlite3
|-- README.md
|-- house_price_project/
|   |-- settings.py        (project settings)
|   `-- urls.py            (main URL file)
`-- predictor/
    |-- models.py          (Prediction database table)
    |-- forms.py           (input form and validation)
    |-- views.py           (logic for the pages)
    |-- urls.py            (app URLs)
    |-- admin.py           (admin panel setup)
    |-- pricing_data.py    (sample prices and formula)
    |-- templates/predictor/
    |   |-- base.html
    |   |-- home.html
    |   |-- predict.html
    |   |-- result.html
    |   `-- history.html
    `-- static/predictor/css/
        `-- style.css
```

## Architecture

```
 User (Browser)
      |  1. opens a page / submits the form
      v
 urls.py  ---------->  decides which view to run
      |
      v
 views.py  ---------> forms.py         (validates the input)
      |    ---------> pricing_data.py  (calculates the price)
      |    ---------> models.py <----> SQLite database
      v
 HTML templates (Bootstrap + CSS)  -->  shown back to the user
```

The project follows Django's **MVT** pattern: Model (`models.py`), View (`views.py`)
and Template (HTML files).

## Workflow

1. The user opens the Home page and clicks **Start Prediction**.
2. The browser requests `/predict/` (GET) and Django shows an empty form.
3. The user fills the form and submits it (POST).
4. `forms.py` validates the data. If it is wrong, the form is shown again with errors.
5. If it is valid, `calculate_price()` computes the estimated price.
6. The view saves the details and the price in the database using the Django ORM.
7. The user is redirected to the Result page and sees the estimate.
8. The **History** page reads all saved records from the database and shows them in a table.

## How to Run

1. Open the project folder in a terminal.
2. Create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install the packages:
   ```
   pip install -r requirements.txt
   ```
4. Create the database tables:
   ```
   python manage.py migrate
   ```
5. Start the server:
   ```
   python manage.py runserver
   ```
6. Open http://127.0.0.1:8000/ in the browser.

Optional: run `python manage.py createsuperuser` and open `/admin/` to view saved records.

## Pages

| Page | Address |
|---|---|
| Home | `/` |
| Prediction | `/predict/` |
| Result | `/result/<id>/` |
| History | `/history/` |

## Limitations

- The estimate uses a simple formula and city-level average prices only.
- It does not consider the exact locality, builder, floor, market conditions or live prices.
- Prices are fixed sample values and must be updated by hand in `pricing_data.py`.

## Author

Pavithra Mallampalli