**Example 1: 获取实例列表**

获取实例列表

Input: 

```
tccli tdmq DescribeRocketMQVipInstances --cli-unfold-argument  \
    --Limit 20 \
    --Offset 0
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
                "InstanceId": "rocketmq-vvqb9emabapx",
                "NodeCount": 3,
                "ExpireTime": 1730877758000,
                "InstanceVersion": "4.9.3",
                "MaxStorage": 200,
                "MaxBandWidth": 10,
                "SpecName": "rocket-vip-basic-1",
                "ConfigDisplay": "基础型",
                "InstanceName": "order-instance",
                "MaxTps": 4000,
                "AclEnabled": true,
                "Retention": 72,
                "MinRetention": 72,
                "MaxRetention": 960
            }
        ]
    }
}
```

