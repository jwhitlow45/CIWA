## Purpose
The purpose of this database is to create a clone of the [California Irrigation Management Information System](https://cimis.water.ca.gov/) (CIMIS) database. The CIMIS database has frequent outages, some lasting as long as 3 months, so this database aims to be more robust. To do this we are using a commercially viable host, Microsoft Azure, and their various services including Azure Functions, Azure Core Tools, Azure Service Bus, Azure Data Queue, and Azure SQL Databases.

## CIWA Weather Database Structure
The database structure is comprised of a multiple functions which send requests through Azure Data Queues, allowing for thousands of instructions to be sent at once and the system to handle them over long periods of time. A large SQL database comprised of multiple SQL tables are used throughout the project to allow for efficient data retrieval and storage.

![img](https://i.imgur.com/gBRc8eJ.png)


