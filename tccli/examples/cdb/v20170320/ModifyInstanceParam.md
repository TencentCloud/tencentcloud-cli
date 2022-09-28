**Example 1: 修改实例参数**



Input: 

```
tccli cdb ModifyInstanceParam --cli-unfold-argument  \
    --NotSyncDr True \
    --NotSyncRo True \
    --ParamList.0.CurrentValue xx \
    --ParamList.0.Name xx \
    --TemplateId 0 \
    --InstanceIds cdb-atjl8gns \
    --WaitSwitch 0
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "AsyncRequestId": "38265324-dd030463-3d46a793-4a0420b1"
    }
}
```

