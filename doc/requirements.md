# Requirements

This document will outline core requirements of the system and relate to parts of the specification that meet them, or fall short of meeting them.

## Interoperation

### Private communications between SXPs
Between two posts, the only unencrypted communication is the initial protocol version handshake (->SXP <version>[ ..<versions>..]) (<-ACCEPT <version>)

See [Encryption](./social-exchange-communications.md)

### Private communications between users
Communications transmitted are encrypted using a recipient's public key.  If these communications are more sensitive, it is up to the users to select a destination key where the private key is managed by an appopriate layer.  Examples would be a user's endpoint device, or a corporate shared client system (like a web application, but run very privately)

