---
marp: true
theme: eventstore
paginate: true
header: '![topbar](../themes/media/header.png)'
footer: '![eventstore](../themes/media/eventstore.png)'
---

<!-- markdownlint-disable --> 
<!-- _class: cover -->
<!-- _paginate: false -->
<!-- _header: " " -->
<!-- _footer: '![eventstore](../themes/media/eventstore-inverse.png)' -->

![bg](../themes/media/background-darkblue.png)

# EventStoreDB Overview



---

<!-- _class: title-body -->

# In This Section You Will Learn how to:


<box>

* Differentiate the unique functionality of EventStoreDB from other systems
* Install EventStoreDB from a binary distribution
* Add events to EventStoreDB streams
* Configure stream settings to delete old events
* Use the EventStorDB webui
</box>


---

<!-- _class: title-body -->
# Outline


<box-half-left>

* EventStoreDB overview
* EventStoreDB comparison to other DBs 
* Introduction to events and streams
* Concurrency
* EventStoreDB internals 
* Events
* Reading streams
* Database configuration
* <span style="color:blue;">Lab: Install EventStoreDB</span>
* Truncate, delete, and configure streams
* Subscriptions

</box-half-left>

<box-half-right>

* Projections:  System & User Defined
* <span style="color:blue;">Lab: Exploring the Projection Engine</span>
* EventStoreDB internals:  Storage on Disk
* <span style="color:blue;">Lab: Files used by EventStoreDB</span>
* Write path
* Read path
* System streams
* Stream access control
* <span style="color:blue;">Lab: Modify stream access control List</span>
* <span style="color:blue;">Lab (optional): Stress test the server</span> 

</box-half-right>


---

<!-- _class: cover -->
<!-- _paginate: false -->
<!-- _header: 
 -->
<!-- _footer: '![eventstore](../themes/media/eventstore-inverse.png)' --> 

![bg](../themes/media/background-darkblue.png) 

# EventStoreDB Overview

## 


---

<!-- _class: title-body -->
# EventStoreDB

<box>

**Designed for event-native applications, EventStoreDB immutably stores every event to provide:**  

<br/>

* Context rich business data 
* Decoupled complex systems 
* Increased scalability and flexibility
* Contextual, real-time insights
* Future proofed architecture

</box>


---

<!-- _class: title-body -->
# EventStoreDB Server: Deployment Options

<box-half-left>

**EventStoreDB**

