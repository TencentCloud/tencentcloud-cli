**Example 1: 释放弹性公网IPv6地址带宽**

入参传递Ip6AddressIds

Input: 

```
tccli vpc ReleaseIp6AddressesBandwidth --cli-unfold-argument  \
    --Ip6AddressIds eip-31g37kea
```

Output: 
```
{
    "Response": {
        "TaskId": "12579789",
        "RequestId": "fe6aa94a-2a74-41d8-9570-337a575443fe"
    }
}
```

**Example 2: 释放弹性公网IPv6地址带宽-2**

入参传递Ip6Addresses

Input: 

```
tccli vpc ReleaseIp6AddressesBandwidth --cli-unfold-argument  \
    --Ip6Addresses 2402:4e00:1000:200:0:8d8a:60b7:87f8
```

Output: 
```
{
    "Response": {
        "TaskId": "12579786",
        "RequestId": "3287c8ef-2bfb-4ae7-8874-f3628c0344b1"
    }
}
```

