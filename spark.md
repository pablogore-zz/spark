### What is apache spak?
* Cluster computing platform on top of storage layer
* Extends MapReduce with support for more components
    - Streaming
    - Interactive analytics
* Can run in-memory or on disk


### Spark
* Parallel in-Memory processing across platform
* Multiple data source , applications , users.

### Spark on Hadoop
The combination of Spark and Hadoop takes advantage of both platforms, providing:
* Analytics over operational Hadoop applications
* Reliable unlimited scale

#### What are the advantages of using Apache Spark?
It is compatible with Hadoop, is very fast, is easy to develop applications with, provides multiple language support, and offers a unified stack of libraries.

### Define Spark Components
agregar imagen  

The spark cluster consists a two processes , a Drive programm and multiples workers node.  
The Driver Program run on the driver machine which is commonly an edge node,and the workers programs run on cluster nodes or on local threads.

The first things the program does is to create a SparkSession object , that tells Spark how and where access to the cluster.
SparkSession connect to the cluster manager.
Cluster manager allocated resources across apllications .
Once connected Spark required executors in the workers node .
And executor is a process that runs computations and store data from you application.
Jar or Python files pass the spark Session or send to the executors.
SparkSession send the task to the executor to run , the workers nonde can acces data store sources to injest and output data as need it.


### Spark Dataset
1. Primary abstraction in Spark
2. Collection of objects distributed across nodes in a cluster
3. Data operations performed on datasets
4. Once created, Datasets are immutable
5. Can persist, or cache, in-memory or on disk
6. Fault-tolerant

#### Spark Dataset Operations, Transformations, and Actions
* Operations:
    - There are two types of data operations you can perform on a Dataset: transformations and actions.

* Transformations:
    - A transformation operates on an existing Dataset, and returns a new Dataset. A new Dataset is required because Datasets are immutable.

* Actions:
    - An action will return a value

You can combine transformations and actions in any order, to process and analyze your data.    