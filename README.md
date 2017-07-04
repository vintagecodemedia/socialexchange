# SignOn/Social Exchange Protocol
SignOn/SXP Is a social networking system built around layers of public key trust. This systems aims to create a feature set and protocol for disparate social networks to interoperate, while giving users a new level of two way trust and selective privacy. SXP is meant to be decentralized in the same fashion that E-Mail is, where providers look eachother up for delivery of content. It differs from e-mail in that all actions must be signed, and it provides social networking features like content management.

Intended feature set for users:

 * Adding Contacts
 * Managing groups of followed contacts
 * Managing permissions of visibility to contacts
 * Publishing content of varying types
 * Pushing announcements (status updates), with attached preview data and references to other content
 * Creating content collections (for example photo albums)
 * Direct Messaging
 * Direct Messaging with end-to-end encryption, using tools like browser extensions and client access applications
 * "Signing" of contacts' announcements and publications. This conveys upvoting or other public emotional responses to contacts.
 * "Signing" of contacts. This helps to validate real people and organizations, playing into a globalized reputation system.
 * Session Initiation.  End-to-end "stateful" communications for chat, voice, video or whatever else needs to be session oriented.
 * Flexibility in contact control--blacklist or whitelist users or whole providers based on criteria, such as knowledge or reputation.
 * Contact requesting--Make friends.
 * Contact request management--filter contact requests by criteria such as reputation and provider.
 * Directory privacy--How much of your info is available for anonymous search, if any.

Intended feature set for providers:
 * Efficient Interoperation through SXP with fallback on HTTP API
 * Flexibility in contact control, as seen at the user level
 * Publishing content policies in the style of Mastodon
 * Ability to run on small home appliances, optionally with the help of public gateway services
 * Gateway services use netsted TLS layers so that virtual host requests may remain private
   * Client TLS to gateway before requesting the host domain. Then another layer of TLS proxied by the gateway to ensure private communications from the gateway administration.
 * Spam deterrent. Published updates will have to be digitally signed by the sender after the receiving server issues a receipt-id. Non-reputable sources may be rejected or heavily time delayed, or forced to sign out of band.

Intended feature set for user agents:
 * Efficient connectivity through SXP with fallback on HTTP API
 * Optional endpoint key pair, used for end-to-end encryption
 *

## Mission
The short-term mission of SignOn/SXP is to provide a complete specification and proof of concept for a decentralized social networking system that ought to be able to replace any of the major players that exist today, or better yet to compel them to get connected to SXP. SignOn/SXP must provide a robust feature set and ultimate privacy control. Once the technology is established a new mission statement will need to be written which aims to assure the survival and freedom of this system.

## Why?
The persons you see to your left and right are addicted to social networking--one provider in particular.  This is a dangerous predicament, sometimes even alluded to by these companies themselves.  It is truly time to deliver freedom and democracy to the users of social networking.  In our vision, those who enjoy the large providers should be able to stay on them while still being able to network with anybody who chooses to operate on smaller or more private providers.

## Can this be done?
See E-Mail.  The concept of SXP is similar to SMTP, although it employs a combination of pushing updates metadata and pulling on-demand only as needed, which prevents unnecessary propagation of data.  SignOn/SXP while much heavier than email overall can employ various technologies and various levels of help from CDNs and other providers.  There really isn't anything new here--it is content management and signed messages.  The piece that resembles the behavior of E-Mail is designed to be small.

## Hasn't this been done before?
I hope so.  It's taken long enough.  Let's see some actually successful providers who can interoperate. There is Mastodon, but it's more a twitter replacement.  We need a system for sharing more types of content, managing that content into collections, and even sharing that content with people who don't have a provider at all.  We also want to support end-to-end message encryption.

## This specification is trash!
I'm glad you think so! You must have great ideas, so please help! I don't necessarily wish to build the perfect social media platform--I wish to get the herd off of one dangerously large one without losing key crucial capabilities.

## What is the actual direction?
At this time it's almost entirely up in the air.  You can see more stuff at [doc](./doc), and particularly [the requirements](./doc/requirements.md) table to help guide the specification along as a WIP.

## Communication Model
There are several ways Social Exchange can be implemented.  These different styles of service answer to different users' needs, mostly dealing in the convenience-security tradeoff.  But the bare requirements to be a valid Social Exchange Provider are pretty straightforward.  A public-facing social exchange host is required to interoperate with other providers.  This is a service which is capable of two-way authentication and handles pushing and pulling of data between providers.  Once updates are pushed and content is pulled, it's up to your implementation to make fancy presentation and management features to attract users.

Refer to [Social Exchange Communications](./doc/social-exchange-communications.md) for the gritty details.

## Privacy and Security
Social Exchange aims to bake in key concepts to prevent phishing and spam and unsolicited content. It uses PKI to authenticate content creators and other posts making requests.  The specification demands that every single user has at least one key pair, so messages in-flight are protected, unlike SMTP.

### Registered Endpoints
Social Exchange Users can register "endpoints (or "clients") that have their own asymmetric key pair.  Social Exchange hosts can query for those public keys by name for people desiring to send truly end-to-end encrypted messages to those users.  Users may also provide "unlisted" public keys, for which the sender needs to know that key's given name when querying for it.  This can prevent coercion from automated scanning.

Endpoints can also be aliased into a group.  This basically pulls down 1 or many public keys for the sender to encrypt with.

### Federation of Providers
So long as you do not lose control of your DNS, providers will not accept forged messages from your provider because sending messages must be signed with a valid provider certificate.  The free market should be diligent to select sensible certificate authorities and perhaps other listing services and PKIs and reputation systems.  Specifications for trust and reputation are TBD.

## Client Access Model
As mentioned earlier, the Social Exchange system is designed such that people can run their own "thick" client, using the Social Exchange provider as an outpost or medium for interoperability.  But most commonly, providers will provide a web-based portal for convenience and feature parity with the existing competition.  There is no technical reason why providers can't support multiple types of client access.

## Existing Services
At the time of this writing, there are none.  To live up to the mission statement, reference implementations are to be created along with sample configurations to suit various different business models.

Refer to [Business Models](./doc/business-models.md) for some sample configurations.

