# Big Data Cumulative Review

## Python

1) What is the difference between an interpreter and a compiler? Which does Python use?
	- https://docs.python.org/3/tutorial/interpreter.html

2) What is a REPL?

3) What is a compound statement?

4) What data types do we have by default in Python?

5) What is a namespace?

6) What is the scope of a variable?

7) What are the different operators we have in Python?

8) What are functions?

9) What is a lambda function? What is the syntax for creating a lambda?

10) What is a list?
	- https://docs.python.org/3/tutorial/datastructures.html

11) What is a set?

12) What is a tuple?

13) What is a Dictionary?

14) How can we open a file? What are the different modes for opening a file?
	- https://docs.python.org/3/tutorial/inputoutput.html

15) What is a module? How do we import a module?
	- https://docs.python.org/3/tutorial/modules.html

16) What is a datetime object?

17) What are Regular Expressions? How do we use them?

18) What are some data collections we have at our disposal in the Collections module?

19) What is a class? What is an object?
	- https://docs.python.org/3/tutorial/classes.html

20) What are the pillars of Object Oriented Programming? (OOP) Explain them.
	- https://medium.com/swlh/the-4-pillars-of-oop-in-python-9daaca4c0d13

21) Know the different flow control statements (if/elif/else, for loops, while loops, etc.)
	- https://docs.python.org/3/tutorial/controlflow.html

22) What are exceptions? How can we handle them?
	- https://docs.python.org/3/tutorial/errors.html


## SQL 

1)  What is SQL?

    1.  Structured Query Language

2)  What is a relational database management system?

    1.  RDBMS. It is a database management system in which the database
        is organized and accessed according to the relationships between
        data items. Expressed with tables

3)  What is a database?

    1.  An organized collection of structured information or data,
        stored and accessed from a computer system

4)  What are the sublanguages of SQL?

    1.  Data Definition Language (DDL)

    2.  Data Manipulation Language (DML)

    3.  Transaction Control Language (TCL)

    4.  Data Control Language (DCL)

    5.  Data Query Language (DQL)

5)  What is cardinality? How does it compare to multiplicity?

    1.  \> <https://en.wikipedia.org/wiki/Cardinality_(data_modeling)>

    2.  Numerical relationship between rows of one table and rows in the
        other

    3.  One-to-one, one-to-many, many-to-many

6)  What is a candidate key?

    1.  Unique key to identify a record uniquely in a table

7)  What is referential integrity?

    1.  The logical dependency of a foreign key on a primary key

8)  What are primary keys? Foreign keys?

    1.  Primary keys are candidate keys that are used to relate one
        column in a table to the rest. Foreign keys are used to relate
        rows of one table to rows of another table

9)  What are some of the different constraints on columns?

    1.  NOT NULL, UNIQUE, PRIMARY KEY, FOREIGN KEY, DEFAULT, CREATE
        INDEX

10) What is an entity relation diagram?

    1.  ERD. Shows the relationships of entity sets stored in a database

11) What are the differences between WHERE vs HAVING?

    1.  HAVING can work on aggregated data. Good practice to use WHERE
        before GROUP BY and HAVING after GROUP BY

12) What are the differences between GROUP BY and ORDER BY?

    1.  GROUP BY groups rows that have the same value while ORDER BY
        sorts

13) What does LIKE do?

    1.  LIKE is used to search for a specific pattern in a column

14) How do I use sub queries?

    1.  Use it as a nested query in a WHERE clause, SELECT clause, or
        FROM clause. Use parentheses

15) How does BETWEEN work?

    1.  Selects the values in a given range, inclusive on both ends

16) What is the order of operations in an SQL statement?

    1.  The order is SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY

17) What is the difference between an aggregate function and a scalar
    function?

    1.  Aggregate functions return a single summarizing value while
        scalar functions return a value based on scalar inputs

18) What are examples of aggregate and scalar functions?

    1.  Aggregate: AVG, SUM, COUNT, MAX, MIN…

    2.  Scalar: ROUND, FORMAT, UCASE, LCASE

