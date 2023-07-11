**Example 1: 指定ipv6地址开通公网访问能力**



Input: 

```
tccli ecm AllocateIpv6AddressesBandwidth --cli-unfold-argument  \
    --EcmRegion ap-xian-ecm \
    --Ipv6Addresses 2402:4e00:1000:200:0:8d8a:60b7:87f8
```

Output: 
```
{
    "Response": {
        "AddressSet": [
            "eip-3l4nwzvo"
        ],
        "TaskId": 202869021,
        "RequestId": "aac03e7b-3c91-4970-b2bc-c20f0c6bdd38"
    }
}
```

