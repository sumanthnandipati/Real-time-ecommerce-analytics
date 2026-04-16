# Real-Time E-commerce Analytics Dashboard

## Overview
This project implements a real-time e-commerce analytics pipeline using Apache Spark and Databricks. It processes user events such as product views, add-to-cart actions, and purchases, and generates live insights through an interactive dashboard.

## Features
- Real-time event processing (view, add_to_cart, checkout, purchase)
- Bronze-Silver-Gold data pipeline architecture
- Live revenue tracking
- User behavior distribution analysis
- Top products by revenue and quantity
- Interactive dashboard

## Tech Stack
- Apache Spark
- Databricks
- SQL
- Delta Lake

## Architecture
1. Event data is generated and ingested
2. Raw events stored in Bronze layer
3. Cleaned data stored in Silver layer
4. Aggregated metrics stored in Gold layer
5. Dashboard visualizes real-time insights

## Dashboard Metrics
- Total Revenue (Real-Time)
- Revenue Trend
- User Behavior Distribution
- Top Products by Revenue
- Top Products by Quantity

## Project Structure
real-time-ecommerce-analytics
├── data
├── notebooks
├── sql
├── dashboard
├── README.md


## Outcome
Demonstrates how real-time event data can be processed into actionable business insights using a scalable data pipeline.
