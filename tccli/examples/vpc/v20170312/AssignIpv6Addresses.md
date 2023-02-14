**Example 1: 分配指定IPv6地址**

分配指定IPv6地址

Input: 

```
tccli vpc AssignIpv6Addresses --cli-unfold-argument  \
    --Ipv6Addresses.0.Description test2 \
    --Ipv6Addresses.0.Primary false \
    --Ipv6Addresses.0.Address 3402:4e00:20:1202::2 \
    --Ipv6Addresses.1.Description test1 \
    --Ipv6Addresses.1.Primary false \
    --Ipv6Addresses.1.Address 3402:4e00:20:1202::1 \
    --NetworkInterfaceId eni-5u5biujl
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
                "Description": "test1",
                "IsWanIpBlocked": false,
                "State": "PENDING"
            },
            {
                "Address": "3402:4e00:20:1202::2",
                "AddressId": "",
                "Primary": false,
                "Description": "test2",
                "IsWanIpBlocked": false,
                "State": "PENDING"
            }
        ],
        "RequestId": "4a8d6fc0-bc48-4394-b1f7-2818a217359a"
    }
}
```

**Example 2: 按个数自动分配IPv6地址**

按个数自动分配IPv6地址

Input: 

```
tccli vpc AssignIpv6Addresses --cli-unfold-argument  \
    --NetworkInterfaceId eni-5u5biujl \
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
                "Description": "",
                "IsWanIpBlocked": false,
                "State": "PENDING"
            },
            {
                "Address": "3402:4e00:20:1202:0:8d05:c272:f559",
                "AddressId": "",
                "Primary": false,
                "Description": "",
                "IsWanIpBlocked": false,
                "State": "PENDING"
            }
        ],
        "RequestId": "4a8d6fc0-bc48-4394-b1f7-2818a217359a"
    }
}
```

