---
theme: ./kurrent_2025
fonts:
  # basically the text
  sans: Work Sans
  # use with `font-serif` css class from UnoCSS
  serif: Robot Slab
  # for code blocks, inline code, etc.
  mono: Fira Code
layout: cover
---

# KurrentDB 
# Foundations


---
layout: main-full
---

# Table of Contents:

1. KurrentDB Overview
2. KurrentDB comparison to other systems



---
layout: two-cols-header
---

# Outline

::left::

* KurrentDB overview
* KurrentDB comparison to other DBs 
* Introduction to events and streams
* Concurrency
* KurrentDB internals 
* Events
* Reading streams
* Database configuration
* Lab: Install KurrentDB
* Truncate, delete, and configure streams
* Subscriptions
* Projections:  System & User Defined


::right::
* Lab: Exploring the Projection Engine
* KurrentDB internals:  Storage on Disk
* Lab: Files used by KurrentDB
* Truncate, delete, and configure streams
* Subscriptions
* Projections:  System & User Defined
* Lab: Exploring the Projection Engine
* KurrentDB internals:  Storage on Disk
* Lab: Files used by KurrentDB
* Write path

---
layout: main-full
---

# Outline

* Read path
* System streams
* Stream access control
* Lab: Modify stream access control List
* Lab (optional): Stress test the server 

---
src: ./pages/overview.md 
---

# INCLUDE POINTER TO OVERVIEW MODULE
# THIS IS NOT DISPLAYED



---
src: ./pages/comparison.md 
---

# INCLUDE POINTER TO COMPARISON MODULE
# THIS IS NOT DISPLAYED


---
src: ./pages/events.md 
---

# INCLUDE POINTER TO EVENTS MODULE
# THIS IS NOT DISPLAYED


---
src: ./pages/streams.md 
---

# INCLUDE POINTER TO EVENTS MODULE
# THIS IS NOT DISPLAYED

---
src: ./pages/stream_details.md 
---

# INCLUDE POINTER TO stream_details MODULE
# THIS IS NOT DISPLAYED

This content is the images of the all stream, 
and the stream index


---
src: ./pages/concurrency.md 
---

# INCLUDE POINTER TO stream_details MODULE
# THIS IS NOT DISPLAYED

This content is the images of the all stream, 
and the stream index


---
layout: section
---

# BREAK FROM SECTIONIZED CONTENT

# TO COMBINED CONTENT


---
layout: main-full
---

# Maybe make the next topic "stream metadata"



---
layout: cover
---

# Deleting Events

Stream Configuration

---
layout: main-full
---

# Event Removal Triggers

* Stream Deletion
    * Hard
    * Soft
* Stream Configuration
    * MaxAge
    * MaxCount    


---
layout: main-full
---

# Stream Configuration


Each stream has an optional metadata stream for configuration

\$$<Stream_Name>

Commonly used stream settings:

* **maxAge**
    * Older events are deleted  

* **maxCount**
    * Events are deleted that violate maxCount

* **ACL**
    * Access Control List


---
layout: section
---

# KurrentDB Internals

---
layout: main-full
---

# KurrentDB Internals: Event Management


* KurrentDB is a sequenced log of events
* As events are written, they are appended to a global log
* The global log contains all user and system generated events
* The global log can be read as the $all stream
* Events are stored in consistent order
* Events have a permanent sequence number
* LSM(Log Structured Merge Tree) structure 



---
layout: main-full
---

# KurrentDB Optimizations

**General Considerations**

* Durability (Crash tolerance)
* Disk access patterns
    * Sequential reads
    * Random seeks 

<!-- 
Instructor should be able to describe the general aspects of these terms  

The main point is that the append only log is sequential write, and the structure of a stream is more or less sequential-ish reads. 

The LSM structure was designed for these issues
-->

---
layout: main-full
---

# KurrentDB Optimizations

KurrentDB has the following design features: 

* Pre-allocated append-only log that enables high throughput and sequential writes 
* Log-structured merge-tree(LSM) for high write capacity for the additional data storage (stream indexes)


<!-- The pre-allocated log avoids fragmentation, favoring sequential reads 
* It is beyond the scope of this course to go into details of LSM’s, but RocksDB is a widely used system, that also makes use of LSM’s https://rocksdb.org/
* And this site is useful, https://disc-projects.bu.edu/compactionary/index.html, and this animation is great https://disc-projects.bu.edu/compactionary/research.html -->


---
layout: main-full
---

# Deleting Events

Event deletion occurs when:

* Event is older than $maxAge stream setting
* Event violates $maxCount stream setting
* The stream itself is deleted


