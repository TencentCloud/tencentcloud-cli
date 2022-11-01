**Example 1: 获取实例列表**



Input: 

```
tccli tdmq DescribeRabbitMQVipInstances --cli-unfold-argument  \
    --Limit 1 \
    --Filters.0.Values xx \
    --Filters.0.Name xx \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "xx",
        "Instances": [
            {
                "Status": 1,
                "PayMode": 1,
                "Remark": "xx",
                "AutoRenewFlag": 1,
                "InstanceId": "xx",
                "NodeCount": 1,
                "ExpireTime": 1,
                "InstanceVersion": "xx",
                "MaxStorage": 1,
                "MaxBandWidth": 1,
                "SpecName": "xx",
                "ConfigDisplay": "xx",
                "InstanceName": "xx",
                "MaxTps": 1
            }
        ]
    }
}
```

