**Example 1: 获取实例列表**



Input: 

```
tccli tdmq DescribePulsarProInstances --cli-unfold-argument  \
    --Filters.0.Name instancelds \
    --Filters.0.Values pulsar-aer8pde2z2we \
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
                "InstanceId": "pulsar-aer8pde2z2we",
                "InstanceName": "DevName",
                "InstanceVersion": "2.9.1",
                "Status": 1,
                "ConfigDisplay": "基础型",
                "MaxTps": 1,
                "MaxStorage": 1,
                "ExpireTime": 1,
                "AutoRenewFlag": 1,
                "PayMode": 1,
                "Remark": "devRemark",
                "SpecName": "vip-basic-1",
                "ScalableTps": 1,
                "VpcId": "vpc-xxxx",
                "SubnetId": "subnet-xxxx",
                "MaxBandWidth": 1,
                "Tags": [
                    {
                        "TagKey": "devKey",
                        "TagValue": "devValue"
                    }
                ],
                "CreateTime": "2023-12-08 10:25:51",
                "BillingLabelVersion": "PULSAR.P1"
            }
        ],
        "RequestId": "e83dfdba-ed1a-4460-b175-81430ddf61fa"
    }
}
```

