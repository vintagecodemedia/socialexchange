# Social Exchange Communications
The big pivot point of Social Exchange is the "outpost" node, which is the piece that all providers use to interface with one another.

## Connecting and Transacting

### SRV DNS Record
Any valid reachable inbound outpost needs to have a SRV record in DNS. If there are updates destined for the user terry@a.example.com, the sending client will look up _sxpost._tcp.a.example.com.

### Connecting
Connections may be done on a one-and-done basis, or if both parties allow it, they may be kept alive for more transactions.  Busy active gateways might prefer this.

### Handshake
Upon connection the server is silent until the client begins the handshake which is "SXP " followed by a space-separated list of supported versions, highest priority first

    SXP 1.0 0.9 0.8 0.7

The server responds with the selected version.  The version MUST be listed in the client handshake, otherwise it MUST respond with a failure handshake.  If this condition is not adequately met, the client MUST disconnect.

Success:
    ACCEPT 0.9

Anything other than "ACCEPT " followed by a client-listed version is a failed handshake.

### Alternate protocols
SXP servers MAY accept traffic destined for other protocols where the client initiates a handshake.

### Encryption
Immediately after the protocol version is negotiated, the server must present a certificate, and the client must decide whether or not to honor it. Then the client presents a client certificate and the server must decide whether to honor that.  At this point all communications are encrypted.

### Provider-Provider Transactions
When a user creates content and allows another user on another network to receive it, the first provider will use UPDATE
    UPDATE TO bob@b.example.com FROM alice@a.example.com <content-id> <type> <preview-bytesize><preview>

To which sensible responses include
    200 OK
