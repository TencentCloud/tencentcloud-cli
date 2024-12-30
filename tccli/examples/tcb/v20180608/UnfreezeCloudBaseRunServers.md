**Example 1: 批量解冻服务**



Input: 

```
tccli tcb UnfreezeCloudBaseRunServers --cli-unfold-argument  \
    --EnvId env-sdfsdf \
    --ServerNameList server
```

Output: 
```
{
    "Response": {
        "FailServerList": [
            "server"
        ],
        "Result": "succ",
        "RequestId": "sdfsfdf"
    }
}
```

