**Example 1: 批量冻结**

批量冻结

Input: 

```
tccli tcb FreezeCloudBaseRunServers --cli-unfold-argument  \
    --EnvId env-abc \
    --ServerNameList abc
```

Output: 
```
{
    "Response": {
        "FailServerList": [
            "abc"
        ],
        "Result": "abc",
        "RequestId": "aa"
    }
}
```

