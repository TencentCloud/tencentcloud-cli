**Example 1: 变配同时修改规格相关的参数**



Input: 

```
tccli postgres ModifyDBInstanceSpec --cli-unfold-argument  \
    --DBInstanceId postgres-hys3shmz \
    --Memory 2 \
    --Storage 100 \
    --Cpu 1 \
    --SyncModifyParams.0.Name max_connections \
    --SyncModifyParams.0.ExpectedValue 2048
```

Output: 
```
{
    "Response": {
        "BillId": "",
        "DealName": "",
        "RequestId": "2f149335-b67e-48f9-bbfa-1448d85631e5"
    }
}
```

