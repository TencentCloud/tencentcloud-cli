**Example 1: 实例未开启SRV链接**



Input: 

```
tccli mongodb DescribeSRVConnectionDomain --cli-unfold-argument  \
    --InstanceId cmgo-3ap*****
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter",
            "Message": "SRV connection has not enabled."
        },
        "RequestId": "ac6aebb4-fddc-4a7c-9ce2-00359c74ce67"
    }
}
```