19) What are the different joins in SQL?

    1.  \> We have CROSS, INNER, OUTER LEFT, OUTER RIGHT, and OUTER FULL
        joins. INNER joins only include records with a match in the
        output (so records where the join condition is true). OUTER
        joins includes records with a match \*and\* all unmatched
        records from the left, right, or both tables.

    2.  \> The part of the JOIN \`\`\`ON album.artist_id =
        artist.artist_id\`\`\` is the join condition. When the join
        condition is true for a pair of records, those records are
        matched together in the output. 90+% of the time, the join
        condition will be equality based on a foreign key relationship,
        but you can have various strange join conditions. A join
        condition of just TRUE will include all pairs of records in the
        output and is called a CROSS JOIN.

20) What are the different set operations in SQL? Which set operations
    support duplicates?

    1.  \> UNION, INTERSECT, UNION ALL are good to know. UNION combines
        two resultsets removing duplicates, INTERSECT produces results
        that appear in both of two result sets, and UNION ALL combines
        two resultsets including duplicates.

21) What is the difference between joins and set operations?

    1.  Joins are used to combine columns from different tables while
        set operations are used to combine rows

22) How can I create an alias in SQL?

    1.  Keyword AS

23) What does the AS keyword do in a query?

    1.  Creates an alias

24) What is multiplicity? Examples of 1-to-1, 1-to-N, N-to-N?

    1.  specifies the cardinality or number of instances of an
        EntityType that can be associated with the instances of another
        EntityType

25) What is an Index?

    1.  A quick lookup table that is used for finding records quickly in
        a database

26) What advantages does creating an Index give us? Disadvantages?

    1.  Allows for quicker searching

    2.  Decreases performance on inserts updates and deletes

27) What is CRUD?

    1.  Create, Read, Update, Delete. The most basic operations that can
        be performed in SQL

28) What is normalization?

    1. Database normalization is the process of restructuring a relational database in accordance with a series of so-called normal forms in order to reduce data redundancy and improve data integrity
    

29) What are the normal forms up to 3NF?
    1. 1NF
        - Each table cell should contain a single value
        - Each record should be unique
    
    2. 2NF
        - Be in 1NF
        - Has no partial dependency. That is, all non-key attributes are fully dependent on a primary key.

    3. 3NF
    	- Be in 2NF
	    - Have no transitive partial dependencies

## MongoDB

1.  What does BASE stand for?

    a.  Basic Availability, Soft-state, Eventual consistency

2.  What is a database in Mongo?

    a.  A database in Mongo is a grouping of unstructured data in JSON
        format

3.  What is a collection?

    a.  Equates to a table

4.  What is a document?

    a.  Equates to a row

5.  What rules does Mongo enforce about the structure of documents
    inside a collection?

6.  What is a distributed application? A distributed data store?

7.  What is High Availability? How is it achieved in Mongo?

    a.  High availability is the ability of a system to operate
        continuously without failing for a designated period of time.
        Mongo achieves it through replica sets

8.  What is Scalability? How is it achieved in Mongo?

    a.  Scalability is the ability of a database to grow in size. It is
        achieved both vertically and horizontally in MongoDB.
        Horizontally through sharding and replica sets

9.  Explain replica sets and sharding

10. What are NoSQL databases? What are the different types of NoSQL
    databases?

    a.  NoSQL is a type of nonrelational database query language.

    b.  Wide column, document, key-value, graph

11. What kind of NoSQL database MongoDB is?

    a.  It is a document database

12. Which are the most important features of MongoDB?

    a.  Can handle unstructured data

13. What is a Namespace in MongoDB?

    a.  The name of the collection, including the database.

14. Which all languages can be used with MongoDB?

15. Compare SQL databases and MongoDB at a high level.

    a.  SQL databases are structured while MongoDB is used to save
        unstructured data

16. How is MongoDB better than other SQL databases?

    a.  It is much faster than other SQL databases

    b.  Much more scalable

    c.  More flexible

17. Does MongoDB support foreign key constraints?

    a.  No

18. Does MongoDB support ACID transaction management and locking
    functionalities?

    a.  YES, but not innately

19. How can you achieve primary key - foreign key relationships in
    MongoDB?

    a.  By embedding a document inside another

20. When should we embed one document within another in MongoDB?

    a.  When we want to relate the two documents

21. Mention what is Objecld composed of?

    i.  4-byte timestamp value representing object's creation

    ii. 5-byte random value

    iii. 3-byte incrementing counter


## Hive 

1. What is Hive?
- Hive gives an SQL-like interface to query data that interfaces with Hadoop

2. Where is the default location of Hive's data in HDFS?
- /user/hive/warehouse

3. What is an External table?
- A table whose data is stored outside of Hive’s structure. The data is not lost when drop is used on an external table

4. What is a managed table?
- A table whose data is stored in hive. If dropped, the data is removed.

5. What is a Hive partition?
- A way of dividing a table into related parts based on the values of particular columns

6. Provide an example of a good column or set of columns to partition on.
- A good column to partition on is one where there might be many duplicate elements so as not to create too many directories  for small partitions

7. What's the benefit of partitioning?
- Queries on smaller pieces of data become much faster if you only have to search through one or few partitions

8. What does a partitioned table look like in HDFS?
- Each partition is stored in its own directory in HDFS with each row as a file within

9. What is a Hive bucket?
- Bucketing in Hive groups the data by ranges of values of a column or combination of columns.

10. What does it mean to have data skew and why does this matter when bucketing?
- Skew data is data that is very far off from the rest of the data in a table. For example, a field having a very large number when all the other values in the column are quite small. If skew data is not handled, the ranges for the buckets might not be optimized. 

11. What does a bucketed table look like in HDFS?
- The buckets are stored as separate files with the rows that fall into each bucket contained within.

12. Hive syntax: Create a table?
- Example:
    - ```CREATE TABLE <table_name> (column_names DATATYPE,…) row format deliminated fields terminated by ‘<deliminator>’ stored as textfile;```

13. Hive syntax: Load data into a table?
- Example:
    - ```LOAD DATA INPATH ‘<path>’ INTO TABLE <table_name>;```


## PowerBI

1. How would you define Power BI as an effective solution?** 

    Power BI is a strong business analytical tool that creates useful
    insights and reports by collating data from unrelated sources. This data
    can be extracted from any source like Microsoft Excel or hybrid data
    warehouses. Power BI drives an extreme level of utility and purpose
    using interactive graphical interface and visualizations. we can create
    reports using the Excel BI toolkit and share them on-cloud with the
    co-workers. 

      

2. What are the major components of Power BI?** 

    Power BI has these major components: 

    - Power Query : It is used for data mash-up and transformation and we can
    use this to extract data from various databases like SQL Server, MySql,
    and many others  and to delete a chunk of data from various sources. 

    - Power Pivot : It is a tabular data modeling engine that uses a
    functional language called Data Analysis Expression (DAX) to perform the
    calculations. Also, creates a relationship between various tables to be
    viewed as pivot tables. 

    - Power View : It is used for viewing data visualizations that provides an
    interactive display of various data sources to extract metadata for
    proper data analysis. 

    - Power BI Desktop : Power Desktop is an aggregated companion development
    tool of Power Query, Power View, and Power Pivot. Create advanced
    queries, models, and reports using the desktop tool. 

      

3. What are the various refresh options available?** 

    Four main refresh options are available in Power BI: 

    - Package/OneDrive refresh: This synchronizes Power BI desktop or Excel
    file between the Power BI service and OneDrive 

    - Data/Model refresh: This means scheduling the data import from all the
    sources based on either refresh schedule or on-demand.  

    - Tile refresh: Refresh the tiles cache on the dashboard every time the
    data changes. 

    - Visual container refresh: Update the reports visuals and visual
    container once the data changes. 

      

4. What are the different connectivity modes in Power BI?** 

    The three major connectivity modes in Power BI are: 

    - Direct Query: The method allows direct connection to the Power BI model.
    The data doesn't get stored in Power BI. Interestingly, Power BI will
    only store the metadata of the data tables involved and not the actual
    data. The supported sources of data query are: 

      

        - Amazon Redshift 

        - Azure HDInsight Spark (Beta) 

        - Azure SQL Database 

        - Azure SQL Data Warehouse 

        - IBM Netezza (Beta) 

        - Impala (version 2.x) 

        - Oracle Database (version 12 and above) 

        - SAP Business Warehouse (Beta) 

        - SAP HANA 

        - Snowflake 

        - Spark (Beta) (version 0.9 and above) 

        - SQL Server 

        - Teradata Database 

    - Live Connection: Live connection is analogous to the direct query method
    as it doesn't store any data in Power BI either. But opposed to the
    direct query method, it is a direct connection to the analysis services
    model. Also, the supported data sources with live connection method are
    limited: 

      

        - SQL Server Analysis Services (SSAS) Tabular 

        - SQL Server Analysis Services (SSAS) Multi-Dimensional 

        - Power BI Service 

    - Import Data (Scheduled Refresh): we upload the data into Power BI.
    Uploading data on Power BI means consuming the memory space of your
    Power BI desktop. If it is on the website, it consumes the space of the
    Power BI cloud machine. Even though it is the fastest method, the
    maximum size of the file to be uploaded cannot exceed 1 GB until and
    unless you have Power BI premium. 

      

      

5. What are the different kinds of views?

    The different  kinds of views are: 

    - Data View: Curating, exploring, and viewing data tables in the data set.
    Unlike, Power Query editor, with data view, you are looking at the data
    after it has been fed to the model. 

    - Model View: This view shows you all the tables along with their complex
    relationships. With this, you can break these complex models into
    simplified diagrams or set properties for them at once. 

    - Report View: The report view displays the tables in an interactive
    format to simplify data analysis. You can create n number of reports,
    provide visualizations, merge them, or apply any such functionality. 

      

6. What are the data sources Power BI can connect?

    The data source is the point from which the data has been retrieved. It
    can be files in various formats like .xlsx, .csv, .pbix, .xml, .txt etc,
    and databases like SQL database, SQL Data Warehouse, Spark on Azure
    HDInsight, or form content packets like Google Analytics etc., 

      

7. What are the building blocks of Power BI?

    The major building blocks of Power BI are: 

    - Datasets: Dataset is a collection of data gathered from various sources
    like SQL Server, Azure, Text, Oracle, XML, JSON, and many more. With the
    GetData feature in Power BI, we can easily fetch data from any data
    source. 

    - Visualizations: Visualization is the visual aesthetic representation of
    data in the form of maps, charts, or tables. 

    - Reports: Reports are a structured representation of datasets that
    consists of multiple pages. Reports help to extract important
    information and insights from datasets to take major business
    decisions. 

    - Dashboards: A dashboard is a single-page representation of reports made
    of various datasets. Each element is termed a tile.  

    - Tiles: Tiles are single-block containing visualizations of a report.
    Tiles help to differentiate each report. 

      

8. What is DAX?

    Data Analysis Expression (DAX) is a library of formulas used for
    calculations and data analysis. This library comprises functions,
    constants, and operators to perform calculations and give results. DAX
    lets you use the data sets to their full potential and provide
    insightful reports.DAX is based on different nested filters which
    magnificently improves the performance of data merging, modeling, and
    filtering tables. 

    DAX is a functional language containing conditional statements, nested
    functions, value references, and much more. The formulas are either
    numeric (integers, decimals, etc.) or non-numeric (string, binary). A
    DAX formula always starts with an equal sign and Name of the
    project,Start of the DAX formula,DAX function (to add),Parentheses
    defining arguments,Name of the table,Name of the field,Operator 

      

9. What is Power Pivot?

    Power Pivot enables you to import millions of rows from heterogeneous
    sources of data into a single excel sheet. It lets us create
    relationships between the various tables, create columns, calculate
    using formulas, and create PivotCharts and PivotTables.At a time there
    can be only one active relationship between the tables which is
    represented by a continuous line. 


10. What is Power Query?

    Power query is a function that filters transforms, and combines the data
    extracted from various sources. It helps to import data from databases,
    files, etc and append data 

11. Difference between Power BI and Tableau?

    The major differences between Power BI and Tableau are: 

    - While Power BI uses DAX for calculating columns of a table, Tableau uses
    MDX (Multidimensional Expressions). 

    - Tableau is more efficient as it can handle a large chunk of data while
    Power BI can handle only a limited amount.  

    - Tableau is more challenging to use than Power BI. 


12. What is GetData in Power BI?

    GetData offers data connectivity to various data sources. Connect data
    files on your local system. The supported data sources are: 

    - File: Excel, Text/CSV, XML, PDF, JSON, Folder, SharePoint. 

    - Database: SQL Server database, Access database, Oracle database, SAP
    HANA database, IBM, MySQL, Teradata, Impala, Amazon Redshift, Google
    BigQuery, etc. 

    - Power BI: Power BI datasets, Power BI dataflows. 

    - Azure: Azure SQL, Azure SQL Data Warehouse, Azure Analysis Services,
    Azure Data Lake, Azure Cosmos DB, etc. 

    - Online Services: Salesforce, Azure DevOps, Google Analytics, Adobe
    Analytics, Dynamics 365, Facebook, GitHub, etc. 

    - Others: Python script, R script, Web, Spark, Hadoop File (HDFS), ODBC,
    OLE DB, Active Directory, etc. 

13. What are filters in Power BI?

    Filters sort data based on the condition applied to it. Filters enable
    us to select particular fields and extract information in a
    page/visualization/report level. For example, filters can provide sales
    reports from the year 2022 for the US region.  Power BI can make changes
    based on the filters and create graphs or visuals accordingly.  

    The types of filters are: 

    - Page-level filters: These are applied on a particular page from various
    pages available within a report. 

    - Visualization-level filters: These are applied to both data and
    calculation conditions for particular visualizations. 

    - Report-level filters: These are applied to the entire report 

14. What are the types of visualizations in Power BI?

    Visualization is a graphical representation of data. We can use
    visualizations to create reports and dashboards. The kinds of
    visualizations available in Power BI are Bar charts, Column charts, Line
    chart, Area chart, Stacked area chart, Ribbon chart, Waterfall chart,
    Scatter chart, Pie chart, Donut chart, Treemap chart, Map, Funnel chart,
    Gauge chart, Cards, KPI, Slicer, Table, Matrix, R script visual, Python
    visual, etc. 


15. What do we understand by Power BI services?

    Power BI provides services for its cloud-based business analytics. With
    these services, you can view and share reports via the Power BI website.
    Power BI is a web-based service for sharing reports. Power BI service
    can be best referred to as PowerBI.com, PowerBI workspace, PowerBI site,
    or PowerBI portal. 

16. What is the comprehensive working system of Power BI?

    Power BI's working system mainly comprises three steps: 

    - Data Integration: The first step is to extract and integrate the data
    from heterogeneous data sources. After integration, the data is
    converted into a standard format and stored in a common area called the
    staging area. 

    - Data Processing: Once the data is assembled and integrated, it requires
    some cleaning up. Raw data is not so useful therefore, a few
    transformation and cleaning operations are performed on the data to
    remove redundant values, etc. After the data is transformed, it is
    stored in data warehouses. 

    - Data Presentation: Now that the data is transformed and cleaned, it is
    visually presented on the Power BI desktop as reports, dashboards, or
    scorecards. These reports can be shared via mobile apps or web to
    various business users. 


17. What are custom visuals in Power BI?

    Using Power BI visualizations, you can apply customized visualizations
    like charts, KPIs, etc. from the rich library of PowerBI's custom
    visuals. It refrains the developers from creating it from scratch using
    JQuery or Javascript SDK. Once the custom visual is ready, it is tested
    thoroughly. Post testing, they are packaged in .pbiviz file format and
    shared within the organization. 

    Types of visuals available in Power BI are: 

    - Custom visual files. 

    - Organizational files. 

    - Marketplace files. 


18. What are the various type of users who can use Power BI?

    Anyone and everyone can use PowerBI to their advantage. But even then a
    specific set of users are more likely to use it: 

    - Business Users: Business users are the ones who constantly keep an eye
    on the reports to make important business decisions based on the
    insights. 

    - Business Analysts: Analysts are the ones who create dashboards, reports,
    and visual representations of data to study the dataset properly.
    Studying data needs an analytical eye to capture important trends within
    the reports. 

    - Developers: Developers are involved while creating custom visuals to
    create Power BI, integrating Power BI with other applications, etc.  

    - Professionals: They use Power BI to check the data scalability,
    security, and availability of data. 

      

19. What are the advantages of Power BI?

    The advantages of Power BI that make it an excellent business
    intelligence software: 

    - It's easy to use, even for non-technical people. 

    - It has a powerful toolkit for conducting ETL (extraction,
    transformation, and loading the data). 

    - It helps share the insights from the data with data consumers. 

    - It accommodates fast updates of the data in use from the data
    sources. 

    - It is equipped with template dashboards and SaaS solution reports. 

    - It allows real-time dashboard and report updates. 

    - It allows results displays on various devices (computers, tablets,
    and mobile phones). 

    - It ensures quick and safe connection to the data sources in the cloud
    or locally. 

    - It enables data querying using natural language processing. 

    - It provides hybrid configuration and smart deployment. 


20. What are some disadvantages of Power BI?

    The disadvantages of Power BI are: 

    - The software is not very intuitive for the beginners. 

    - Dashboard and report sharing is limited: only users with the same email
    domain can access the results. 

    - The majority of data sources don\'t support real-time connections to
    Power BI interactive dashboards and reports. 

    - Power BI for free users can\'t process datasets larger than 1 GB. 

    - We can\'t store an adjusted filter in the saved Power BI visual report
    filter. In addition, the filter is always displayed on the report, which
    isn't always convenient 

    However, Power Bi is in the process of constant development and
    improvement, so we can expect the software to overcome some or all of
    its limitations. 

      

21. What is a common workflow in Power BI?

    A standard Power BI workflow includes the following four steps: 

    - Fetch the data to the Power BI Desktop, clean and manipulate the
    data, and create a report. 

    - Publish the report to the Power BI Service and build dashboards. 

    - Share the dashboards with your colleagues, managers, or
    shareholders. 

    - Interact with the final dashboards and reports in Power BI Mobile
    apps to extract business insights. 

      

22. What are the main business applications of Power BI?

    Since Power BI is a business intelligence application, we can apply it
    to a range of business spheres. Its most crucial applications include
    the following: 

    - Extracting meaningful business insights from the available raw data 

    - Creating compelling live reports and insightful interactive
    dashboards 

    - Identifying the current state of different departments or projects 

    - Tracking progress and KPIs of different departments or projects 

    - Detecting the strong and weak sides of a project from the standpoint
    of its performance 

    - Distributing the roles inside the team 

    - Granting access to the dashboards and reports to the relevant group
    of team members 

    - Displaying various statistics of a certain business on many different
    applications and websites in a   favorable light for a potential
    customer 

23. What kind of specialists typically use Power BI?

    - Project managers 

    - Business analysts 

    - Data analysts 

    - Data scientists 

    - IT specialists 

    - Data administrators 

    - Developers 

    - Report consumers 


24. Where is the data stored in Power BI?

    The data in Power BI is stored in the form of either fact tables which
    are quantitative, usually non-normalized data or dimension tables like
    the attributes and dimensions related to the data in a fact table  and
    in one of the two cloud repositories: 

    - Microsoft Azure Blob Storage: contains the data uploaded by the users 

    - Microsoft Azure SQL Database: contains all the metadata and the
    artifacts of the system 

    For both, encryption and passwords protect the data. 

25. What does self-service business intelligence (SSBI) mean?

    SSBI is a set of approaches and tools that enable end users --- even
    those without any background in BI (e.g., sales or marketing teams,
    product developers, etc.) --- to access, manipulate, analyze, and
    visualize the data in an intuitive way to make strategic, data-driven
    business decisions. 

26. What are content packs in Power BI?

    A content pack is a package of Power BI interrelated documents, such as
    dashboards, reports, and datasets, that are stored as a group. In Power
    BI, there are two types of such packages: service content packs from
    services providers like Google Analytics, Marketo, MailChimp, or Twilio
    that we can access by typing our account data, and organizational
    content packs created by the users of our company and shared with the
    entire organization or a selected group of people. 

27. How can we define the relationships between two tables in a data model in the Power BI Desktop?

    There are two approaches: 

    - Manual: by using primary and foreign keys 

    - Automatic: the relationships are identified automatically if the
    autodetect feature is switched on 

    To define the relationships between two tables, there shouldn\'t be any
    null values or duplicate rows in the data. Also, it\'s possible to have
    multiple relationships between tables (represented by dotted lines), but
    only one of them can be active (represented by a continuous line). 


## Spark 

1. What does Cluster Computing refer to?

Cluster computing refers to the process of sharing computation tasks among multiple machines which works together to act as a single machine

2. What does RDD stand for?

Resilient Distributed dataset

3. What key APIs does Spark provide?

RDD, DataFrame, Dataset (not available in Python)

4. What languages does Spark provide APIs for?

Java, Scala, Python, R

5. What does it mean when we say an RDD is a collection of objects partitioned across a set of machines?

An RDD is distributed, meaning the data is stored across multiple nodes. This helps the data to be resilient. Now, the data itself that is contained in the RDD is not copied across to create resilience, but the lineage of the RDD is, so that the data that is accessed after an action can still be accessed.

6. Explain the deficiency in using Hive for interactive analysis on datasets. How does Spark alleviate this problem?

Hive is more suited for batch processing with large amounts of data. It is not good with streaming data. As such, it runs slower on those interactive analysis processes. Spark, as it runs on RAM, can process streaming data much faster.

7. SparkSession vs SparkContext?

SparkContext
    - 	Spark SparkContext is an entry point to Spark and defined in org.apache.spark package since 1.x and used to programmatically create Spark RDD, accumulators and broadcast variables on the cluster. Since Spark 2.0 most of the functionalities (methods) available in SparkContext are also available in SparkSession. Its object sc is default available in spark-shell and it can be programmatically created using SparkContext class.

SparkSession
    -	SparkSession introduced in version 2.0 and and is an entry point to underlying Spark functionality in order to programmatically create Spark RDD, DataFrame and DataSet. It’s object ‘spark’ is default available in spark-shell and it can be created programmatically using SparkSession builder pattern.


8. What is the lineage of an RDD?

The list of transformations that the RDD has gone through.

9. RDDs are lazy and ephemeral. What does this mean?

The processing of transformations do not occur until an action is called, and the dataset is discarded from memory after use

10. What are the 4 ways provided to construct an RDD?

Parallelize, from another RDD, from DF/DS, from file

11. What does it mean to cache an RDD? *

Caching is an optimization tactic. It saves the data from an RDD action instead of deleting that data right away so that the RDD can be used again on a later transformation or action. This can be helpful if many different transformations and actions are called from a common RDD.

12. What does it mean to perform a parallel operation on an RDD?

Since the RDD is partitioned, operations can be done in parallel, where multiple executors can perform the same action across those partitions

13. Why does Spark need special tools for shared variables, instead of just declaring, for instance, var counter=0? * 

Because operations happen in parallel across multiple partitions, shared variables need to be able to be accessed in each of those places in memory

14. What is a broadcast variable? 

A broadcast variable is a read-only variable that is shared on all nodes. They are immutable and distributed. 

15. What is a Spark Application? Job? Stage? Task?

-	Application- main function 
-	Jobs- Work submitted to Spark. Created when an action occurs
-	Stage- Jobs are divided into stages
-	Task- Each stage is divided into tasks, the smallest unit of work for Spark


16. What’s the difference between cluster mode and client mode on YARN?

In cluster mode, the driver runs inside an application master process which is managed by YARN on the cluster and the client can go away after initiation. In client mode, the driver runs in the client process and the application master is only used for requesting resources from YARN	

17. What is an executor?  What are executors when we run Spark on YARN?

Executors are worker nodes’ processes in charge of running individual tasks in a given Spark job. 

18. Different ways to repartition?

-	.repartition
-	.coalesce (to reduce partitions)


19. What is the logical plan?  The physical plan?

-	The logical plan is the tree that represents both the data and schema. They depict the expected output
-	The physical plan decides what type of join, sequence of execution of many methods


20. How many partitions does a single task work on?

One

21. What is a Dataframe?

A DataFrame is a distributed collection of data organized into named columns, similar to a table in a relational database. It provides an abstraction for working with structured and semi-structured data in Spark, enabling efficient data processing and querying across large datasets. It is a higher-level abstraction compared to RDD's and offers a more optimized and user-friendly API for working with structured data. 

22. How would we go about using Spark SQL to query Dataframes?

- Initialize a SparkSession
- Create or load a DataFrame
- Register the df as a temporary view
- Run queries using spark.sql()


# Kafka 

1. What is Kafka? How is it different from Spark?


2. What are the various features of Kafka?


3. What are the various Kafka components?


4. Explain about Producer and Consumer.


5. What is a Topic and How to create It?


6. What is the role of a Broker?


7. What is a Consumer Group?


8. What are main APIs of Kafka?


9. What do you know about Partitions in Kafka?


10. What is the Zookeeper in Kafka?