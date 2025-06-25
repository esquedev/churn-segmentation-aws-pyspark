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