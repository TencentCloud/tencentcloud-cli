**Example 1: 获取实例列表**

获取实例列表

Input: 

```
tccli tdmq DescribeRocketMQVipInstances --cli-unfold-argument  \
    --Limit 1 \
    --Filters.0.Values rocketmq-1q23swe3 \
    --Filters.0.Name order-instance \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "23ca1a58-0388-4d2d-8465-653a53addda7",
        "Instances": [
            {
                "Status": 1,
                "PayMode": 1,
                "Remark": "remark-info",
                "AutoRenewFlag": 1,
                "InstanceId": "rocketmq-1233",
                "NodeCount": 1,
                "ExpireTime": 1,
                "InstanceVersion": "4.9.3",
                "MaxStorage": 1,
                "MaxBandWidth": 1,
                "SpecName": "rocket-vip-basic-1",
                "ConfigDisplay": "基础型",
                "InstanceName": "order-instance",
                "MaxTps": 1,
                "AclEnabled": true,
                "Retention": 0,
                "MinRetention": 0,
                "MaxRetention": 0
            }
        ]
    }
}
```

