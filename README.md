# Social Exchange
The Social Exchange Protocol

## Mission
The mission of Social Exchange is to create a medium for social networks to interoperate.  We aim to build a protocol and reference implementations so robust that free market Social Exchange services will become as prevalent as E-Mail and that large existing social network operators will be compelled to join this open standard in order to keep its user base.

## Communication Model
There are several ways Social Exchange can be implemented.  These different styles of service answer to different users' needs, mostly dealing in the convenience-security tradeoff.  But the bare requirements to be a valid Social Exchange Provider are pretty straightforward.  A public-facing social exchange host is required to interoperate with other providers.  This is a service which is capable of two-way authentication and handles pushing and pulling of data between providers.  Once updates are pushed and content is pulled, it's up to your implementation to make fancy presentation and management features to attract users.

Refer to [Social Exchange Communications](./doc/social-exchange-communications.md) for the gritty details.

## Privacy and Security
Social Exchange aims to bake in key concepts to prevent phishing and spam.

### Registered Endpoints
Social Exchange Users can register "endpoints (or "clients") that have their own asymmetric key pair.  Social Exchange hosts can query for those public keys by name for people desiring to send truly end-to-end encrypted messages to those users.  Users may also provide "unlisted" public keys, for which the sender needs to know that key's given name when querying for it.  This can prevent coercion from automated scanning.

Endpoints can also be aliased into a group.  This basically pulls down 1 or many public keys for the sender to encrypt with.

### Federation of Providers
So long as you do not lose control of your DNS, providers will not accept forged messages from your provider because sending messages must be signed with a valid provider certificate.

## Client Access Model
As mentioned earlier, the Social Exchange system is designed such that people can run their own "thick" client, using the Social Exchange provider as an outpost or medium for interoperability.  But most commonly, providers will provide a web-based portal for convenience and feature parity with the existing competition.  There is no technical reason why providers can't support multiple types of client access.

## Existing Services
At the time of this writing, there are none.  To live up to the mission statement, reference implementations are to be created along with sample configurations to suit various different business models.

Refer to [Business Models](./doc/business-models.md) for some sample configurations.

