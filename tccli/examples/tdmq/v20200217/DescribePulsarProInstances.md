**Example 1: 获取实例列表**



Input: 

```
tccli tdmq DescribePulsarProInstances --cli-unfold-argument  \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Instances": [
            {
                "InstanceId": "abc",
                "InstanceName": "abc",
                "InstanceVersion": "abc",
                "Status": 1,
                "ConfigDisplay": "abc",
                "MaxTps": 1,
                "MaxStorage": 1,
                "ExpireTime": 1,
                "AutoRenewFlag": 1,
                "PayMode": 1,
                "Remark": "abc",
                "SpecName": "abc",
                "ScalableTps": 1,
                "VpcId": "abc",
                "SubnetId": "abc",
                "MaxBandWidth": 1,
                "Tags": [
                    {
                        "TagKey": "abc",
                        "TagValue": "abc"
                    }
                ],
                "CreateTime": "abc",
                "BillingLabelVersion": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

