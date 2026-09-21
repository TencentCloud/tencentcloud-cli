**Example 1: 批量删除消费组灰度标签成功**



Input: 

```
tccli trocket DeleteConsumerLabels --cli-unfold-argument  \
    --InstanceId rmq-1****jjdr \
    --Labels.0.Group bs01-fb0534 \
    --Labels.0.Label nw01fb0534
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "FailedCount": 0,
        "Failures": [],
        "RequestId": "c8f5a5e1-6abd-4881-9d99-e7507bd369af"
    }
}
```