* Compatible with Docker, Linux, Windows
* Open Source and free to use
    * As of 24.10, [ESLv2 license model](https://www.eventstore.com/blog/introducing-event-store-license-v2-eslv2)
* Enterprise Offerings
* Self-managed on-prem or cloud

</box-half-left>
<box-half-right>

**EventStoreDB Cloud**

* AWS, Azure, Google
* Security and Compliance
* Scalability and High Availability
* Managed Service

</box-half-right>



 ---

 <!-- _class: title-body -->
 # EventStoreDB Clients
 
 
 
<box-half-left>

 **GRPC based clients**

* Node.js
* .NET
* Java
* Python
* Rust
* Go

 

</box-half-left>
<box-half-right>
 
 **HTTP API**

 * Read/Write events
 * Admin functions
 * Add users/groups
 * Enable/Disable features
 * Retrieve logs/metrics


</box-half-right>

---

<!-- _class: title-body -->
# EventStoreDB


<box>

**Builds Data Immutability**
EventStoreDB stores data as a series of immutable events over time to provide for greater data integrity and transparency.

<br/>

**Decouples Core Logic**
With EventStoreDB you can decouple your external systems with asynchronous messaging making your system cleaner and more compact.

<br/>

**Creates a Source of Truth**
Events in EventStoreDB are stored as a reliable log of the changes in your application. 

</box>



---

<!-- _class: cover -->
<!-- _paginate: false -->
<!-- _header: 
 -->
<!-- _footer: '![eventstore](../themes/media/eventstore-inverse.png)' --> 

![bg](../themes/media/background-darkblue.png) 

# Comparing EventStoreDB to Other Systems

## 

---

<!-- _class: title-body -->
# Key Concepts


<box>


When using any database (SQL, Document, NoSQL, or EventStoreDB), its critical to understand the tools available to: 

<br>

* Manage potential conflicts between multiple readers and writers
* Enforce constraints
* Retrieve data or subsets of data
* Deletion process

<br/>

This section discusses those concepts and compares EventStoreDB to other types of databases.   

</box>


---

<!-- _class: title-body -->
# How Data is Stored


<box>

Some systems store data as a document that can be read and rewritten as a new version. Others store data as a table with a collection of rows containing typed columns. 
<br/>
This section breaks down the topic into:

* Unit of storage
* Available operations
* Schemas
* Pub-sub functionality


</box>


---

<!-- _class: title-body -->
# EventStoreDB: Unit of Data Storage


<box>

**Comparing databases and their basic units of storage**
<br>

<style scoped>
    table {
        margin: 0 auto;
    }
</style>

<style>
    .slide{
        font-family: 'Museo sans';
    }
</style>

| Database Type | Base Unit of Storage| 
|---------------|---------------------|
|Relational database (MySQL, Postgres, Oracle)|Rows
|Document store(MongoDB, Cosmos)|Documents
|Data lake |Combination of documents and rows
|EventStoreDB| Events |


</box>


---

<!-- _class: title-body -->
# Event Details


<box>

* Appended in order to a stream
* Immutable

</box>


---

<!-- _class: title-body -->
# Comparison by Supported Operations


<box>

Some systems allow granular updates/deletes.  Others group data into subsets and allow granular updates/deletes on those subsets. 
<br/>
Some systems allow updates of previously written data in place.  Others replace the previous version with a new version containing the update/delete.
<br/>
The following slide(s) summarize those differences


</box>

<!-- Instructor Note
This is key to enabling proper understanding and use of EventStoreDB, certain classes may already understand the differences, but it is critical to have a baseline understanding, go as deep or as shallow as the class requires  -->

---


<!-- _class: title-body -->
# Overview of EventStoreDB, Supported Operations


<box>

**Comparing databases and their supported operations** 
<br>

<style scoped>
    table {
        margin: 0 auto;
    }
</style>

<style>
    .slide{
        font-family: 'Museo sans';
    }
</style>

| Database Type| Supported Operations |
|--------------|----------------------|
|Relational database (MySQL, Postgres, Oracle)|Create, Read, Update, Delete (rows)|
|Document store (MongoDB, Cosmos)|Create, Read, Update, Delete (documents) |
|Data lake |Create, Read, Update, Delete (combination)|
|EventStoreDB|Create(append), Read, Delete* (events)|



</box>



---

<!-- _class: title-body -->
# Schemas

<box-half-left>

**Systems that enforce schemas on write**

* Relational databases

<br>

**Systems that define schema on read**

* Data Lakes *(Typically SQL layers over semi-structured distributed storage)* 

</box-half-left>

<box-half-right>

**EventStoreDB**

* EventStoreDB neither manages or enforces schemas
* Schema enforcement/management is the responsibility of the application

</box-half-right>


---



<!-- _class: title-body -->
# Reading Data


<box>

|Database Type | Read Path | Subscriptions |
|--------------|-----------|---------------|
| Relational | Granular reads or scans/joins with filters interpreted and applied by the server | No subscriptions |
| NoSQL | Differs per system | Differs per system |
| EventStoreDB | Read Stream/projection sequentially forwards/backwards | Subscriptions to streams/projections |


</box>


---



<!-- _class: title-body -->
# Data Transformations on Write


<box>

|Database Type | Write Transformation | 
|--------------|-----------|
| Relational | Triggers, Stored Procedures |
| NoSQL | Differs per system | 
| Data Lake | Differs per system |
| EventStoreDB | Projections |
</box>

<!-- Instructor Note, if you wanted to demonstrate an eventbeing appended and you had a database instance available go ahead -->


---



<!-- _class: cover -->
<!-- _paginate: false -->
<!-- _header: 
 -->
<!-- _footer: '![eventstore](../themes/media/eventstore-inverse.png)' --> 

![bg](../themes/media/background-darkblue.png) 

# Events & Streams

##

---

<!-- _class: title-body -->

# Introduction to Events and Streams


<box>

Since EventStoreDB Stores immutable events appended to streams, lets start with a review of each item. 

* Events
* Streams

</box>


---

<!-- _class: title-body -->
# Events


<box>

**General definition**

Events are schema-less, immutable bytes appended in order and guaranteed to be retrieved in that order. 

<br>

**The nuance of events**

Events represent meaningful actions that happened at a specific time and altered the state of a business entity. <b>Events</b> can contain all the relevant information about the action or decision that occurred, allowing future systems or services to understand the circumstances in which the event happened. 

</box>


---

<!-- _class: title-body -->
# Events: Bytes or JSON


<box>

<br>

Events are stored as **bytes**, but frequently JSON format is used. 

<br>

Some internal EventStoreDB subsystems expect, or generate, JSON formatted events. 


</box>


---

<!-- _class: title-body -->
# Events Review


<box>


<br>

Events are:
* Immutable
* Ordered
* Schemaless
* Stored in a stream 
<br>


</box>


---

<!-- _class: title-body -->
# Streams


<box>

Events are sequentially organized into logical <b>streams</b> containing related events.

<br>

Streams are:
* Fine-grained
* Subscribeable
* Unit of consistency guarantees
* Created when an event is appended to it

</box>


---

<!-- _class: title-body -->
# Fine-grained Streams


<box>

A well designed EventStoreDB application will typically revolve around a collection of fine grained streams. 




</box>

<!-- For example, if EventStoreDB was used to track the trips taken by your vehicle from the day you purchased it, instead of a single stream of "All Trips", you would have a collection of smaller streams, My_Car_Jan1, rather than My_Car_2024 -->

---

<!-- _class: title-body -->
# Streams:  Subscribable


<box>

EventStoreDB in addition to storing immutable, consistently ordered events also has pub-sub funcionality

<br>

**Subscription Levels**
* $all stream
* Individual stream
* Projection

</box>


---


<!-- _class: cover -->
<!-- _paginate: false -->
<!-- _header: " " -->
<!-- _footer: '![eventstore](../themes/media/eventstore-inverse.png)' -->

![bg](../themes/media/background-darkblue.png)

# Concurrency

EventStoreDB supports an Optimistic Concurrency Check on appends. <br> This Module will demonstrate the available features.

<!-- Hello and welcome to the template sample video, this is the cover layout -->

---






<!-- _class: title-body -->

# Optimistic Concurrency Control Defined

<box>

Instead of locking first in order to guarantee success of a transaction, OCC assume success (that is the optimistic part) and fails the transaction if a conflict is detected.

</box>

---

<!-- _class: title-body -->

# Pessimistic Concurrency Control Defined

<box>

Lock the record for your exclusive use until you have finished with it.

</box>

---


<!-- _class: title-body -->

# When are the Concurrency checks made?

<box>

The concurrency check is defined on the write of an event. If the concurrency check fails then the write of that event fails.

</box>

<!-- The Concurrency check specified by the write operation is verified at the time of writing -->

---

<!-- _class: title-body -->

# Available Settings

<box>

* Any Integer Value (`expectedRevision: n`)
    * Must be that Event Number  <br/>
* `ExpectedVersion.NoStream / StreamState.No_Stream`
  * Stream Does Not Exist Yet <br/> 
* `ExpectedVerstion.streamExists/StreamState.Exists`
    * Stream Exists, **Event number** not checked <br/>
* `ExpectedVersion.Any` / `StreamState.Any`
   * *Disables* concurrency Check        

</box>


---

<!-- _class: title-body -->

# Event ID

<box>

Although not specifically a concurrency check, you should be aware that

* Event Ids are a UUID, unique over the store, supplied by the writer.
* If there are two writes in rapid succession with the same Event ID, the server may write only one of the events to disk.
* If you do not provide an EventID, the client will assign one.
* Best practice is to generate and manage the Event ID in your application.

</box>


---

<!-- _class: title-body -->

# Use Case for this example



<box>

Issue/support ticket management system

* Streamname = Support ticket id
* EventTypes [TicketCreate, TicketComment, TicketAssigned, TicketClosed]

</box>



---

<style scoped>
section {
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
}
</style>

# Example Stream

<img src="./media/stream.png" alt="stream" width="1000" >


---

<!-- _class: cover -->
<!-- _paginate: false -->
<!-- _header: " " -->
<!-- _footer: '![eventstore](../themes/media/eventstore-inverse.png)' -->

![bg](../themes/media/background-darkblue.png)

# Examples 

## The following slides are examples of each of the settings


<!-- 
In the following slides we will review examples of each setting.

 -->
---

<!-- _class: title-body -->

# Integer Value

<box>

* This is the most commonly used setting for most applications.
* It is typically used to guarantee the state of the stream has not changed between the time that you read and the time that you write.


</box>



---

<!-- _class: title-body -->

# Use Case

<box>

* A stream is created when a user fills out a web form to open a support ticket. 
* Any one of the Support Engineers can view the ticket and assign it to themselves. 
* When closing a ticket the it is important that the support engineer has read all the issues present in the stream. Using ExpectedVersion.(Integer) can guarantee that. 

<br>

* Bonus Question: Which other EventType in this use case would use expected.Version = integerValue

</box>


---


<style scoped>
section {
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
}
</style>

![width:800px](./media/Integer_Value_support_ticket.jpg)

<!-- The lower example fails, bacause a comment was appended after the read -->

---

<!-- _class: title-body -->

# No Stream

<box>

Specifies the expectation that the target stream does not yet exist.

</box>

<!-- 
 -->

---

<!-- _class: title-body -->

# Use Case

<box>

* Used when you want your application to create a new stream, by appending an event to it. If a stream of that name has already been created you want the operation to fail.
* For our ticketing system application this might be used when the customer first creates the ticket. 

</box>

<!-- 
In our use case of support tickets multiple customers may be using the application at once. If our application issues ticket numbers incrementally, for example ticket_01, ticket_02, ticket_03 etc. In that case if there is a race condition to create ticket_04, one operation will succeed, and the other will have to retry.

 -->

---
<!-- _class: title-body -->

<box style="display: flex; align-items: center; justify-content: center;"> 

<img src="./media/NoStream_support_ticket.jpg" width="1050">

</box>

<!-- This diagram provides a visualization of the use of No Stream -->


---

<!-- _class: title-body -->

# Stream Exists

<box>

Specifies the expectation that the target stream or its metadata stream has been created, but does not expect the stream to be at a specific event number.

</box>

<!-- The Stream Exists Concurrency check sets the expectation that the stream your application is appending an event to, must already exist.
-->


---

<!-- _class: title-body -->

# Use Case

<box>

You would use this when you want to guarantee the stream exists before writing your event. <br/>
In our Support Ticket System example, TicketComment events might use this level of concurrency check.
<br/>Multiple comment events from multiple sources could be appended to the stream without regards to other TicketComment events occurring. 
<br/>The risk is that TicketComment events might be appended after a TicketClosed event. 

</box>

<!-- In our support ticket example the Comment Added Event would want to verify that the stream exists before appending an event.  -->

---

<style scoped>
section {
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
}
</style>

![width:1050px](./media/Stream_exists_support_ticket.jpg)

<!-- 
This diagram demonstrates the use of the Stream Exists concurrency check. 
 -->

---

<!-- _class: title-body -->

# Expected Version Any

<box>

* Disables concurrency check
* This is the most liberal setting
* It is often used for examples and demos, but in most cases your application will want to perform some sort of check

</box>


---


<!-- _class: title-body -->


<box style="display: flex; align-items: center; justify-content: center;">

<img src="./media/ExpectedVersionAny_support.jpg" width="1000">

</box>

<!-- 
This diagram shows what would happen if our support ticket system disabled concurrency checks on comment added events. 

As you see a ticket stream may be  created that starts with a Comment Added event rather than a ticket created event.
 -->

---

<!-- _class: cover -->
<!-- _paginate: false -->
<!-- _header: 
 -->
<!-- _footer: '![eventstore](../themes/media/eventstore-inverse.png)' --> 

![bg](../themes/media/background-darkblue.png) 

# Deleting Events/Streams

## Stream Configuration

---

<!-- _class: title-body -->

# Event Removal Triggers


<box>

* Stream Deletion
    * Hard
    * Soft
* Stream Configuration
    * MaxAge
    * MaxCount    

</box>


---


<!-- _class: title-body -->
# Stream Configuration


<box>

Each stream has an optional metadata stream for configuration

* \$$<Stream_Name>


**Commonly used stream settings:**

**maxAge**
    * Older events are deleted  

**maxCount**
    * Events are deleted that violate maxCount

**ACL**
    * Access Control List


</box>


---






<!-- _class: cover -->
<!-- _paginate: false -->
<!-- _header: 
 -->
<!-- _footer: '![eventstore](../themes/media/eventstore-inverse.png)' --> 

![bg](../themes/media/background-darkblue.png) 

# EventStoreDB Internals

##


---

<!-- _class: title-body -->

# EventStoreDB Internals: Event Management


<box>
 

* EventStoreDB is a sequenced log of events
* As events are written, they are appended to a global log
* The global log contains all user and system generated events
* The global log can be read as the $all stream
* Events are stored in consistent order
* Events have a permanent sequence number
* LSM(Log Structured Merge Tree) structure 

</box>


---


<!-- _class: title-body -->
# Streams Illustrated


<box>

<img src="./media/all_stream.png" alt="streams" width="800" >

</box>


---

<!-- _class: title-body -->
# Streams Illustrated

<box>

<img src="./media/all_stream1.png" alt="streams" width="800" >

</box>


---

<!-- _class: title-body -->
# Streams Illustrated


<box>

<img src="./media/all_stream2.png" alt="streams" width="800" >


</box>


---

<!-- _class: title-body -->
# Streams Illustrated


<box>

<img src="./media/all_stream3.png" alt="streams" width="800" >



</box>


---

<!-- _class: title-body -->
# Streams Illustrated


<box>

<img src="./media/all_stream4.png" alt="streams" width="800" >

</box>


---

<!-- _class: title-body -->
# EventStoreDB Internals: Streams and Events


<box>

* An Event is part of a stream 
* An Event is an entry in a global log known as the $all stream 
* A stream is a subset of the $all stream
* The index contains information on which events are in which stream



</box>


---

<!-- _class: title-body -->
# EventStoreDB Optimizations


<box>

**General Considerations**

<br>

* Durability (Crash tolerance)
* Disk access patterns
    * Sequential reads
    * Random seeks 

<!-- 
Instructor should be able to describe the general aspects of these terms  

The main point is that the append only log is sequential write, and the structure of a stream is more or less sequential-ish reads. 

The LSM structure was designed for these issues
-->
</box>


---

<!-- _class: title-body -->
# EventStoreDB Optimizations



<box>

EventStoreDB has the following design features: 
<br>

* Pre-allocated append-only log that enables high throughput and sequential writes 
* Log-structured merge-tree(LSM) for high write capacity for the additional data storage (stream indexes)


</box>

<!-- The pre-allocated log avoids fragmentation, favoring sequential reads 
* It is beyond the scope of this course to go into details of LSM’s, but RocksDB is a widely used system, that also makes use of LSM’s https://rocksdb.org/
* And this site is useful, https://disc-projects.bu.edu/compactionary/index.html, and this animation is great https://disc-projects.bu.edu/compactionary/research.html -->



---













<!-- _class: cover -->
<!-- _paginate: false -->
<!-- _header: 
 -->
<!-- _footer: '![eventstore](../themes/media/eventstore-inverse.png)' --> 

![bg](../themes/media/background-darkblue.png) 

# Event Details

##

---

<!-- _class: title-body -->
# Event Details:


<box>

* **Type**: A string, defined by the application
* **Stream**: The stream the event belongs to
* **Id**: UUID string, unique over the store *(typically generated by the client)*
* **Revision**: A number representing the position in the specific stream this event is part of.
* **Data**: A ByteArray of application generated data (often JSON formatted)




</box>


---

<!-- _class: title-body -->
# Event Details


<box>


* **Metadata**: A ByteArray of user or system generated metadata
    * **System metadata**
        * **Timestamp**: The date and time when the event was appended to the store, controlled by the database
    * **Application Metadata**: 
        * Any application-level metadata, no assumptions should be made on the data format
        * **CorrelationId**: supplied by the application
        * **CausationId**: supplied by the application



</box>


---
 






<!-- _class: title-body -->
# Event Details


<box>

* **Event ID**: (GUID) can be used for deduplication when appending data to the store
* **Revision #**: Typically used for optimistic locking
* **System metadata timestamp**: In the system metadata should never be used for application-level purposes
* **Revision & positions**: Are strictly increasing in their respective streams
    * These numbers are managed by the Event Store server only.

</box>


---

<!-- _class: title-body -->
# Properties of an Event


<box>

**Immutable**: Once an event is written it can not be modified
**Guaranteed Order**: The ordering of events is global across all events and streams in the database


</box>

--- 

<!-- _class: title-body -->

# Event Example: Support Ticket


<box>


No | Stream | Type | Timestamp 
---| ----- |-----|---|
0 | ticket_0001 | TicketCreate | 2025-01-09 19:13:13|

Data:

```
{
  "user": "tom",
  "customer_id": "1",
  "Issue summary": "When I create a new user I get a \"quota exceeded error\" ",
  "time stamp": "1736467966"
}
```				
Metadata

```{}```

EventId:	46765067-5067-5067-5067-173646765067

</box>

Note, the file 

---

<!-- _class: title-body -->
# Deleting Events


<box>

Event deletion occurs when:

<br>

* Event is older than $maxAge stream setting
* Event violates $maxCount stream setting
* The stream itself is deleted

</box>


---



<!-- _class: cover -->
<!-- _paginate: false -->
<!-- _header: 
 -->
<!-- _footer: '![eventstore](../themes/media/eventstore-inverse.png)' --> 

![bg](../themes/media/background-darkblue.png) 

# Reading Streams


---

<!-- _class: title-body -->
# Reading Streams


<box>

The following options are availalbe when reading a stream:

<br>

* Read forward 
* Read backward
* Read n number of events
* Start reading from any position in the stream


</box>


---

<!-- _class: title-body -->
# Reading streams: example code


<box>

Starting from a particular location, reading backwards, limit 100 events
<br>

```
events = client.get_stream(
    stream_name="demo",
    stream_position=2,
    limit=100,
    backwards=True
)


```

</box>


---

<!-- _class: title-body -->
# Reading the $all stream


<box>

When reading from the $all stream, you must provide byteoffset of the event instead of event number

<br>

<pre>
event_all = client.read_all(commit_position=955159)

for event in event_all:
     # Doing something productive with the event
     print(f"Event: {event}")

</pre>
</box>


---

<!-- _class: cover -->
<!-- _paginate: false -->
<!-- _header: -->
<!-- _footer: '![eventstore](../themes/media/eventstore-inverse.png)' --> 

![bg](../themes/media/background-darkblue.png) 

# Database Configuration 



---

<!-- _class: title-body -->
# Configuration Sources


<box>

* Configuration file
* Command line
* Environment variables

</box>


---

<!-- _class: title-body -->
# Configuration Precedence

<box>

1 - Command line options
2 - Environment variables
3 - Configuration files (YAML and JSON)

<br>


This order of precedence allows for flexible configuration management, where you can set default values in configuration files, override them with environment variables if needed, and use command line options for the highest priority settings.

</box>


---

<!-- _class: title-body -->
# Common Configuration Options


<box>


* [**ClusterSize**](https://developers.eventstore.com/server/v24.10/configuration/cluster.html#cluster-size):  Number of nodes in the cluster (excludes read-only replicas)
* [**DiscoverViaDns**](https://developers.eventstore.com/server/v24.10/configuration/cluster.html#cluster-with-dns): Whether to enable DNS discovery
* [**GossipSeed**](https://developers.eventstore.com/server/v24.10/configuration/cluster.html#cluster-with-gossip-seeds): A list of hosts to gossip to (when DNS discovery is disabled)
* [**ClusterDns**](https://developers.eventstore.com/server/v24.10/configuration/cluster.html#cluster-with-dns): The DNS discovery endpoint (when DNS discovery is enabled)

</box>


---

<!-- _class: title-body -->
# Common Configuration Options


<box>

**IP / Hostname settings**

* [**ReplicationIp**](https://developers.eventstore.com/server/v24.10/configuration/networking.html#interface-and-port) (formerly IntIp): IP address to bind to for internal node-to-node communication
* [**NodeIp**](https://developers.eventstore.com/server/v24.10/configuration/networking.html#http-configuration) (formerly ExtIp): IP address to bind to for node-to-node and node-to-client communication
    * *ReplicationIp and NodeIp will be the same if you are using a single network interface (which is true for most configurations)*
* **NodeHostAdvertiseAs** (previously ExtHostAdvertiseAs): The hostname to advertise the node as on the gossip endpoint. This is usually changed to the node’s hostname when you are using certificates to prevent certificate name mismatches.
* **AdvertiseHostToClientAs**: The hostname to advertise the node as on the client gossip endpoint. This is usually used when clients are connecting behind a NAT or set to match the node’s hostname when using certificates.

</box>


---

<!-- _class: title-body -->
# Common Configuration Options


<box>

* [**Log rotation**](https://developers.eventstore.com/server/v24.6/diagnostics/logs.html#log-file-interval) (LogFileSize, LogFileInterval, LogFileRetentionCount)
* [**ReaderThreadsCount**](https://developers.eventstore.com/server/v24.10/configuration/#readerthreadscount)
    * Can be increased if reader threads are saturated
* **Projection settings**
    * RunProjections - whether to start the projection subsystem
    * StartStandardProjections - whether to start the built-in system projections


</box>


---

<!-- _class: title-body -->
# Commonly used configuration options


<box>

* [SkipIndexVerify](https://developers.eventstore.com/server/v24.10/configuration/indexes.html#skip-index-verification)
* Certificate settings 
* [CachedChunks / ChunksCacheSize](https://developers.eventstore.com/server/v24.10/configuration/db-config.html#chunk-cache)
* [StreamInfoCacheCapacity](https://developers.eventstore.com/server/v24.10/configuration/#streaminfocachecapacity)
* [EnableExternalTcp](https://developers.eventstore.com/server/v24.10/configuration/networking.html#external-tcp)
* Timeout settings

</box>


---

<!-- _class: section-divider -->
<!-- _header: '![logo](../themes/media/eventstore-white.png)' -->
<!-- _footer: 
 -->
![bg](../themes/media/section-divider-green.png)


# Lab: Install EventStoreDB


## See the labs folder on the desktop


---

<!-- _class: title-body -->
# Lab: Install EventstoreDB


<box>

Please open
`lab_install_esdb`
in your Labs folder.


<br>

Lab Summary: 

1. Un-archive a pre downloaded binary

2. Append an event using the Webui


</box>


---

<!-- _class: cover -->
<!-- _paginate: false -->
<!-- _header: 
 -->
<!-- _footer: '![eventstore](../themes/media/eventstore-inverse.png)' --> 

![bg](../themes/media/background-darkblue.png) 

# Truncating, Deleting, and Configuring Streams

## 

---

<!-- _class: title-body -->
# Configuration Options


<box>

**Streams can be configured to:**
* Only return x number of events by setting <b>$maxCount</b>
* Only return the most recent events by setting <b>$maxAge</b>
<br> 

It is important to note that events will persist in the $all stream until a scavenge operation rewrites the log. Scavenge is covered later in the course. 
<br>

**Streams can be Deleted**
* [Soft Delete](https://developers.eventstore.com/clients/grpc/delete-stream.html#soft-delete): Truncates the stream allowing future event appends to that stream
* [Hard Delete](https://developers.eventstore.com/clients/grpc/delete-stream.html#hard-delete) ("Tombstone"): Permanently removes a stream and its events. When a stream is hard deleted, you cannot reuse the stream name, it will raise an exception if you try to append to it again. 

</box>


---

<!-- _class: title-body -->
# Stream Configuration Internals


<box>

Streams are configured by appending an event to the `$$<your stream name>` system stream
* \$\$ streams are hard coded to return only a single event
* JSON formatted
* JSON elements used by the system include
    * $maxAge
    * $maxCount
    * Access Control Configuration

</box>


---


<!-- _class: cover -->
<!-- _paginate: false -->
<!-- _header: 
 -->
<!-- _footer: '![eventstore](../themes/media/eventstore-inverse.png)' --> 

![bg](../themes/media/background-darkblue.png) 

# Subscriptions

##

---

<!-- _class: title-body -->
# Subscriptions


<box>

Clients can subscribe to a stream and receive newly appended events as they arrive.

Supported Features of subscriptions include:
* Subscribe to a named stream
* Subscribe to the $all stream
* Persistent Subscriptions
    * ESDB server tracks subscribers progress (manages state)
* Catch-up Subscriptions
    * Application tracks progress (manages state)

</box>


---

<!-- _class: cover -->
<!-- _paginate: false -->
<!-- _header: 
 -->
<!-- _footer: '![eventstore](../themes/media/eventstore-inverse.png)' --> 

![bg](../themes/media/background-darkblue.png) 

# Projections

##

---

<!-- _class: title-body -->
# Projections


<box>

EventStoreDB supports two types of projections:

* System Projections
* User Defined Projections


</box>


---

<!-- _class: title-body -->
# System Projections


<box>

EventStoreDB has a  projections subsystem that lets you append new events or link existing events to streams in a reactive manner. Projections require the event body to be in JSON.
<br/>
Available projections include:
* By Category ($by_category)
* By Event Type ($by_event_type)
* By Correlation ID ($by_correlation_id)
* Stream by Category ($stream_by_category)
* Streams ($streams)


</box>


---

<!-- _class: title-body -->
# Projection by Category ($by_category)


<box>


Events appended into following streams:
* usa-customer1
* usa-customer2
</br>
Would be projected into the stream:
* $ce-usa


</box>


---

<!-- _class: title-body -->
# Projection by Event Type ($by_event_type)


<box>


Events with the event type "SALE" appended into any stream  would be projected into the stream $et-SALE.

</box>


---

<!-- _class: title-body -->
# Projection by Correlation ID ($by_correlation_id)



<box>


Events sharing a $correlationID value "X" in the event metadata that are appended into any stream would be projected into the stream $bc-X.
</br>
The projection takes one parameter, a JSON string as a projection source:
</br>
```JSON
{
  "correlationIdProperty": "$myCorrelationId"
}
```



</box>


---

<!-- _class: title-body -->
# Projection Stream by Category ($by_category)


<box>


The [stream by category](https://developers.eventstore.com/server/v24.10/features/projections/system.html#stream-by-category) projection links existing events from streams to a new stream with a $category prefix by splitting a stream id by a configurable separator.
</br>
The separator as well as where to split the stream id are configurable.
</br>


</box>


---

<!-- _class: title-body -->
# Streams Projection ($streams)


<box>


This projection links existing events from streams to a stream named $streams. <i>This will contain all events in all streams.</i>

</box>


---

<!-- _class: title-body -->
# User-defined Projections


<box>

Just like an application can manage it’s own subscription by storing the offset, an application may read events or subscribe to streams and append new events or create new streams of events based upon logic applied to the events read. 

</box>


---

<!-- _class: title-body -->
# Projection API


<box>

A projections API is available for user defined projections that offers: 

* Custom projections
* Flexible JSON configuration
</br>

[See Documentation for additional information](https://developers.eventstore.com/server/v24.10/features/projections/custom.html#projections-api)


</box>

---

<!-- _class: title-body -->
# User Defined Projections 
<br>

<box-half-left>
<img src="./media/User_Projection.png" alt="projection" width="500" >
</box-half-left>
<box-half-right>
<img src="./media/User_Projection2.png" alt="ouro" width="500"  >
</box-half-right>



 ---

<!-- _class: title-body -->
# Projection Modes


<box>

* Continuous: Continues running after reaching the end of the stream. 
* Onetime: Runs until the end of the stream and stops. Can be re-run later.
* Query: Transient queries which will run until the end of the stream, write a result, and then be deleted after a period of time.


</box>
<!--Course will focus on continous projection mode.
-->

---

<!-- _class: title-body -->
# Projection Configurations


<box>

<b>EmitEnabled</b>: 
* Allows projection to write events<br>

<b>TrackEmittedStreams</b>: 
* Cleans up emitted streams when projection is deleted
* Causes write amplification (<i>use with care</i>)<br>

<b>MaxAllowedWritesInFlight</b>:
* Projection can write to multiple streams at the same time
* By default: 
    * Number of concurrent write requests is unbounded 
    * Projection writes as fast as possible
    * Use for fan out projections with write pressure on the node

        

</box>


---

<!-- _class: title-body -->

# Projection Configurations


<box>

<b>CheckpointAfterMs</b>
* Checkpoint stores the stream position up to where the projection processed
* Checkpoints are written periodically by projections
* The projection will pause and wait for its buffers to empty after a checkpoint is requested
* **Performance Tip:** Limit frequency of projection checkpoints using "CheckpointAfterMs"
    * <i>Especially if projection status is often in "CheckpointRequested"</i>


</box>


---

<!-- _class: title-body -->

# Projection Metadata



<box>

* Projections add metadata to each event they emit
<br>
* The metadata identifies:
    * The projection that emitted the event 
    * The event that caused the emit
<br>    
* The projection checks metadata of the previously emitted event before any further emit to ensure nothing else has been written to the stream. 
    * If metadata is missing or does not match, then the projection faults

</box>


---

<!-- _class: title-body -->
# Projection Status


<box>

* Checkpoint Requested
    * The projection has handled enough events and is ready to write a checkpoint.
    * New event processing is paused until the checkpoint is completed.
    * Checkpoint must be written before a projection can stop gracefully.
* Starting
    * The projection is starting and catching up from the previous checkpoint.
* Running
    * The projection is running normally.
* Stopping
    * The projection is stopping.
    * Includes writing a checkpoint and clearing state.

</box>


---

<!-- _class: title-body -->
# Projection Status


<box>


* Stopped
    * The projection is disabled. The projection must be enabled to restart.
* Faulted
    * The projection experienced an error. A status message should describe the failure.

</box>


---

<!-- _class: title-body -->
# Projection Pitfalls


<box>

**Write amplification**

* Projections write events for:
    * Emitted events
    * LinkTo events
    * State and result updates
    * Checkpoints
    * Configuration changes
<br/>
* Write amplification must be condisdered when estimating disk space.
    * Be aware of infinite loop where a projection feeds into another projection that feeds the original projection. 
    * Some projected system streams have maxCount set to combat write amplification   
    * Scavenge regularly

</box>


---

<!-- _class: title-body -->
# Projection Pitfalls


<box>

**Projections only run on Leader**

* This puts extra pressure on the leader node.<br/>

**Projections are not real-time**
* Delay between an event being appended and the projection emit.
* If this not acceptable, using subscriptions is an alternative.</br>

**ProjectionThreads Config**
* This is the number of threads shared among all projections.
* If there are fewer threads than projections, the projections may run on same thread.
* Slow projection may impact a faster projection if they share the same thread.


</box>


---

<!-- _class: title-body -->
# Projection Configuration


<box>

* **Dev:** dev mode enables and starts system projections by default.
* **RunProjections=System:** Enables system projections only
* **RunProjections=All:** Enables both system projections and user projections.
* **StartStandardProjections:** Starts system projections



</box>




---


<!-- _class: title-body -->
# Questions?


<box>

Please take this time to ask any questions you may have. 

</box>


---

<!-- _class: section-divider -->
<!-- _header: '![logo](../themes/media/eventstore-white.png)' -->
<!-- _footer: 
 -->
![bg](../themes/media/section-divider-green.png)


# Lab: Exploring the Projection Engine


## 

---

<!-- _class: title-body -->
# Lab Summary


<box>

In this lab you will use the webui and:
1. Verify the projection engine is running
2. Start projections if needed
3. Append events that will demonstrate the behavior of the enabled projections



Please open
`lab_exploring_the_projection_engine.pdf`
in your Labs folder


</box>


---

<!-- _class: cover -->
<!-- _paginate: false -->
<!-- _header: 
 -->
<!-- _footer: '![eventstore](../themes/media/eventstore-inverse.png)' --> 

![bg](../themes/media/background-darkblue.png) 

# Internals

## 


---

<!-- _class: title-body -->
# Storage on Disk


<box>
Database Disk Files

* Transaction Log
* Indexes
* Scavenge Data

</box>



---

<!-- _class: title-body -->

# EventstoreDB Disk Use

<box-half-left> 

<img src="./media/ESDB_on_disk.png" alt="dashboad" width="500" >

</box-half-left>


<box-half-right> 

**Transaction Log**

**Physically**
Logical log split up into physical chunk files.
Up to 256 MiB of logical log per physical chunk.
With a header and footer in addition.
With a checkpoint: The Writer Checkpoint to know where the end of the log is. (explain)
All chunks are immutable (read only) except the last chunk, which is append only (also can be read).
(Demo)



</box-half-right>
<!--
This content is VERY similar to content in day2
Sort that out !!
-->

---



<!-- _class: title-body -->

# Data Directory

<box>
<img src="./media/Data_directory.png" alt="dashboad" width="1000" >
</box>




---

<!-- _class: title-body -->

# EventstoreDB Disk Use

<box-half-left> 

<img src="./media/ESDB_on_disk.png" alt="dashboad" width="500" >

</box-half-left>


<box-half-right> 

**Transaction Log**

* Not to be confused with Log Files
    * The log files contain the info/debug/error messages of the running database
    * The Transaction Log contains the actual data stored in the database.

**Logically, the transaction log is**

* Append only log containing up to 8,000 petabytes of data.
* THE SOURCE OF TRUTH for the database
    * The index and scavenge info is derived from this and can be regenerated.



</box-half-right>


---

<!-- _class: title-body -->

# Transaction Log

<box-half-left> 

**Physically**

* Logical log split up into physical chunk files.
* Up to 256 MiB of logical log per physical chunk.
* With a header and footer in addition.
* With a checkpoint: The Writer Checkpoint to know where the end of the log is. (explain)
* All chunks are immutable (read only) except the last chunk, which is append only (also can be read).
(Demo)


</box-half-left>


<box-half-right> 

<img src="./media/ESDB_on_disk.png" alt="dashboad" width="500" >


</box-half-right>


---

<!-- _class: title-body -->
# Chunk Naming (no scavenge)

<box-half-left>

**chunk-XXXXXX.YYYYYY**

* X is the chunk number.
* Y is zero
* Scavenging will make this more complicated

</box-half-left>

<box-half-right>
<img src="./media/Chunk_no_scavenge.png" alt="dashboad" width="200" >


</box-half-right>



---

<!-- _class: title-body -->
# Index


<box>

**Purpose: Finding Events in a Stream.**
<br/>

**Two main components:**

* Mem Tables (In-memory tables)
* PTables (Persisted tables)

**Immutable files**

* Inside a PTable: one entry per event, entries grouped by stream.
* PTables are merged together, forming a log-structured-merge tree.



</box>


---

<!-- _class: title-body -->
# Index Map File


<box>

* Immutable (meaning the whole file is replaced with a new file, not edited)
* Text format, not quite human readable
* Contains a list of the PTables and a checkpoint.
* When a new PTable is written, a new Index map file is created.
* When taking a backup there needs to be consistency between the PTables present, and the PTables the map file lists.

</box>


---

<!-- _class: title-body -->
# PTable Internals




<box>

**Each PTable entry is a triple of Int64s:**

* Hash of the StreamName
* The number of the event in the stream
* Position of the event in the logical transaction log.

</box>


---

<!-- _class: title-body -->
# Index 



<box>

**PTable Bloom Filters**

* Immutable files
* One for each PTable
* Describes what is in the PTable so it is not accessed unnecessarily
* Only a performance optimisation, not necessary for correct operation.

**Stream Existence Filter**

* This is a Bloom Filter for the whole of the index.
* Facilitates faster stream creation.
* MUTABLE data file.
* Checkpoint (order of backup rule applies here)

</box>

--- 

<!-- _class: title-body -->

# Scavenge


<box>

**scavenge.db**

* An sqlite database containing accumulated data to make scavenging faster.
* Checkpoint is stored in the db.
* More on scavenge in later section.

</box>


---

<!-- _class: section-divider -->
<!-- _header: '![logo](../themes/media/eventstore-white.png)' -->
<!-- _footer: 
 -->
![bg](../themes/media/section-divider-green.png)


# Lab: Files Used by EventStoreDB


##


---

<!-- _class: title-body -->
# Lab Summary


<box>

In this lab you will:
1. Locate the Data and Logs directory
2. Delete the Data directory and restart
3. View the log files

Please open

`lab_exploring_the_projection_engine.pdf`

in your Labs folder.

</box>


---

<!-- _class: cover -->
<!-- _paginate: false -->
<!-- _header: 
 -->
<!-- _footer: '![eventstore](../themes/media/eventstore-inverse.png)' --> 

![bg](../themes/media/background-darkblue.png) 

# Write Path

## 

---

<!-- _class: title-body -->
# Cluster Review



<box>

* Typically a 3 Node Cluster
* Leader
    * Responsible for writes
    * Write replication
    * Write Acknowledgement to Client
* Follower
    * Replicates Write from Reader
* Read Only Replica
    * Is not part of the cluster
    * Does not participate in quorum activities
    * Leader Elections
    * Accepting writes
    * Simply Replicates writes from the leader
    * For serving reads
    * For a kind of continuous backup


<!-- All of this needs to be spit out
into single node and multi node
Leaving for now -->

</box>


---

<!-- _class: title-body -->
# Cluster Write
<box-half-left>

**Connectivity**

* All nodes connect to each other on port 2113 for Gossip and Elections. gRPC is used.

* All nodes connect to the leader node on port 1112 for Log Replication. TCP is used directly.

</box-half-left>
<box-half-right>
<img src="./media/3node_cluster_commication_during_write.png" alt="ouro" width="400" >
</box-half-right>



---

<!-- _class: title-body -->
# Stages of a Write


<box>

1. Leader receives a write request.
2. Leader writes to its own copy of the transaction log (details on another slide).
3. The write is replicated to the other nodes.
4. The data is safe when on the majority of cluster nodes.
5. The write is indexed on the leader (in-memory operation, even if it causes a new PTable to be created).

</box>


---

<!-- _class: title-body -->
# Stages of a Write


<box>

6. Now the write can be read from leader.
7. The write is acknowledged as successful to the Client by the leader.
8. Now the client knows the write was successful. The write is complete as far as the client is concerned.
9. The followers/RoR become aware that the write was successful and they index it too.
10. Now the write can be read from the followers/RoR.

</box>


---

<!-- _class: title-body -->
# <!-- _class: title-body -->
# Write Path in three slides


<box-half-left>

<img src="./media/write_to_leader.png" alt="projection" width="500" >

</box-half-left>

<box-half-right>

**Local to Leader**
* gRPC service
    * Authentication (who is this user)
    * Authorization (are they allowed to write to this stream)
    * Puts a WriteEvents message on the Main Queue



</box-half-right>



---

 <!-- _class: title-body -->
# <!-- _class: title-body -->
# Write Path

<box-half-left>
<img src="./media/write_to_leader.png" alt="projection" width="500" >
</box-half-left>

<box-half-right>

**Local to Leader**
* MainStage
    * Is the Node in a fit state to service writes
    * IsLeaderRequired
    * Via the Request Management Service, puts the write on the writer queue



</box-half-right>

<!-- For the bullet "IsLeaderRequred", here is how it works:  If a follower is processing a write, it checks the RequiresLeader flag on the request. If the request requires leader, the follower will reject it (because it is not the leader). If the request does not require leader then the follower can continue to process it, by forwarding it to the leader. -->

---

<!-- _class: title-body -->
# <!-- _class: title-body -->
# Write Path



<box-half-left>

<img src="./media/write_to_leader.png" alt="projection" width="500" >

</box-half-left>
<box-half-right>

**Local to Leader**

* Writer
    * Checks if the request has been cancelled
    * Idempotency check.
    * Look up last event number: Expected version check
* Number the events being written 
    * Append them to the active chunk

</box-half-right>



---

<!-- _class: title-body -->
# Write Path: Append to Active Chunk
<box-half-left>

* Appended to the active Chunk at the Writer Checkpoint
* Occasionally flush to disk (every ~2ms when under load)
    * Chunk file is flushed to disk
    * Writer checkpoint is flushed to disk

* Flushing in this order guarantees that the Writer Checkpoint is always valid even under power-loss.

</box-half-left>
<box-half-right>
<img src="./media/write_to_log.png" alt="ouro" width="400"  >
</box-half-right>



---

 <!-- _class: title-body -->

 # Write Path: Replicate the Write (part 1)
 
 <box-half-left>
 <img src="./media/replicate_the_write.png" alt="replicate" width="500" >
 </box-half-left>
<box-half-right>

* The data is sent to the other nodes.
* Cluster + ROR
* Results in an identical copy of the log.
* No need for looking up the last event number etc, it’s all baked into the data now.
* Chunk still flushed to disk before writer checkpoint.
* The nodes respond when they have the data.


 
 </box-half-right>
 
 
 
---

<!-- _class: title-body -->

# Write Path: Replicate the Write (part 2)
 
<box-half-left>
<img src="./media/replicate_the_write.png" alt="replicate" width="500" >
</box-half-left>
<box-half-right>


* Leader considers the data safe when the majority of cluster nodes have replicated the log up to that point.
* Read Only Replica does not count towards the majority.
* On a three node cluster the data needs to be replicated to one other node.

 
</box-half-right>
 
 
 
---

<!-- _class: title-body -->
# Write Path: Replication Failure



<box>

* What if the leader wrote a write but cannot replicate it?
* The write times out.
* The data was was written locally is guaranteed to eventually either be accepted by the cluster, or removed in an offline truncation operation
* The copies of the Transaction Log on each node do not permanently diverge from each other.


(Demo)

</box>


---

<!-- _class: cover -->
<!-- _paginate: false -->
<!-- _header: 
 -->
<!-- _footer: '![eventstore](../themes/media/eventstore-inverse.png)' --> 

![bg](../themes/media/background-darkblue.png) 

# Read Path

## 

---

<!-- _class: title-body -->
# Read Path: $all Reads (part 1)
<box-half-left>

* gRPC service
* Authentication (who is this user)
* Authorization (are they allowed to read $all)
* Breaks up the read into small reads (32 events)
* MainStage
* Is the Node in a fit state to service reads
* IsLeaderRequired
* Distributes the read to one of the reader queues

</box-half-left>
<box-half-right>
<img src="./media/read_path_all_reads.png" alt="ouro" width="500"  >
</box-half-right>



---

<!-- _class: title-body -->

# Read Path: $all Reads (part 2)

<box-half-left>


* Reader Worker
* Checks if the request has expired
* Reads the events out of the chunk (they are just there in a row)
* The index is not used, but the results are limited to what has been indexed.

</box-half-left>
<box-half-right>
<img src="./media/read_path_all_reads.png" alt="ouro" width="500"  >
</box-half-right>



---
 
<!-- _class: title-body -->
# Read Path: Streams (part 1)


<box>

gRPC service
* Same as for $all read
* Authentication (who is this user)
* Authorization (are they allowed to read $all)
* Breaks up the read into small reads (32 events)
MainStage
* Same as for $all read
* Is the Node in a fit state to service reads
* IsLeaderRequired
* Distributes the read to one of the reader queues

</box>


---

<!-- _class: title-body -->
# Read Path: Streams (part 2)


<box>


Reader Worker
* Checks if the request has expired
* Finds the event addresses in the index (the stream may be scattered throughout the chunks)
* Loads the events from the chunks by address
* Looks up and applies Metadata, Tombstone

</box>


---

<!-- _class: title-body -->
# Read Path: Streams


<box>
<img src="./media/read_path_streams.png" alt="projection" width="500" >
</box>


---

<!-- _class: title-body -->
# Read Path: Potential Issues


<box>

* Incorrect credentials
* Not authorized
* Stream does not exist
* Leader was required but node was not leader
* Request was queued so long it expired
* $all position was not valid

</box>

---

<!-- _class: cover -->
<!-- _paginate: false -->
<!-- _header: 
 -->
<!-- _footer: '![eventstore](../themes/media/eventstore-inverse.png)' --> 

![bg](../themes/media/background-darkblue.png) 

# System Streams 

## 

---

<!-- _class: title-body -->
# System Streams Overview


<box>

EventStoreDB uses Streams internally to manage permissions and configuration settings. 

System Streams: 
* Start with "$"
* May be automatically generated or user generated
* Can be modified by the server automatically
* Can be modified by the user


</box>


---

<!-- _class: title-body -->
# System Streams Demo


<box>

In this demo the instructor will show the system streams used to store settings for the projection engine. 

<br>

Rquirements:
* A running EventStoreDB cluster
* Access to the webui for that cluster

</box>


---



<!-- _class: title-body -->
# Using the Stream Browser to View System Streams
<box-half-left>

This screenshot is from a freshly started cluster. A long running cluster will have additional streams. 

</box-half-left>
<box-half-right>
<img src="./media/webui_system_streams.png" alt="webui" width="600"  >
</box-half-right>



---

<!-- _class: title-body -->

# Changing Projections Setting

<box-half-left>

* Using the webui the instructor will change a projection setting from running, to disabled. 
* The instructor will then view the system stream for that projection.
* Each setting change will be an event in the associated system stream

</box-half-left>
<box-half-right>
<img src="./media/webui_system_streams.png" alt="webui" width="600"  >
</box-half-right>



---

<!-- _class: title-body -->

# Disable/Enable Projections

<box>

<img src="./media/webui_system_streams2.png" alt="projection" width="1000" >

</box>



---

 <!-- _class: title-body -->
# View Stream Browser
<box>

View of the ```$projections-$by_category```  after a few Enable/Disable changes. 
<br/>

<img src="./media/webui_system_streams3.png" alt="projection" width="1000" >

</box>



---

<!-- _class: title-body -->
# System Streams Review
 
 
<box>

 Note that the configuration settings for enable/disable of system projections is managed by system streams. 

A change from enabled to disabled of the by_category projection creates:
* An event of type ```$ProjectionUpdated```
* Appended to the stream ```$projections-$by_category```
* The event has a JSON payload of details
 


</box>
 
 
 
---



<!-- _class: cover -->
<!-- _paginate: false -->
<!-- _header: 
 -->
<!-- _footer: '![eventstore](../themes/media/eventstore-inverse.png)' --> 

![bg](../themes/media/background-darkblue.png) 

# Stream Access Control 

## 

---

<!-- _class: title-body -->
# Stream Access Control


<box>

* Stream metadata is stored in a separate stream
* Stream name="mystream"
* Metadata stream = "$$mystream"
* $maxCount = 1
    * Only one event in the stream
* JSON format containing:
    * ACL's
    * $maxAge
    * $maxCount


</box>


---

<!-- _class: title-body -->
# Stream Metadata Demo


<box>

The instructor will demonstrate using the webui. 

1. Using the webui create a stream by appending an event.
2. The instructor will show the stream for the event.
3. Use the "Edit ACL" button to change stream permissions
4. Note the creation of the "$$" stream to manage permissions

</box>


---

<!-- _class: section-divider -->
<!-- _header: '![logo](../themes/media/eventstore-white.png)' -->
<!-- _footer: 
 -->
![bg](../themes/media/section-divider-green.png)


# Lab: Modify Acccess Control List for a Stream

##


---

<!-- _class: title-body -->
# Lab Summary


<box>

This lab can be run using github codespaces. 

<br>

This lab has the following steps:
1. Start a secure cluster
2. Use http api requests to create a $$ metadata stream with ACL
3. Use http api to create a user
3. Append to the stream as authorized user
4. Attempt to append as a non-authorized user

Please open 
`lab_modify_acl_for_stream.pdf`
in your Labs folder.

</box>

---

<!-- _class: title-body -->
# Congratulations


<box>

**You know know how to:**


<box>

* Differentiate the unique functionality of EventStoreDB from other systems
* Install EventStoreDB from a binary distribution
* Add events to EventStoreDB streams
* Configure stream settings to delete old events
* Use the EventStorDB webui
</box>

</box>


---
