### Define Data Sources, Structures, and Schemas
#### Data Sources
* Local file systems
* HDFS
* MapR-XD
* Hive
* HBase or MapR-DB
* JDBC databases 
* Cloud storage
* Any other data source


### Data Formats
* Spark provides wrappers for these types of files.
    - Text
    - Json
    - CVS
    - Parquet
    - Sequence File
    - Protocol Buffer
    - Object

Spark interacts with any Hadoop-supported formats.

### Datasets and DataFrames
1. Datasets
* Primary abstraction in Spark
* Collection of objects distributed across a cluster
* Immutable once created
* Fault-tolerant
* Persist or cache in-memory or on disk
* Data stored in tabular format
2. DataFrames
* DataFrame is the name for an untyped Dataset of type row, where “row” is a collection of
generic objects

 DataFrame does not understand the difference between a
string and integer at compile time, but once it is computed, it can be converted into a Dataset if
the schema is defined.

### Spark DataFrames
If our data type and schema are not explicitly defined, the construct will automatically be a
DataFrame. 

DataFrames can be converted into a Dataset of type “T” using the Case Class and inferring the
schema by reflection

 Once we know the schema and type for each column, we can call the
df.as[T] method to convert it into a Dataset.

### Resilient Distributed Datasets
Resilient Distributed Datasets, or RDDs, are the basic building blocks of Spark. When we build
Datasets in our applications, Spark uses RDDs under the hood for final computation.

### Schema
The schema of a Dataset is the logical visualization of how data stored in your system is
organized. 

### Ways of Defining Schema
1. Construct schema using Case Class
    - Use to construct Datasets when columns and types are known at runtime.
    - Scala Case Class restriction to 22 fields.
2. Construct schema programmatically
    - Use to construct Datasets or DataFrames when columns and types are not known until runtime.
    - Use if schema has more than 22 fields

 ### Start Spark Interactive Shell
    $SPARK_HOME/bin/spark-shell

Start the Interactive Shell by running spark-shell from the bin in the Spark install directory. 

### Create a Dataset
1. Import Classes
     - import spark.implicits._
2. Define a case class
    - case class Incidents(incidentnum:String,category:String,description:String,dayofweek:String,date:String)
    Remember -> if your case class has more than 22 fields you must define your schema programmatically.
3.  Load Data
    - val sfpdDS = spark.read.csv("/path to file/sfpd.csv").as[Incidents]
4. Register Dataset as View (optional)
    - sfpdDS.createTempView("sfpd")

#### Create DataFrame and Construct Schema Programmatically
1.  Import Classes
    - import spark.implicits._
      import org.apache.spark.sql.types._
2.  Create Schema Programmatically
    - val spdfSchema = StructType(Array(StructField("incidentnum",StringType,true),
    StructField("category",StringType,true),StructField("description",StringType,true),
    StructField("dayofweek",StringType,true)),StructField("date",StringType,true))
3.  Create DataFrame by Loading Data
    - 