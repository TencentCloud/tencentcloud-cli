**Example 1: 批量冻结**

批量冻结

Input: 

```
tccli tcb FreezeCloudBaseRunServers --cli-unfold-argument  \
    --EnvId env-ser \
    --ServerNameList server
```

Output: 
```
{
    "Response": {
        "FailServerList": [
            ""
        ],
        "Result": "succ",
        "RequestId": "sdfsfadf"
    }
}
```

