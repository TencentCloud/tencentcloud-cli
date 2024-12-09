**Example 1: 申请按小时流量计费的常规BGP IPv6地址。**

申请按小时流量计费的常规BGP IPv6地址。

Input: 

```
tccli vpc AllocateIPv6Addresses --cli-unfold-argument  \
    --AddressCount 1
```

Output: 
```
{
    "Response": {
        "AddressSet": [
            "eipv6-m44ku5d2"
        ],
        "TaskId": "61531421",
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

