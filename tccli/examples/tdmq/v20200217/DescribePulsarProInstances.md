**Example 1: 获取实例列表**



Input: 

```
tccli tdmq DescribePulsarProInstances --cli-unfold-argument  \
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
                "VpcId": "xx",
                "AutoRenewFlag": 1,
                "InstanceId": "xx",
                "ScalableTps": 1,
                "ExpireTime": 1,
                "InstanceVersion": "xx",
                "MaxStorage": 1,
                "SpecName": "xx",
                "ConfigDisplay": "xx",
                "SubnetId": "xx",
                "InstanceName": "xx",
                "MaxTps": 1
            }
        ]
    }
}
```

