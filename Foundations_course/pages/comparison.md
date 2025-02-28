---
layout: section
---

    

# Comparing KurrentDB 
# to Other Systems

## 

---
layout: main-full
---

# Table of Contents

1. An example, storing user's address
2. Schema management
3. Systems comparison by operation
4. Comparison by unit of storage
5. Comparison by supported operations
6. Pub/Sub features
7. Projections



---
layout: main-full
---

# Key Concepts

When using any database (SQL, Document, NoSQL, or KurrentDB), its critical to understand the tools available to: 

* Manage potential conflicts between multiple readers and writers
* Enforce constraints
* Retrieve data or subsets of data
* Deletion process

This section discusses those concepts and compares KurrentDB to other types of databases.   


---
layout: main-full
---

# Example: Storing User Address

---
layout: main-full
---

# Adding a User

## Relational Database: 

Insert into users (id, name, address) VALUES  (1000, “John Doe”, "USA")

## MongoDB:

db.users.insert( { id: 1000, name: “John Doe”, address: “USA” } )

## Elastic

PUT /users/userdetails/1000 {“f”name: “John Doe”, address: "USA"}


---
layout: main-full
---

# Adding a User: KurrentDB


```
POST http://localhost:2113/streams/users-1000
Content-Type: application/vnd.eventstore.events+json

[
  {
    "eventId": "fbf4a1a3-b4a3-3dfe-a01f-ec52c34e19e9",
    "eventType": "user-added",
    "data": {
      "name": "John Doe",
      "address": "USA"
    }
  }
]

```

---
layout: main-full
---

# Changing a User's Address

## Relational Database: 

Update users set address="CAN" where id = 1000;

## MongoDB:

```
db.users.updateOne(
      { "name" : "John Doe" },
      { $set: { "address" : "CAN" } }
   );
```

## Elastic

POST /users/userdetails/_update/1000
{
  "doc": {
    "address": "CAN"
  }
}


---
layout: main-full
---

# Changing a User's Address: KurrentDB


```
POST http://localhost:2113/streams/users-1000
Content-Type: application/vnd.eventstore.events+json

[
  {
    "eventId": "fbf4a1a3-b4a3-3dfe-a01f-ec52c34e19e9",
    "eventType": "Update Address",
    "data": {
      "address": "CAN"
    }
  }
]

```

---
layout: main-full
---

# Retrieving a User's Address

## Relational Database: 

Select address from users where id = 1000;

## MongoDB:

```
db.users.find( { "name": ""name" : "John Doe" } )
```

## Elastic

```
GET users/userdetails/_search
{
  "query": {
    "match": {
      "user.name": "John Doe"
    }....
  }}
```

---
layout: main-full
---

# Retrieving Address: KurrentDB

## Get all Events
```
events = client.get_stream(
    stream_name="user-1000",
    stream_position=0,
    limit=100,
)

```

## Returns list of events

* Paginate through events to get most recent address
* Alternate method, read backwards till first address entry

---
layout: main-full
---

# How Data is stored

## Relational Database

Address is a mutable column in a row of the users table

## MongoDB

Address is a field in a mutable document

## Elastic Search

User Address is a field in a mutable document



---
layout: main-full
---

# How Data is stored

## KurrentDB

Address is a field in an immutable event appended to a stream


---
layout: main-full
---

# Schema Management

## Relational Database

Schema is defined when the table is created

## MongoDB

Defaults to flexible schema, can be configured to validate schema

## Elastic

Defaults to flexible schema


---
layout: main-full
---

# Schema Management

## KurrentDB

Events are stored as schemaless byte arrays.

---
layout: main-full
---

# Schema Management Summary

In systems that do not authenticate or validate data against a schema, schema management becomes the responsibility of the application.

---
layout: main-full
---

# How Data is Stored (MOVE)

Some systems store data as a document that can be read and rewritten as a new version. Others store data as a table with a collection of rows containing typed columns. 

This section breaks down the topic into:

* Unit of storage
* Available operations
* Schemas
* Pub-sub functionality

---
layout: main-full
---

# Systems Comparison


---
layout: main-full
---

# Systems Comparison

| RDBMS | MongoDB | KurrentDB|
|---|---|---|
| Create Row | Create Document | Append event to new stream |
| Update Row | Update Document | Append event to existing stream |
| Delete Row | Delete Document | Delete stream |
| Retrieve by id | Retrieve by ID | Load stream by id |
| Retreive by range | Retrieve by Range | Not Supported |


---
layout: two-cols-header
---

# Update state

::left::

## "Regular" database

* Mutate entity properties
* Detect mutated properties
* Compose a valid update operation
* Execute update in the database (group of table rows or a document)
<br>&nbsp;</br>
<br>&nbsp;</br>
<br>&nbsp;</br>
<br>&nbsp;</br>
<br>&nbsp;</br>
<br>&nbsp;</br>

