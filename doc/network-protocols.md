# Network Protocols
Social Exchange uses HTTP in various service roles.  It also can use a service called SXP (Social Exchange Post) that has a mix of features found in HTTP and SMTP.

# Protocol version
As of 2017-07-10 We're using HTTP API version v0.0 to accumulate the design specs. When the spec stabilizes we will roll that up to v1.1 and begin promotion.  Spec versions ending in an even number are reserved for immature concepts.  This applies to HTTP and SXP alike.

# SXP vs HTTP Gateways
SXP and HTTP are meant to be capable of the same kinds of methods.


# Service Roles

## Public Posts
Public Posts (or Outposts or Relay)  are used for interoperation between providers.

### Addressing
A provider controls a DNS name such as "example.com" or "bobshouse.dyn.example.net".

