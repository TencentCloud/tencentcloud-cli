**Example 1: Modifying instance parameter**



Input: 

```
tccli cdb ModifyInstanceParam --cli-unfold-argument  \
    --InstanceIds cdb-atjl8gns\
    --ParamList.0.Name auto_increment_increment\
    --ParamList.0.CurrentValue 1\
    --TemplateId 99\
    --InTimeWindow true
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

