# SignOn Proof-of-concept

# Domains
bigsite.example.com and littlesite.example.com are virtual providers operating on one provider instance.
homesite.example.com we will pretend is a proxy to somebody's house.

# relay-loadbalancer.py
This is the service that the DNS SRV records would map to.  It does load balancing in 2 ways, but distribution is always round robin.  For homesite.example.com it performs a persistent stateful proxy.  ???Should it be transparent to the client, or do we need an instruction to nest a new TLS connection???.  For the other two it performs an out-of-band redirect.

The SRV records point at this service:
    _sxp_public._tcp.bigsite.example.com
    _sxp_public._tcp.littlesite.example.com
    _sxp_public._tcp.homesite.example.com

Like

# provider-public-relay.py
This is a service which accepts traffic for forwarding to 3 domains, the ones mentioned above.

In some cases it forwards you
