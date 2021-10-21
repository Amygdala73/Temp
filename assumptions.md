# Assumptions
## Auth

### auth_register_v1

1. Multiple users can register with the same first names, last names and passwords.

## DMs

### dm_create_v1

1. The creator of the dm cant be in the users list.

## Channels

### channels_create_v1

1. Every channel has its unique id.

### channel_messsages_v1

1. In iteration 1, total messages is zero as messages cannot be created.
2. End return -1, in iteration 1 as there is no messages.
3. In iteraton 1, messages returns an empty list as no messages can be created.

## Channel

### channel_join_v1

1. Users can not join the channel where he/she/sth is already a member.
2. Users can join 0, 1 or more channels.

### channel_invite_v1

1. Users can join any channel that the user is being invited, regardless tha channel
   is private or not.

## Data store

1. There will be an entry for storing the information of users.
2. There will be an entry for storing the information of channels.
3. There will be an entry for storing messages.

## Other

### clear_v1

1. This function will clean all the users, channels, and messages.
