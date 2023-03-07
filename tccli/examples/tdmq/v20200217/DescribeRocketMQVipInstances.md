**Example 1: 获取实例列表**

获取实例列表

Input: 

```
tccli tdmq DescribeRocketMQVipInstances --cli-unfold-argument  \
    --Limit 1 \
    --Filters.0.Values rocketmq-1233 \
    --Filters.0.Name InstanceIds \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "abcdef",
        "Instances": [
            {
                "Status": 1,
                "PayMode": 1,
                "Remark": "test",
                "AutoRenewFlag": 1,
                "InstanceId": "rocketmq-1233",
                "NodeCount": 1,
                "ExpireTime": 1,
                "InstanceVersion": "4.9.3",
                "MaxStorage": 1,
                "MaxBandWidth": 1,
                "SpecName": "rocket-vip-basic-1",
                "ConfigDisplay": "基础型",
                "InstanceName": "abc",
                "MaxTps": 1
            }
        ]
    }
}
```

