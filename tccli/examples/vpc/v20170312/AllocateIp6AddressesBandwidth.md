**Example 1: 指定ipv6地址开通公网访问能力**

指定ipv6地址开通公网访问能力。

Input: 

```
tccli vpc AllocateIp6AddressesBandwidth --cli-unfold-argument  \
    --Ip6Addresses 2402:4e00:1000:200:0:8d8a:60b7:87f8 \
    --InternetMaxBandwidthOut 1
```

Output: 
```
{
    "Response": {
        "AddressSet": [
            "eip-68dqs5ri"
        ],
        "TaskId": "194395704",
        "RequestId": "283a29bf-982d-4d55-984a-0d464f61f9ae"
    }
}
```

