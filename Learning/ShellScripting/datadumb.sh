#!/bin/bash

# Export the sales_data table to sales_data.sql file

# Replace the following variables with your actual MySQL credentials and database name
DB_USER="root"
DB_PASS="VMmFLCRS4ezKIvR5K5py6ScR"
DB_NAME="sales"

mysqldump -u $DB_USER -p$DB_PASS $DB_NAME sales_data > sales_data.sql