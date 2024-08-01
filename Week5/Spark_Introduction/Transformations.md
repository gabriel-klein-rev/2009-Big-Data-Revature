# Cumulative for the  Transformations
<details><summary>Prerequisites and Learning Objectives</summary>

## Prerequisites

- Knowledge about how to create an RDD in Spark.

## Objectives

- To learn about different transformation operations that can be applied on RDDs.

---

</details>
<details><summary>Description</summary>

## Description

- Transformation operations are used in manipulating RDD data and returns new RDD. 

- Transformations are evaluated lazily means they are not executed until an action is performed on it. 

## Transformations in Spark-RDD

- To get the unique elements from an RDD, use `distinct` operation.

- Use `filter` transformation for selecting elements based on condition. 

- To sort the data present inside the RDD in ascending or descending order, use `sortBy` operation. It will sort the data in ascending order when the condition is true and in descending order when the condition is false.

- `Map` transformation applies operation on each element present in RDD and returns a new RDD. The length of an old RDD and a new RDD both are the same.

- `flatMap` transformation is like `map`, but it also flattens the result after doing map operation. The length of the old RDD and new RDD may or may not be the same in flatMap case.

- If you have two RDDs and you need the combined data of both the RDDs into new RDD then use `union` operation.

- If you have two RDDs and you need the common data of both the RDDs into new RDD then use `intersection` operation.

- There are two operations through which you can increase or decrease the number of partitions for the RDD. 
  - Use `repartition` operation for increasing the number of partitions and `coalesce` for decreasing the number of partitions.

- Use `groupByKey()` to group each input key to an iterable value in the RDD. This will result in shuffling of data over the network.

- Similar to `groupByKey()` there is one more operation we can use on the Dataset that is `reduceByKey()`. Both do similar operation and result in same output, but the key difference between both is that reduceByKey() do the map side combine but groupBykey() doesn't.

---

</details>
<details><summary>Real World Application</summary>

</details>
<details><summary>Implementation</summary> 

## Implementation

- For applying some operations on RDD, let's first create the RDD.

```
data = [1, 2, 3, 3, 4, 5, 2]
rdd1 = sc.parallelize(data)
``` 


- Using `distinct()` to get unique elements.
```
rdd1.distinct().collect()
```


- Using `filter` to get elements which are less than 3.
```
filter_rdd = rdd1.filter(lambda x: x<3)
filter_rdd.collect()
```
 

- `sortByKey()` example 
```
rdd1.sortBy(lambda x: x, true).collect()
rdd1.sortBy(lambda x: x, false).collect()
```


- Using `map()` to split the list of items. 
```
rdd1 = sc.parallelize(["hello my friend", "how are you"])

rdd1.map(lambda x: x.split(" ")).collect()
```
- This will result in:
> [("hello", "my", "friend"), Array("how", "are", "you")]

- Using `flatMap()` to split the list of items.
```
rdd1 = sc.parallelize(["hello my friend", "how are you"])

rdd1.flatMap(lambda x: x.split(" ")).collect()
```
- This will result in:
> ["hello", "my", "friend", "how", "are", "you"]


- Applying `union()` on RDDs. 
```
rdd1 = sc.parallelize([1, 2, 3])
rdd2 = sc.parallelize([4, 5, 6])

rdd1.union(rdd2).collect()
```
- Output will be:
> [1, 2, 3, 4, 5, 6]

- Applying `intersection()` on RDDs. 
```
rdd1 = sc.parallelize([1, 2, 3, 5])
rdd2 = sc.parallelize([4, 5, 2])

rdd1.intersection(rdd2).collect()
```
- Output will be:
> [2, 5]


- Example of `coalesce` and `repartition`. 

```
rdd1 = sc.parallelize([10, 20 , 30 , 20 , 40])
rdd2 = rdd1.repartition(5)
rdd3 = rdd2.coalesce(2)
```

**Note:**
> `repartition` can be used for increasing or decreasing the number of partitions but, it is recommended to use `coalesce` when the need is to decrease the partitions as it doesn't result in shuffling of all the data over the network.


- Example of `groupByKey()`

```
rdd1 = sc.parallelize(["A", "B", "B", "D", "A"])
rdd2 = rdd1.map(lambda char : (char, 1))
rdd3 = rdd2.groupByKey().map(lambda a,b : (a, sum(b)))
```

- Example of `reduceByKey()`.
```
rdd1 = sc.parallelize(["A", "B", "B", "D", "A"])
rdd2 = rdd1.map(lambda char : (char, 1))
rdd3 = rdd2.reduceByKey(lambda a,b : (a + b))
```
**Note:**
> - `groupByKey()` and `reduceByKey()` both come under wide transformation that means they both result in shuffling of data between partitions.
> - To choose between both depends on the size and type of data. Use `reduceByKey()` over `groupByKey()` as it does the map side combine and hence sends less amount of data to reduce over the network and preferable if we apply some aggregate functions like sum, average on the dataset. 
> - Go for `groupByKey()` when there is no need of map side combine or when the data is less in size. 

---

</details>
<details><summary>Summary</summary> 

## Summary 

- Transformation operations are used in manipulating data present inside an RDD and, it returns new RDD. They are evaluated lazily means they are not executed until an action is performed on it. 

- Examples of Transformations in Spark-RDD are filter(), map(), flatMap(), reduceByKey(), etc.

---

</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
