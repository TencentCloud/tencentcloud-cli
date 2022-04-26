**Example 1: 启用读写分离**



Input: 

```
tccli redis EnableReplicaReadonly --cli-unfold-argument  \
    --InstanceId crs-5a4py64p
```

Output: 
```
{
    "Response": {
        "RequestId": "2d4387ee-2011-449e-a32b-87f9366f3ef4",
        "Status": "OK",
        "TaskId": 21312
    }
}
```

