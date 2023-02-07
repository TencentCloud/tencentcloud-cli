**Example 1: 修改云数据库实例账号的主机**



Input: 

```
tccli cdb ModifyAccountHost --cli-unfold-argument  \
    --InstanceId cdb-f35wr6wj \
    --Host 127.0.0.1 \
    --User ajnnw \
    --NewHost %
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "AsyncRequestId": "256117ed-efa08b54-61784d44-91781bbd"
    }
}
```

