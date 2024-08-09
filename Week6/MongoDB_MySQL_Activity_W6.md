# Data Migration Activity - Soccer Data

## Goal
- Practice using MongoDB and MySQL

## Steps

- Import [soccer_results_2014.json](./soccer_results_2014.json) into a mongodb collection titled "soccer_results". You can do this using MongoDBCompass.
    - The schema is as follows
        ```
        {
            date : The date of the recorded match,
            team1 : Name of the Home team,
            team2 : Name of the Away team,
            score : Object representation of the score of the game. Includes a field "ft", which is a list of the score,
                ft: List of score: [home score, away score]
        }
        ```
    - NOTE: This is the same dataset we used last week!

- Write a Python application that connects to your MongoDB server, imports this data into a data collection, connect to your MySQL server, and create a table with the data from this collection. The table schema should be as follows:
    ```
        date varchar(255),
        Home varchar(255), # Home team
        Away varchar(255), # Away team
        Home_Score int,
        Away_Score int
    ```
- Write queries to complete the following tasks:

    1) How many total matches were there?
    2) How many ties were there?
    3) How many total goals were scored?
    4) How many games has "Arsenal FC" won?


## Review
- We will review this activity.
