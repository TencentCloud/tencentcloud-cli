**Example 1: 按个数自动分配IPv6地址**

按个数自动分配IPv6地址

Input: 

```
tccli ecm AssignIpv6Addresses --cli-unfold-argument  \
    --EcmRegion ap-xian-ecm \
    --NetworkInterfaceId eni-1snva0vd \
    --Ipv6AddressCount 1 \
    --SkipCheckIPv6Address true \
    --SkipAllocateBandwidth true
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
            }
        ],
        "RequestId": "4a8d6fc0-bc48-4394-b1f7-2818a217359a"
    }
}
```

