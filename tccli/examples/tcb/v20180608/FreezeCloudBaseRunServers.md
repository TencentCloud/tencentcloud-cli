**Example 1: 批量冻结**



Input: 

```
tccli tcb FreezeCloudBaseRunServers --cli-unfold-argument  \
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

