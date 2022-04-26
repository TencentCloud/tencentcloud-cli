**Example 1: 批量解冻服务**



Input: 

```
tccli tcb UnfreezeCloudBaseRunServers --cli-unfold-argument  \
    --EnvId xx \
    --ServerNameList xx
```

Output: 
```
{
    "Response": {
        "FailServerList": [
            "xx"
        ],
        "Result": "xx",
        "RequestId": "xx"
    }
}
```

