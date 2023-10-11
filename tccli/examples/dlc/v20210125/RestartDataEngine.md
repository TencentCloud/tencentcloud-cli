**Example 1: 重启集群**

重启集群

Input: 

```
tccli dlc RestartDataEngine --cli-unfold-argument  \
    --DataEngineId abc \
    --ForcedOperation True
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

