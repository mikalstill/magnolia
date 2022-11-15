A simple cooperative distributed queuing system
===============================================

Magnolia is a simple cooperative distributed queuing system. What does that mean? Well, it means that its a way of passing messages requesting work be done between machines, without a central server being involved. Instead the machines collaborate to queue the work in the correct place, and then ensure the work isn't lost in the case of a crash.

Magnolia was written as a replacement for a simple queueing system implemented using etcd, and similarly to etcd does not implement an authentication scheme -- network access to the REST API endpoint implies a trust relationship. This is obviously not great, and something to be improved in the future. The main issue here is how to manage keys across a cluster which currently shares nothing...