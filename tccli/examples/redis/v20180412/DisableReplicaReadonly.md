**Example 1: 关闭读写分离**



Input: 

```
tccli redis DisableReplicaReadonly --cli-unfold-argument  \
    --InstanceId crs-5a4py64p
```

Output: 
```
{
    "Response": {
        "RequestId": "2d4387ee-2011-449e-a32b-87f9366f3ef4",
        "TaskId": 15236
    }
}
```

