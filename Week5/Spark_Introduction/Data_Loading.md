# Cumulative for the  Data Loading and saving through RDDs
<details><summary>Prerequisites and Learning Objectives</summary>

## Prerequisites 

- Knowledge of different filesystems.

## Objectives

- To learn about how to read/load a data from filesystem to RDD 
- To learn about how to store the result of RDD to the filesystem.

---
</details>
<details><summary>Description</summary>

## Description

- In this content we are going to see how to load/read a file stored in any location of any filesystem configured with Apache Spark and then how to store it back to filesystem. 

## Loading/Reading Data into RDD

- To load the data of a file into an Spark RDD, we can use two methods: 
  - `textFile()`
  - `wholeTextFiles()`

- **textFile():** This method is used to read the file as a collection of lines. It can read a single file, multiple files on the same folder, multiple files from different folders of any filesystem such as local filesystem, Hadoop's HDFS and Amazon S3. It has a optional parameter to include number of partitions against the default partitions created by spark based on the file size.

- Syntax:
```
SparkContext.textFile("path_of_the_file")
```

- **wholeTextFiles():** This method returns a pair-RDD that contains a filename and the content of the file in the form of tuple. 

- Syntax:
```
SparkContext.wholeTextFiles("path_of_the_file")
```

## Storing/Saving an RDD to FileSystem 

- After applying the transformation operations on your data you may want to store the final result back to the filesystem. To do so, we have one method as `saveAsTextFile()`, which helps in saving the data into one or many part files on the filesystem. 

- Syntax:
```
SparkContext.saveAsTextFile("FileSystem_path")
```

---
</details>
<details><summary>Real World Application</summary>

</details>
<details><summary>Implementation</summary> 

## Implementation

- For this implementation, we are using sc as sparkContext(). 

- Reading a text file stored in local file system having path as "abc/xyz/demo.txt.
```
rdd1 = sc.textFile("/abc/xyz/demo.txt")
```

- Reading a text file with partition count.
```
rdd1 = sc.textFile("/abc/xyz/demo.txt", 4)
```

- Reading multiple files stored in same directory.
```
rdd1 = sc.textFile("/abc/xyz/demo.txt", "/abc/xyz/test.txt")
```

- Reading all files stored in same location.
```
rdd1 = sc.textFile("/abc/xyz/*")
```

- Reading multiple files stored in different location.
```
rdd1 = sc.textFile("/abc/pqr/test.txt", "/tvs/xyz/demo.txt")
```

- Reading file stored in HDFS.
```
rdd1 = sc.textFile("hdfs://abc/xyz/demo.txt")
```

- Reading file stored in Amazon S3. 
```
rdd1 = sc.textFile("s3a://abc/xyz/demo.txt")
```

- To get the filename along with its content use `wholeTextFiles()`.
```
rdd1 = sc.wholeTextFiles("/abc/xyz/demo.txt")
```

- To save the data of an RDD to the file in local filesystem use `saveAsTextFile()` method. Let's say we have an RDD named as "rdd1" which we have to store in the local filesystem under the "abc/xyz" directory.
```
rdd1.saveAsTextFile("/abc/xyz")
```

- To save the data of an RDD to HDFS location. 
```
rdd1.saveAsTextFile("hdfs://abc/xyz")
```

- To store the data of an RDD to Amazon S3 location.
```
rdd1.saveAsTextFile("s3a://abc/xyz") 
```

**Note**
> All these `saveAsTextFile` operations will create many partition files representing the RDD as part-00001, part-00002, etc. under the /abc/xyz directory, where each part file consists of some data of an RDD.

---

</details>
<details><summary>Summary</summary> 

## Summary

- Spark allows to load data from filesystems such as local, HDFS and S3 to an RDD. RDD provides two methods using which we can read from filesystem, one is `textFile()` and another one is `wholeTextFiles()`. 

- To load the data present in files stored in HDFS or S3, we must use the hdfs:// and s3a:// as prefix to the file path.

- To store the result of RDD back to any file system, after applying transformations on it, use `saveAsTextFile()` method. 

---

</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
