# Churn Segmentation with AWS and PySpark

## Project Overview
This project predicts customer churn and performs behavioral segmentation using AWS services and PySpark.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/esquedev/churn-segmentation-aws-pyspark.git
   cd churn-segmentation-aws-pyspark
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Deploy infrastructure:
   ```bash
   bash scripts/deploy_infrastructure.sh
   ```

4. Run the ETL job:
   ```bash
   bash scripts/run_etl_job.sh
   ```

## Dataset

This project utilizes the **Customer Churn Dataset** sourced from Kaggle, available [here](https://www.kaggle.com/datasets/muhammadshahidazeem/customer-churn-dataset). This dataset was selected due to its high usability score (10/10) and its compatible GNU GPL License, making it ideal for a showcase project.

**Dataset Description:**
The dataset comprises customer records designed for evaluating churn prediction models. While a separate training file exists, the core dataset used here is analogous, featuring comprehensive customer information. Each record includes a variety of features relevant to customer behavior and service interaction:

* **CustomerID:** Unique identifier for each customer.
* **Age:** Age of the customer.
* **Gender:** Gender of the customer.
* **Tenure:** Duration (in months/years) of the customer's relationship with the service.
* **Usage Frequency:** How often the customer uses the service.
* **Support Calls:** Number of times the customer has contacted support.
* **Payment Delay:** Any delays in customer payments.
* **Subscription Type:** The type of subscription the customer has (e.g., Basic, Standard, Premium).
* **Contract Length:** The length of the customer's service contract (e.g., Monthly, Annually).
* **Total Spend:** Total amount of money spent by the customer.
* **Last Interaction:** Date or time of the customer's last interaction with the service.
* **Churn:** The target variable, indicating whether the customer has churned (likely binary: Yes/No or 1/0).

This dataset will be instrumental in developing and evaluating the ML models for customer segmentation and churn prediction within this pipeline.