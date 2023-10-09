**Example 1: 查看集群是否能回滚**



Input: 

```
tccli dlc CheckDataEngineImageCanBeRollback --cli-unfold-argument  \
    --DataEngineId DataEngine-1
```

Output: 
```
{
    "Response": {
        "FromRecordId": "d3018ad4-9a7e-4f64-a3f4-f38507c69742",
        "ToRecordId": "89570c65-49de-4bbd-ac0a-a67c724fc80f",
        "IsRollback": true,
        "RequestId": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1"
    }
}
```

