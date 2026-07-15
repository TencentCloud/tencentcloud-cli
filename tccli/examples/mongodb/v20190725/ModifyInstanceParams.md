**Example 1: 修改 MongoDB 实例参数**



Input: 

```
tccli mongodb ModifyInstanceParams --cli-unfold-argument  \
    --InstanceId cmgo-g1fh**** \
    --InstanceParams.0.Key operationProfiling.mode \
    --InstanceParams.0.Value off
```

Output: 
```
{
    "Response": {
        "Changed": true,
        "TaskId": 100000745,
        "RequestId": "87582bb0-3be1-41e8-b54b-ecd8beb9a132"
    }
}
```

