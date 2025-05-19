**Example 1: 获取实例列表**



Input: 

```
tccli tke DescribePrometheusInstancesOverview --cli-unfold-argument  \
    --Offset 1 \
    --Limit 1 \
    --Filters.0.Name abc \
    --Filters.0.Values abc
```

Output: 
```
{
    "Response": {
        "Instances": [
            {
                "InstanceId": "abc",
                "InstanceName": "abc",
                "VpcId": "abc",
                "SubnetId": "abc",
                "InstanceStatus": 0,
                "ChargeStatus": 0,
                "EnableGrafana": 0,
                "GrafanaURL": "abc",
                "InstanceChargeType": 0,
                "SpecName": "abc",
                "DataRetentionTime": 0,
                "ExpireTime": "abc",
                "AutoRenewFlag": 0,
                "BoundTotal": 0,
                "BoundNormal": 0
            }
        ],
        "Total": 1,
        "RequestId": "abc"
    }
}
```