::right::

## KurrentDB

* Emit new events
* Serialize events to bytes
* Figure entity stream name
* Append events to the stream
<br>&nbsp;</br>
<br>&nbsp;</br>
<br>&nbsp;</br>
<br>&nbsp;</br>
<br>&nbsp;</br>
<br>&nbsp;</br>


---
layout: two-cols-header
---

# Typical Application Flow

::left::

## "Regular" database
* Retrieve latest state
* Ensure action can be performed
* Mutate state
* Persist new state
<br>&nbsp;</br>
<br>&nbsp;</br>
<br>&nbsp;</br>
<br>&nbsp;</br>
<br>&nbsp;</br>
<br>&nbsp;</br>

::right::
## KurrentDB
* Read stream
* Restore state
* Ensure action can be performed
* Emit events
* Persist events
<br>&nbsp;</br>
<br>&nbsp;</br>
<br>&nbsp;</br>
<br>&nbsp;</br>
<br>&nbsp;</br>
<br>&nbsp;</br>

---
layout: two-cols-header
---

# Retrieve State

::left::

## "Regular" database
* Load data from database (group of table rows or a document)
* Map data to an entity object.
<br>&nbsp;</br>
<br>&nbsp;</br>
<br>&nbsp;</br>
<br>&nbsp;</br>
<br>&nbsp;</br>
<br>&nbsp;</br>

::right::
## KurrentDB

* Load data from database (events from one stream)
* Deserialize events to objects
* Evolve state from all events
<br>&nbsp;</br>
<br>&nbsp;</br>
<br>&nbsp;</br>
<br>&nbsp;</br>
<br>&nbsp;</br>
<br>&nbsp;</br>


---
layout: main-full
---

# Comparison by Unit of Data Storage


---
layout: main-full
---

# Systems Comparison:

**Unit of Data Storage**


| Database Type | Base Unit of Storage| 
|---------------|---------------------|
|Relational database (MySQL, Postgres, Oracle)|Rows
|Document store(MongoDB, Cosmos, Elastic)|Documents
|KurrentDB| Events (Immutable, ordered, schemaless byte arrays) |



---
layout: main-full
---

# Comparison by Supported Operations


Some systems allow granular updates/deletes.  Others group data into subsets and allow granular updates/deletes on those subsets. 

Some systems allow updates of previously written data in place.  Others replace the previous version with a new version containing the update/delete.

The following slide(s) summarize those differences


<!-- Instructor Note
This is key to enabling proper understanding and use of KurrentDB, certain classes may already understand the differences, but it is critical to have a baseline understanding, go as deep or as shallow as the class requires  -->

---
layout: main-full
---


# Overview of KurrentDB, Supported Operations


| Database Type| Supported Operations |
|--------------|----------------------|
|Relational database (MySQL, Postgres, Oracle)|Create, Read, Update, Delete (rows)|
|Document store (MongoDB, Cosmos, Elastic)|Create, Read, Update, Delete (documents) |
|KurrentDB|Create(append), Read, Delete* (events)|


---
layout: main-full
---

# Reading Data

|Database Type | Read Path | Subscriptions |
|--------------|-----------|---------------|
| Relational | Granular reads or scans/joins with filters interpreted and applied by the server | No subscriptions |
| NoSQL | Differs per system | Differs per system |
| KurrentDB | Read Stream/projection sequentially forwards/backwards | Subscriptions to streams/projections |


---
layout: main-full
---

# Data Transformations on Write

|Database Type | Write Transformation | 
|--------------|-----------|
| Relational | Triggers, Stored Procedures |
| Document Database | Differs per system | 
| KurrentDB | Projections |


---
layout: main-full
---

# Deleting Data:

Scope of delete operations

* Relational Database
    * Delete a row, or rows in a single statement based on a search query.
* Document Store
    * Delete a document.
* KurrentDB
    * Delete a stream and all events.
    * Delete all events older than x(date), or greater than n(number).

---
layout: main-full
---

# Pub/Sub Functionality

KurrentDB has a built in Pub/Sub feature.

* Managed Subscriptions
    * Subscription State is managed by KurrentDB
* Catch Up Subscriptions
    * Subscription State is managed by the applicaiton    

---
layout: main-full
---

# Subscription Scope

* Single Stream
    * Includes Streams generated by projections
* $all Stream
    * Stream of all events written to all streams

---
layout: main-full
---

# Projections

KurrentDB supports projections. 

Projections "project" events, or links to events from the stream the event was written to into another stream. 

---
layout: main-full
---

# Projection Types

**KurrentDB supports two types of projections

* System Projections
    * Standard projections based on Event Type, Category, etc
* User Defined Projections
    * Custom projections against a stream, the $all stream or multple streams 