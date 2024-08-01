# Cumulative for the  Actions
<details><summary>Prerequisites and Learning Objectives</summary>

## Prerequisites

- Knowledge about how to create an RDD in Spark.

## Objectives

- To learn about different action operations that can be applied on RDDs.

---

</details>
<details><summary>Description</summary>

## Description

- Actions are the operations that return a non-RDD value when applied on RDD. The value of action gets stored in the driver program. Example of action operations are count(), collect(), first(), take(), etc.

## Actions in Spark-RDD

- To read a RDD result use `collect` operation on it. It will return all the data present inside RDD.

- To get the total number of elements present in the RDD, use `count` operation.

- `reduce` operation gives the computed summarized result based on function applied on RDD. 

- Use `first` if the need is to get the first item from RDD. `first` is an action. 

- If the requirement is to get the first "n" items from RDD, then use `take` operation.

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

- Use of `collect()`
```
rdd1.collect()
```
> Output: [1, 2, 3, 3, 4, 5, 2]

- Use of `count()` 
```
rdd1.count()
```
> This will return 7 as an output.


- Use of `reduce()`
```
rdd1.reduce(lambda x,y : x+y)
```
> The output will be the sum of all the elements of RDD. 


- Use of `first()`
```
rdd1.first()
```
> The output will be the first element of an RDD. 


- Use of `take()` 
```
rdd1.take(3)
```
> This will return the first 3 elements of an RDD. 

---
</details>
<details><summary>Summary</summary> 

## Summary

- Actions are the operations which brings laziness of transformations into work. Without applying any action function on transformation rdd it is not possible to generate result.

- Examples of actions in Spark-RDD are collect(), count(), take(), reduce(), etc. 

---

</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
