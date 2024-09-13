# Optional Review Project Guidelines

## Project:
Create a Python application that connects to a MySQL database,
loads data into Spark dataframes, and answers some analytical questions listed below. 
Your answers should be generated by transforming your Spark dataframes using
filters and joins. Feel free to use SparkSQL as you see fit. Your output
can either be printed to the terminal, or saved in a file(s).
The application should connect to the "sakila" example database that comes with
your installation of MySQL, and save each table into a dataframe in Spark.

[Installation instructions if you do not have the sakila DB](https://dev.mysql.com/doc/sakila/en/sakila-installation.html)


## Questions to answer:

    1. How many distinct actors last names are there?
    2. Which last names are not repeated?
    3. Which last names appear more than once?
    4. What is that average running time of all the films in the sakila DB?
    5. What is the average running time of films by category?

## Tech Stack:
    - Python 3.x
    - PySpark
    - VS Code
    - MySQL

## Due Date

This optional project will be due by EOD on Friday. Feel free to send me the project (GitHub link)
for me to review and provide feedback. Otherwise, there will be no mandatory evaluation/presentation.

## Stretch Goals

    - Make a CLI to prompt the user for info they might want to see
    - Allow for custom queries using SQL syntax in a CLI
    - Keep logs for your application and store them in a MongoDB