---
layout: section
---

# Reading Streams

---
layout: main-full
---

# Reading Streams

The following options are availalbe when reading a stream:

* Read forward 
* Read backward
* Read n number of events
* Start reading from any position in the stream

---
layout: main-full
---

# Reading streams: example code

Starting from a particular location, reading backwards, limit 100 events

```
events = client.get_stream(
    stream_name="demo",
    stream_position=2,
    limit=100,
    backwards=True
)


```

---
layout: main-full
---

# Reading the $all stream

When reading from the $all stream, you must provide byteoffset of the event instead of event number


```python
event_all = client.read_all(commit_position=955159)

for event in event_all:
     # Doing something productive with the event
     print(f"Event: {event}")

```

---
layout: section
---

# Database Configuration 

---
layout: main-full
---

# Configuration Sources

* Configuration file
* Command line
* Environment variables


---
layout: main-full
---

# Configuration Precedence

1 - Command line options
2 - Environment variables
3 - Configuration files (YAML and JSON)


This order of precedence allows for flexible configuration management, where you can set default values in configuration files, override them with environment variables if needed, and use command line options for the highest priority settings.



---
layout: main-full
---

# Common Configuration Options



* [**ClusterSize**](https://developers.eventstore.com/server/v24.10/configuration/cluster.html#cluster-size):  Number of nodes in the cluster (excludes read-only replicas)
* [**DiscoverViaDns**](https://developers.eventstore.com/server/v24.10/configuration/cluster.html#cluster-with-dns): Whether to enable DNS discovery
* [**GossipSeed**](https://developers.eventstore.com/server/v24.10/configuration/cluster.html#cluster-with-gossip-seeds): A list of hosts to gossip to (when DNS discovery is disabled)
* [**ClusterDns**](https://developers.eventstore.com/server/v24.10/configuration/cluster.html#cluster-with-dns): The DNS discovery endpoint (when DNS discovery is enabled)


---
layout: main-full
---

# Common Configuration Options

**IP / Hostname settings**

* [**ReplicationIp**](https://developers.eventstore.com/server/v24.10/configuration/networking.html#interface-and-port) (formerly IntIp): IP address to bind to for internal node-to-node communication
* [**NodeIp**](https://developers.eventstore.com/server/v24.10/configuration/networking.html#http-configuration) (formerly ExtIp): IP address to bind to for node-to-node and node-to-client communication
    * *ReplicationIp and NodeIp will be the same if you are using a single network interface (which is true for most configurations)*
* **NodeHostAdvertiseAs** (previously ExtHostAdvertiseAs): The hostname to advertise the node as on the gossip endpoint. This is usually changed to the node’s hostname when you are using certificates to prevent certificate name mismatches.
* **AdvertiseHostToClientAs**: The hostname to advertise the node as on the client gossip endpoint. This is usually used when clients are connecting behind a NAT or set to match the node’s hostname when using certificates.


---
layout: main-full
---

# Common Configuration Options


* [**Log rotation**](https://developers.eventstore.com/server/v24.6/diagnostics/logs.html#log-file-interval) (LogFileSize, LogFileInterval, LogFileRetentionCount)
* [**ReaderThreadsCount**](https://developers.eventstore.com/server/v24.10/configuration/#readerthreadscount)
    * Can be increased if reader threads are saturated
* **Projection settings**
    * RunProjections - whether to start the projection subsystem
    * StartStandardProjections - whether to start the built-in system projections


---
layout: main-full
---

# Commonly used configuration options


* [SkipIndexVerify](https://developers.eventstore.com/server/v24.10/configuration/indexes.html#skip-index-verification)
* Certificate settings 
* [CachedChunks / ChunksCacheSize](https://developers.eventstore.com/server/v24.10/configuration/db-config.html#chunk-cache)
* [StreamInfoCacheCapacity](https://developers.eventstore.com/server/v24.10/configuration/#streaminfocachecapacity)
* [EnableExternalTcp](https://developers.eventstore.com/server/v24.10/configuration/networking.html#external-tcp)
* Timeout settings

---
layout: main-full
---


# Lab: Install KurrentDB


## See the labs folder on the desktop

---
layout: lab
---

# Lab: Install KurrentDB

Please open
"lab_install_esdb"
in your Labs folder.


Lab Summary: 

1. Un-archive a pre downloaded binary

2. Append an event using the Webui


---
layout: intro
---

# Stream Metadata

 

---
layout: main-full
---

# Configuration Options

**Streams can be configured to:**
* Only return x number of events by setting $maxCount
* Only return the most recent events by setting $maxAge
 
It is important to note that events will persist in the $all stream until a scavenge operation rewrites the log. Scavenge is covered later in the course. 

**Streams can be Deleted**
* [Soft Delete](https://developers.eventstore.com/clients/grpc/delete-stream.html#soft-delete): Truncates the stream allowing future event appends to that stream
* [Hard Delete](https://developers.eventstore.com/clients/grpc/delete-stream.html#hard-delete) ("Tombstone"): Permanently removes a stream and its events. When a stream is hard deleted, you cannot reuse the stream name, it will raise an exception if you try to append to it again. 

---
layout: main-full
---

# Stream Configuration Internals

Streams are configured by appending an event to the `$$` system stream
* \$\$ streams are hard coded to return only a single event
* JSON formatted
* JSON elements used by the system include
    * $maxAge
    * $maxCount
    * Access Control Configuration

---
layout: intro
---

# Subscriptions

##

---
layout: main-full
---

# Subscriptions

Clients can subscribe to a stream and receive newly appended events as they arrive.

Supported Features of subscriptions include:
* Subscribe to a named stream
* Subscribe to the $all stream
* Persistent Subscriptions
    * ESDB server tracks subscribers progress (manages state)
* Catch-up Subscriptions
    * Application tracks progress (manages state)


---
layout: intro
---

# Projections

##

---
layout: main-full
---

# Projections

KurrentDB supports two types of projections:

* System Projections
* User Defined Projections

---
layout: main-full
---

# System Projections

KurrentDB has a  projections subsystem that lets you append new events or link existing events to streams in a reactive manner. Projections require the event body to be in JSON.

Available projections include:
* By Category ($by_category)
* By Event Type ($by_event_type)
* By Correlation ID ($by_correlation_id)
* Stream by Category ($stream_by_category)
* Streams ($streams)

---
layout: main-full
---

# Projection by Category ($by_category)

Events appended into following streams:
* usa-customer1
* usa-customer2

Would be projected into the stream:
* $ce-usa

---
layout: main-full
---

# Projection by Event Type ($by_event_type)


Events with the event type "SALE" appended into any stream  would be projected into the stream $et-SALE.


---
layout: main-full
---

# Projection by Correlation ID ($by_correlation_id)

Events sharing a $correlationID value "X" in the event metadata that are appended into any stream would be projected into the stream $bc-X.

The projection takes one parameter, a JSON string as a projection source:

```
{
  "correlationIdProperty": "$myCorrelationId"
}
```

---
layout: main-full
---

# Projection Stream by Category ($by_category)


The [stream by category](https://developers.eventstore.com/server/v24.10/features/projections/system.html#stream-by-category) projection links existing events from streams to a new stream with a $category prefix by splitting a stream id by a configurable separator.

The separator as well as where to split the stream id are configurable.


---
layout: main-full
---

# Streams Projection ($streams)

This projection links existing events from streams to a stream named $streams. This will contain all events in all streams.


---
layout: main-full
---

# User-defined Projections


Just like an application can manage it’s own subscription by storing the offset, an application may read events or subscribe to streams and append new events or create new streams of events based upon logic applied to the events read. 


---
layout: main-full
---

# Projection API

A projections API is available for user defined projections that offers: 

* Custom projections
* Flexible JSON configuration


[See Documentation for additional information](https://developers.eventstore.com/server/v24.10/features/projections/custom.html#projections-api)


---
layout: two-cols-header
---


# User Defined Projections 

::left::

<img src="./assets/User_Projection.png" alt="projection" width="400" >

::right::

<img src="./assets/User_Projection2.png" alt="ouro" width="400"  >


---
layout: main-full
---

# Projection Modes

* Continuous: Continues running after reaching the end of the stream. 
* Onetime: Runs until the end of the stream and stops. Can be re-run later.
* Query: Transient queries which will run until the end of the stream, write a result, and then be deleted after a period of time.


---
layout: main-full
---

# Projection Configurations

EmitEnabled: 
* Allows projection to write events

TrackEmittedStreams: 
* Cleans up emitted streams when projection is deleted
* Causes write amplification (use with care)

---
layout: main-full
---

# Projection Configurations

MaxAllowedWritesInFlight:
* Projection can write to multiple streams at the same time
* By default: 
    * Number of concurrent write requests is unbounded 
    * Projection writes as fast as possible
    * Use for fan out projections with write pressure on the node
        
---
layout: main-full
---

# Projection Configurations


CheckpointAfterMs
* Checkpoint stores the stream position up to where the projection processed
* Checkpoints are written periodically by projections
* The projection will pause and wait for its buffers to empty after a checkpoint is requested
* **Performance Tip:** Limit frequency of projection checkpoints using "CheckpointAfterMs"
    * Especially if projection status is often in "CheckpointRequested"


---
layout: main-full
---

# Projection Metadata


* Projections add metadata to each event they emit

* The metadata identifies:
    * The projection that emitted the event 
    * The event that caused the emit
    
* The projection checks metadata of the previously emitted event before any further emit to ensure nothing else has been written to the stream. 
    * If metadata is missing or does not match, then the projection faults


---
layout: main-full
---

# Projection Status


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

---
layout: main-full
---

# Projection Status

* Stopped
    * The projection is disabled. The projection must be enabled to restart.
* Faulted
    * The projection experienced an error. A status message should describe the failure.

---
layout: main-full
---

# Projection Pitfalls:

Write amplification

* Projections write events for:
    * Emitted events
    * LinkTo events
    * State and result updates
    * Checkpoints
    * Configuration changes

* Write amplification must be condisdered when estimating disk space.
    * Be aware of infinite loop where a projection feeds into another projection that feeds the original projection. 
    * Some projected system streams have maxCount set to combat write amplification   
    * Scavenge regularly


---
layout: main-full
---


# Projection Pitfalls


**Projections only run on Leader**

* This puts extra pressure on the leader node.

**Projections are not real-time**
* Delay between an event being appended and the projection emit.
* If this not acceptable, using subscriptions is an alternative.

**ProjectionThreads Config**
* This is the number of threads shared among all projections.
* If there are fewer threads than projections, the projections may run on same thread.
* Slow projection may impact a faster projection if they share the same thread.


---
layout: main-full
---


# Projection Configuration


* **Dev:** dev mode enables and starts system projections by default.
* **RunProjections=System:** Enables system projections only
* **RunProjections=All:** Enables both system projections and user projections.
* **StartStandardProjections:** Starts system projections

---
layout: main-full
---

# Questions?


Please take this time to ask any questions you may have. 


---
layout: lab
---



# Lab: Exploring the Projection Engine


## 

---
layout: main-full
---


# Lab Summary


In this lab you will use the webui and:
1. Verify the projection engine is running
2. Start projections if needed
3. Append events that will demonstrate the behavior of the enabled projections



Please open
`lab_exploring_the_projection_engine.pdf`
in your Labs folder


---
layout: intro
---


# Internals

## 


---
layout: main-full
---

# Storage on Disk

Database Disk Files

* Transaction Log
* Indexes
* Scavenge Data


---
layout: main-full
---


# KurrentDB Disk Use

 

**Transaction Log**

**Physically**
Logical log split up into physical chunk files.
Up to 256 MiB of logical log per physical chunk.
With a header and footer in addition.
With a checkpoint: The Writer Checkpoint to know where the end of the log is. (explain)
All chunks are immutable (read only) except the last chunk, which is append only (also can be read).
(Demo)


---
layout: center
---

<img src="./assets/ESDB_on_disk.png" alt="dashboad" width="500" >


---
layout: main-full
---

# Data Directory


---
layout: center
---

# Data Directory

<img src="./assets/Data_directory.png" alt="dashboad" width="1000" >


---
layout: main-full
---

# KurrentDB Disk Use



**Transaction Log**

* Not to be confused with Log Files
    * The log files contain the info/debug/error messages of the running database
    * The Transaction Log contains the actual data stored in the database.

**Logically, the transaction log is**

* Append only log containing up to 8,000 petabytes of data.
* THE SOURCE OF TRUTH for the database
    * The index and scavenge info is derived from this and can be regenerated.


---
layout: main-full
---


# Transaction Log

**Physically**

* Logical log split up into physical chunk files.
* Up to 256 MiB of logical log per physical chunk.
* With a header and footer in addition.
* With a checkpoint: The Writer Checkpoint to know where the end of the log is. (explain)
* All chunks are immutable (read only) except the last chunk, which is append only (also can be read).
(Demo)


---
layout: two-cols
---

# Chunk Naming (no scavenge)


**chunk-XXXXXX.YYYYYY**

* X is the chunk number.
* Y is zero
* Scavenging will make this more complicated

::right::

<img src="./assets/Chunk_no_scavenge.png" alt="dashboad" width="200" >

---
layout: main-full
---


# Index


**Purpose: Finding Events in a Stream.**


**Two main components:**

* Mem Tables (In-memory tables)
* PTables (Persisted tables)

**Immutable files**

* Inside a PTable: one entry per event, entries grouped by stream.
* PTables are merged together, forming a log-structured-merge tree.




---
layout: main-full
---


# Index Map File



* Immutable (meaning the whole file is replaced with a new file, not edited)
* Text format, not quite human readable
* Contains a list of the PTables and a checkpoint.
* When a new PTable is written, a new Index map file is created.
* When taking a backup there needs to be consistency between the PTables present, and the PTables the map file lists.



---
layout: main-full
---


# PTable Internals



**Each PTable entry is a triple of Int64s:**

* Hash of the StreamName
* The number of the event in the stream
* Position of the event in the logical transaction log.



---
layout: main-full
---


# Index 


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



---
layout: main-full
--- 

# Scavenge


**scavenge.db**

* An sqlite database containing accumulated data to make scavenging faster.
* Checkpoint is stored in the db.
* More on scavenge in later section.


---
layout: lab
---


# Lab: Files Used by KurrentDB


##


---
layout: main-full
---


# Lab Summary




In this lab you will:
1. Locate the Data and Logs directory
2. Delete the Data directory and restart
3. View the log files

Please open

`lab_exploring_the_projection_engine.pdf`

in your Labs folder.




---
layout: intro
---


# Write Path

## 

---
layout: main-full
---


# Cluster Review


* Typically a 3 Node Cluster
* Leader
    * Responsible for writes
    * Write replication
    * Write Acknowledgement to Client
* Follower
    * Replicates Write from Reader




<!-- All of this needs to be spit out
into single node and multi node
Leaving for now -->
---
layout: main-full
---

#  Read Only Replica

* Is not part of the cluster
* Does not participate in quorum activities
* Leader Elections
* Accepting writes
* Simply Replicates writes from the leader
* For serving reads
* For a kind of continuous backup

---
layout: two-cols
---


# Cluster Write


**Connectivity**

* All nodes connect to each other on port 2113 for Gossip and Elections. gRPC is used.

* All nodes connect to the leader node on port 1112 for Log Replication. TCP is used directly.

::right::

<img src="./assets/3node_cluster_commication_during_write.png" alt="ouro" width="300" >







---
layout: main-full
---


# Stages of a Write




1. Leader receives a write request.
2. Leader writes to its own copy of the transaction log (details on another slide).
3. The write is replicated to the other nodes.
4. The data is safe when on the majority of cluster nodes.
5. The write is indexed on the leader (in-memory operation, even if it causes a new PTable to be created).




---
layout: main-full
---


# Stages of a Write




6. Now the write can be read from leader.
7. The write is acknowledged as successful to the Client by the leader.
8. Now the client knows the write was successful. The write is complete as far as the client is concerned.
9. The followers/RoR become aware that the write was successful and they index it too.
10. Now the write can be read from the followers/RoR.




---
layout: main-full
---


# 
# Write Path in three slides





---
layout: center
---

<img src="./assets/write_to_leader.png" alt="projection" width="500" >




**Local to Leader**
* gRPC service
    * Authentication (who is this user)
    * Authorization (are they allowed to write to this stream)
    * Puts a WriteEvents message on the Main Queue







---
layout: main-full
---

 
# 
# Write Path







**Local to Leader**
* MainStage
    * Is the Node in a fit state to service writes
    * IsLeaderRequired
    * Via the Request Management Service, puts the write on the writer queue







---
layout: main-full
---


# 
# Write Path










**Local to Leader**

* Writer
    * Checks if the request has been cancelled
    * Idempotency check.
    * Look up last event number: Expected version check
* Number the events being written 
    * Append them to the active chunk





---
layout: main-full
---


# Write Path: Append to Active Chunk


* Appended to the active Chunk at the Writer Checkpoint
* Occasionally flush to disk (every ~2ms when under load)
    * Chunk file is flushed to disk
    * Writer checkpoint is flushed to disk

* Flushing in this order guarantees that the Writer Checkpoint is always valid even under power-loss.



---
layout: center
---

# Write to log

<img src="./assets/write_to_log.png" alt="ouro" width="400"  >




---
layout: main-full
---

 

 # Write Path: Replicate the Write (part 1)
 
 
 
 


* The data is sent to the other nodes.
* Cluster + ROR
* Results in an identical copy of the log.
* No need for looking up the last event number etc, it’s all baked into the data now.
* Chunk still flushed to disk before writer checkpoint.
* The nodes respond when they have the data.


 
---
layout: center
---

# Replicate the write
<img src="./assets/replicate_the_write.png" alt="replicate" width="500" >
 
 
 
---
layout: main-full
---



# Write Path: Replicate the Write (part 2)
 






* Leader considers the data safe when the majority of cluster nodes have replicated the log up to that point.
* Read Only Replica does not count towards the majority.
* On a three node cluster the data needs to be replicated to one other node.

 

 
 
 
---
layout: main-full
---


# Write Path: Replication Failure





* What if the leader wrote a write but cannot replicate it?
* The write times out.
* The data was was written locally is guaranteed to eventually either be accepted by the cluster, or removed in an offline truncation operation
* The copies of the Transaction Log on each node do not permanently diverge from each other.


(Demo)




---
layout: intro
---


# Read Path

## 

---
layout: two-cols
---


# Read Path: $all Reads (part 1)


* gRPC service
* Authentication (who is this user)
* Authorization (are they allowed to read $all)
* Breaks up the read into small reads (32 events)
* MainStage
* Is the Node in a fit state to service reads
* IsLeaderRequired
* Distributes the read to one of the reader queues

::right::

<img src="./assets/read_path_all_reads.png" alt="ouro" width="500"  >






---
layout: main-full
---



# Read Path: $all Reads (part 2)




* Reader Worker
* Checks if the request has expired
* Reads the events out of the chunk (they are just there in a row)
* The index is not used, but the results are limited to what has been indexed.








---
layout: main-full
---
 

# Read Path: Streams (part 1)




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

---
layout: center
---

# Stream Reads

<img src="./assets/read_path_streams.png" alt="projection" width="500" >


---
layout: main-full
---


# Read Path: Streams (part 2)





Reader Worker
* Checks if the request has expired
* Finds the event addresses in the index (the stream may be scattered throughout the chunks)
* Loads the events from the chunks by address
* Looks up and applies Metadata, Tombstone




---
layout: main-full
---


# Read Path: Streams







---
layout: main-full
---


# Read Path: Potential Issues




* Incorrect credentials
* Not authorized
* Stream does not exist
* Leader was required but node was not leader
* Request was queued so long it expired
* $all position was not valid



---
layout: intro
---

  

# System Streams 

## 

---
layout: two-cols
---


# System Streams Overview


KurrentDB uses Streams internally to manage permissions and configuration settings. 

System Streams: 
* Start with "$"
* May be automatically generated or user generated
* Can be modified by the server automatically
* Can be modified by the user

::right::

<img src="./assets/webui_system_streams.png" alt="webui" width="600"  >


---
layout: main-full
---


# System Streams Demo




In this demo the instructor will show the system streams used to store settings for the projection engine. 



Rquirements:
* A running KurrentDB cluster
* Access to the webui for that cluster




---
layout: main-full
---




# Using the Stream Browser to View System Streams


This screenshot is from a freshly started cluster. A long running cluster will have additional streams. 








---
layout: main-full
---



# Changing Projections Setting



* Using the webui the instructor will change a projection setting from running, to disabled. 
* The instructor will then view the system stream for that projection.
* Each setting change will be an event in the associated system stream








---
layout: center
---



# Disable/Enable Projections


<img src="./assets/webui_system_streams2.png" alt="projection" width="1000" >






---
layout: center
---

 
# View Stream Browser


View of the ```$projections-$by_category```  after a few Enable/Disable changes. 


<img src="./assets/webui_system_streams3.png" alt="projection" width="1000" >





---
layout: main-full
---


# System Streams Review
 
 


 Note that the configuration settings for enable/disable of system projections is managed by system streams. 

A change from enabled to disabled of the by_category projection creates:
* An event of type ```$ProjectionUpdated```
* Appended to the stream ```$projections-$by_category```
* The event has a JSON payload of details
 



 
 
 
---
layout: intro
---


# Stream Access Control 

## 

---
layout: main-full
---


# Stream Access Control




* Stream metadata is stored in a separate stream
* Stream name="mystream"
* Metadata stream = "$$mystream"
* $maxCount = 1
    * Only one event in the stream
* JSON format containing:
    * ACL's
    * $maxAge
    * $maxCount





---
layout: main-full
---


# Stream Metadata Demo


The instructor will demonstrate using the webui. 

1. Using the webui create a stream by appending an event.
2. The instructor will show the stream for the event.
3. Use the "Edit ACL" button to change stream permissions
4. Note the creation of the "$$" stream to manage permissions




---
layout: main-full
---



# Lab: Modify Acccess Control List for a Stream

##


---
layout: lab
---


# Lab Summary




This lab can be run using github codespaces. 



This lab has the following steps:
1. Start a secure cluster
2. Use http api requests to create a $$ metadata stream with ACL
3. Use http api to create a user
3. Append to the stream as authorized user
4. Attempt to append as a non-authorized user

Please open 
`lab_modify_acl_for_stream.pdf`
in your Labs folder.



---
layout: main-full
---

# Congratulations


**You know know how to:**



* Differentiate the unique functionality of KurrentDB from other systems
* Install KurrentDB from a binary distribution
* Add events to KurrentDB streams
* Configure stream settings to delete old events
* Use the EventStorDB webui


---
layout: section
---
# In this Section You Will Learn How To:

++++I ADDED BELOW+++

* Use the following tools 
    * Webui
    * es-cli
    * http-api
* Perform Basic Backup and Restore
* Leverage Projections
* Use Subscriptions 
* Run an EventStore based application   

---
layout: main-full
---

# Outline

* ESDB TOOLBOX
    * Webui
    * es-cli
    * http-api
* Lab webui
* Lab es-cli
* Lab http api
* Backup and Restore 
    * Storage on Disk
    * Backup Process
    * Lab Backup and Restore
* Projections  and Subscriptions

---
layout: section
---

# ESDB Toolbox

##

---
layout: main-full
---

# EventStoreDB Webui

* Built in to the server product
* Navigator
    * Currently under development replacement for Webui


---
layout: main-full
---

# Webui: Dashboard


**EventStoreDB is architected using a Staged Event Driven Architecture (SEDA)**

<!-- ADD BACK LATER
[SEDA definition](https://en.wikipedia.org/wiki/Staged_event-driven_architecture)
-->

The Webui Dashboard Tab Shows Internal Status:

* Main Queue
    * Read/Write requests start here
* Storage Reader Queue
    * Read Requests Handled here
* Storage Writer Queue
    * Write requests Handled here      



---
layout: main-full
---

# Webui Features: Dashboard


<img src="./assets/Dashboard_Annotated.png" alt="dashboard" width="800" >

---
layout: main-full
---

# Webui Features: Stream Browser


**The Stream Browser tab provides an interface to view and create events in Streams.**

With the Stream Browser tab you can:
* Create Events/Streams
* Read Events from Streams
* Set or view Stream Metadata
    * ACL's
    * maxAge
    * maxCount


---
layout: center
---
 
# Webui: Stream Browser

<img src="./assets/Stream_Browser_annotated.png" alt="dashboad" width="700" >


---
layout: main-full
---


# Stream Browser: Detail view



<img src="./assets/Stream_browser_detail.png" alt="dashboad" width="1000" >


---
layout: main-full
---

# Stream Browser: Event View

<img src="./assets/Stream_Browser_Event_view.png" alt="dashboad" width="1000" >


---
layout: main-full
---
 
# Stream Browser: Manage Metadata


<img src="./assets/Stream_Browser_metadata.png" alt="dashboad" width="1000" >


---
layout: main-full
---
 
# Stream Browser: Admin

<img src="./assets/Admin_annotated.png" alt="dashboard" width="700" >


---
layout: main-full
---

# Stream Browser: Projections

<img src="./assets/Projections_annotated.png" alt="dashboard" width="1000" >



---
layout: main-full
---

# Stream Browser: Visualize

<img src="./assets/Visualize_annotated.png" alt="dashboard" width="800" >


---
layout: main-full
---

# Webui: Persistent Subscriptions


<img src="./assets/Persistent_subscriptions_annotated.png" alt="dashboad" width="700" >


---
layout: section
---


# es-cli

## 

---
layout: main-full
---

# EventStoreDB es-cli


EventStoreDB provides a command line tool to interact with EventStoreDB. 

This section will describe how to use some of the most commonly used features of the EventStoreDB command line tool es-cli. 


---
layout: main-full
---


# es-cli


Command line tool providing ability to:
• Add users
• Shutdown server
• List users
<br/>

[See documentation for more info](https://developers.eventstore.com/commercial-tools/cli-tool.html#commands)


---
layout: main-full
---

# Authentication


Authentication credentials can be passed on the command line, or stored in a configuration file. 

**Command Line**

```
es-cli --serverurl="http://localhost:2113" 
     --username=admin --password=changeit
```

**Configuration File**

windows path: ```%AppData%/eventstore.rc```
linux/Mac path: ```~/.eventstorerc```




---
layout: main-full
--- 

# Configuration File Format


**Below is an example of the format of an example es-cli configuration file.**

```
serverurl="http://127.0.0.1:2113"
username="admin"
password="changeit"
output="json" # Or XML
verbose=true # Or false
```

---
layout: main-full
---

# Available es-cli Commands

Admin: 

```
scavenge, shutdown, merge_indexes,
calculate_stream_size, backup, restore, s3_backup,s3_restore, azure_backup, azure_restore,
verify_db, clear_scavenge_streams, delete_streams
```
<br/>
user:

```
add, change_password, delete, disable, update, enable, list, reset_password
```

---
layout: main-full
---
 
# Available es-cli Commands


Projections: 
```
delete, disable, enable, list, new, result, state, status, restore_checkpoint, has_stalled
```

<br/>Subscriptions:
```
list, create, update
```

<br/>config_generator:
```
create_config
```

---
layout: main-full
---


# Backing up a Database


* es-cli admin backup
    * initiates a backup to provided destination directory
<br/>
* es-cli admin azure_backup/s3_backup
    * initates backup to cloud storage
<br/>
* options
    * -databasesource
    * -databasedestination
    * -indexsource
    * -indexdestination
    * -differential
    * -deleteextra


---
layout: main-full
---
 

<!-- style: td { white-space: nowrap; } --> 

# Restore a Database

es-cli admin restore [options]

<!-- | Option               |Description                                                               |
|---------------------|---------------------------------------------------------------------------|
| -databasesource      | The location of the backup to restore                                     |
| -databasedestination | The destination of the restore                                            |
| -indexsource         | The location of the index backup (default: databasesource/index)          |
| -indexdestination    | The destination of the index restore (default: databasedestination/index) |
| -y                   | Automatic yes to prompts to delete files from destination directory       | -->


---
layout: main-full
---

# Deleting Streams

es-cli admin delete_streams [options]

<!-- | Option       | Description                                                    |
|--------------|----------------------------------------------------------------|
| -pattern     | Regular expression that the streams must match                 |
| -list        | Only list the streams matching the pattern, do not delete them |
| -fromall     | Force read stream names from $all                              |
| -fromstreams | Force read stream names from $streams                          |
| -noverify    | Does not verify if the stream exists (faster)                  |
|              | USE THE FOLLOWING OPTIONS WITH CAUTION!                        |
| -hard        | Hard delete the streams (Default: soft delete)                 |
| -system      | Include system streams (starting with $) for deletion          | -->

---
layout: main-full
---

# Managing Users

<!-- es-cli user [--version] [--help] <command> [args]
<br/>
| Command         | Description              |
|-----------------|--------------------------|
| add             | Add a user               |
| change_password | Change the user password |
| delete          | Delete a user            |
| disable         | Disable a user           |
| enable          | Enable a user            |
 
 -->

---
layout: main-full
---

# Managing Users


<!-- es-cli user [--version] [--help] <command> [<args>] -->
<br/>
<!-- | Command         | Description              |
|-----------------|--------------------------|
| list            | List all users           |
| reset_password  | Reset a user's password  |
| update          | Update a user            |
| Command         | Description              | -->


---
layout: main-full
---

# Projections

Delete a projection:

<br/>```es-cli projections delete [options]```

<br/>Disable a projection:

<br/>```es-cli projections disable [options]```

<br/>Enable a projection:

<br/>```es-cli projections enable [options]```


---
layout: main-full
---

# Projections


List all  projections:

<br/>```es-cli projections list [options]```

<br/>Create a new projection.

<br/>```es-cli projections new [options]```

<br/>Get the result of a projection:

<br/>```es-cli projections result [options]```


---
layout: main-full
---


# http api 

##

---
layout: main-full
---

# http API


The EventStoreDB http api enables both Admin and user operations using http requests. 

This allows scripting of functionality allowing users to write scripts to manage users, configure stream permissions, and automate operations. 


---
layout: main-full
---

# http api


* General Features
    *  Append events
    * Read streams
* Admin Features
    * Set stream permissions
    * Add user
    * Start scavenge
* There are more
    * See EventStoreDB_http_endpoints.html in your course content


<!-- Instructor Note, 
The file in the courseware repo, 
applied_course/EventStoreDB_http_endpoints.html
Has a longer, although not complete list. -->

---
layout: lab
---




# Lab: Using the EventstoreDB webui

---
layout: main-full
---

# Lab Instructions

Open 
`lab_webui.pdf`
in your Labs folder 


---
layout: lab
---

# Lab: Using es-cli

---
layout: main-full
---


# Lab Instructions


Open 
`lab_using_es-cli.pdf`
in your Labs folder 


---
layout: lab
---

# Lab: Using http api


---

# Lab Instructions


Please open
`lab_http.pdf`
in your Labs folder


---