Signup
======

The below Scenarios uses the datastore on scenario level.
A new customer gets registered, its name gets stored and reused.

Register a customer
-------------------
Use tags to enrich information about:
Which interface is used? user, admin, manager, ...
What functionality is tested?  signup, login, search, ...
What is the status of the implementation? inprogress, final, deprecated, ...
What is the execution priority / iteration? low, medium, high, smoke, nightly, ...
e.g.:
tags: user, signup, high, final, smoke

* Sign up a new customer
* On the customer page
* Just registered customer is listed
