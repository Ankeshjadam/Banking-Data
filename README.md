# Uber NCR Ride Booking - Data Cleaning Project

This project focuses on cleaning and preparing the raw Uber NCR ride booking data for analysis.

## 📂 Files
- `ncr_ride_bookings.csv` - Raw Data
- `NCR_Ride_Booking_clean_Data.csv` - Cleaned Data
- `Uber.py` - Python Script for Cleaning

## 🧹 Data Cleaning Steps Performed in Python (Uber.py)

1.  **Handled Null Values:** Checked and removed/filled null values in critical columns like Drop Location, Ratings.
2.  **Removed Duplicates:** Removed duplicate booking IDs.
3.  **Fixed Data Types:** Converted Date and Time columns to proper datetime format.
4.  **Standardized Columns:** Cleaned Booking Status (Completed, Cancelled by Customer/Driver), Vehicle Type, Payment Method.
5.  **Handled Inconsistent Values:** Corrected spelling mistakes and extra spaces in Pickup/Drop Locations.
6.  **Created Clean Dataset:** Exported final clean data as `NCR_Ride_Booking_clean_Data.csv`.

## 🛠️ Tech Used
- Python - Pandas, NumPy

## ▶️ How to Run
```python
# Run the cleaning script
python Uber.py
