import pytest
from src.other import clear_v1
from src.auth import auth_register_v1
from src.channel import channel_join_v1
from src.channel import channel_invite_v1
from src.channels import channels_create_v1
from src.channels import channels_listall_v1
from src.error import InputError, AccessError
from src.data_store import data_store

def test_valid_input():
    '''tests for valid channel_invite_v1 implementation'''
    clear_v1()
    user1 = auth_register_v1("AgentSmith@hotmail.com", "abcd1234", "Agent", "Smith")
    user2 = auth_register_v1("JohnSmith@hotmail.com", "abcd1234", "John", "Smith")
    auth_id1 = user1['auth_user_id']
    auth_id2 = user2['auth_user_id']
    channel = channels_create_v1(auth_id1, 'comp1531', True)
    channel_id = channel["channel_id"]
    channel_invite_v1(auth_id1,channel_id,auth_id2)

    channel_test_id = channels_listall_v1(auth_id2)
    output = channel_test_id['channels'][0]['channel_id']
    
    assert output == 1

'''Input Error Testing Module'''

def test_invalid_channel():
    '''tests for valid channel_invite_v1 with invalid channel_id'''
    clear_v1()
    user1 = auth_register_v1("AgentSmith@hotmail.com", "abcd1234", "Agent", "Smith")
    user2 = auth_register_v1("JohnSmith@hotmail.com", "abcd1234", "John", "Smith")
    auth_id1 = user1['auth_user_id']
    auth_id2 = user2['auth_user_id']
    channel = channels_create_v1(auth_id1, 'comp1531', True)
    channel_id = channel["channel_id"]
    channel_invite_v1(auth_id1,channel_id,auth_id2)
    invalid_channel1 = channel_id + 1
    invalid_channel2 = -1
    
    with pytest.raises(InputError):
        channel_invite_v1(auth_id1, invalid_channel1, auth_id2)
    with pytest.raises(InputError):
        channel_invite_v1(auth_id1, invalid_channel2, auth_id2)

def test_invalid_user():
    '''tests for valid channel_invite_v1 with invalid auth_user_id or u_id'''
    clear_v1()
    user1 = auth_register_v1("AgentSmith@hotmail.com", "abcd1234", "Agent", "Smith")
    user2 = auth_register_v1("JohnSmith@hotmail.com", "abcd1234", "John", "Smith")
    auth_id1 = user1['auth_user_id']
    auth_id2 = user2['auth_user_id']
    invalid_u_id1= auth_id1 - 1
    invalid_u_id2 = auth_id2 + 1
    channel = channels_create_v1(auth_id1, 'comp1531', True)
    channel_id = channel["channel_id"]
    
    with pytest.raises(InputError):
        channel_invite_v1(invalid_u_id1, channel_id, auth_id2)

    with pytest.raises(InputError):
        channel_invite_v1(auth_id1, channel_id, invalid_u_id2)

def test_repeated_user():
    '''tests for valid channel_invite_v1 with a user is already a member of the channel'''
    clear_v1()
    user1 = auth_register_v1("AgentSmith@hotmail.com", "abcd1234", "Agent", "Smith")
    user2 = auth_register_v1("JohnSmith@hotmail.com", "abcd1234", "John", "Smith")
    auth_id1 = user1['auth_user_id']
    auth_id2 = user2['auth_user_id']
    channel = channels_create_v1(auth_id1, 'comp1531', True)
    channel_id = channel["channel_id"]
    channel_invite_v1(auth_id1, channel_id, auth_id2)

    with pytest.raises(InputError):
        channel_invite_v1(auth_id1, channel_id, auth_id2)
    with pytest.raises(InputError):
        channel_invite_v1(auth_id1, channel_id, auth_id1)



'''Access Error Testing Module'''

def test_repeated_user():
    '''tests for channel_id is valid and the authorised user is not a member of the channel'''
    clear_v1()
    user1 = auth_register_v1("AgentSmith@hotmail.com", "abcd1234", "Agent", "Smith")
    user2 = auth_register_v1("JohnSmith@hotmail.com", "abcd1234", "John", "Smith")
    user3 = auth_register_v1("AgentJohnson@hotmail.com", "abcd1234", "Agent", "Johnson")
    auth_id1 = user1['auth_user_id']
    auth_id2 = user2['auth_user_id']
    auth_id3 = user2['auth_user_id']
    channel = channels_create_v1(auth_id1, 'comp1531', True)
    channel_id = channel["channel_id"]

    with pytest.raises(AccessError):
        channel_invite_v1(auth_id2, channel_id, auth_id3)
    
