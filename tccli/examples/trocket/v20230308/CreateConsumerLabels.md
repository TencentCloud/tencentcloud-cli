**Example 1: 批量创建标签成功示例**



Input: 

```
tccli trocket CreateConsumerLabels --cli-unfold-argument  \
    --InstanceId rmq-1****jjdr \
    --Labels.0.Group grp-aa3973 \
    --Labels.0.Label lcaa3973
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "FailedCount": 0,
        "Failures": [],
        "RequestId": "e7c0acd5-2ddd-48ef-9086-5f4cfb758af3"
    }
}
```

