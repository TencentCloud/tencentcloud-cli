**Example 1: Assigning the specified IPv6 address**



Input: 

```
tccli vpc AssignIpv6Addresses --cli-unfold-argument  \
    --NetworkInterfaceId eni-5u5biujl\
    --Ipv6Addresses.0.Address 3402:4e00:20:1202::1\
    --Ipv6Addresses.0.Primary false\
    --Ipv6Addresses.0.Description test1\
    --Ipv6Addresses.1.Address 3402:4e00:20:1202::2\
    --Ipv6Addresses.1.Primary false\
    --Ipv6Addresses.1.Description test2
```

Output: 
```
{
    "Response": {
        "Ipv6AddressSet": [
            {
                "Address": "3402:4e00:20:1202::1",
                "AddressId": "",
                "Primary": false,
                "PublicIpAddress": "3402:4e00:20:1202::1",
                "Description": "test1",
                "IsWanIpBlocked": false,
                "State": "PENDING"
            },
            {
                "Address": "3402:4e00:20:1202::2",
                "AddressId": "",
                "Primary": false,
                "PublicIpAddress": "3402:4e00:20:1202::2",
                "Description": "test2",
                "IsWanIpBlocked": false,
                "State": "PENDING"
            }
        ],
        "RequestId": "4a8d6fc0-bc48-4394-b1f7-2818a217359a"
    }
}
```

**Example 2: Assigning IPv6 addresses by number automatically**



Input: 

```
tccli vpc AssignIpv6Addresses --cli-unfold-argument  \
    --NetworkInterfaceId eni-5u5biujl\
    --Ipv6AddressCount 2
```

Output: 
```
{
    "Response": {
        "Ipv6AddressSet": [
            {
                "Address": "3402:4e00:20:1202:0:8d05:c272:f514",
                "AddressId": "",
                "Primary": false,
                "PublicIpAddress": "3402:4e00:20:1202:0:8d05:c272:f514",
                "Description": "",
                "IsWanIpBlocked": false,
                "State": "PENDING"
            },
            {
                "Address": "3402:4e00:20:1202:0:8d05:c272:f559",
                "AddressId": "",
                "Primary": false,
                "PublicIpAddress": "3402:4e00:20:1202:0:8d05:c272:f559",
                "Description": "",
                "IsWanIpBlocked": false,
                "State": "PENDING"
            }
        ],
        "RequestId": "4a8d6fc0-bc48-4394-b1f7-2818a217359a"
    }
}
```

