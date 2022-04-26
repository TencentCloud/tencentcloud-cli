**Example 1: 查询独享实例列表**



Input: 

```
tccli apigateway DescribeExclusiveInstances --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Result": {
            "InstanceDescription": "xx",
            "InstanceId": "xx",
            "InstanceState": "xx",
            "InstanceChargeType": "xx",
            "ResourceId": "xx",
            "CreatedTime": "2020-09-22T00:00:00+00:00",
            "InstanceName": "xx",
            "InstanceType": "xx",
            "DealName": "xx"
        },
        "RequestId": "xx"
    }
}
```

