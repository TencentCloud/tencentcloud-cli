**Example 1: 获取实例列表**

获取实例列表

Input: 

```
tccli monitor DescribePrometheusInstancesOverview --cli-unfold-argument  \
    --Limit 1 \
    --Filters.0.Type xx \
    --Filters.0.Key xx \
    --Filters.0.Value xx \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "Instances": [
            {
                "InstanceStatus": 0,
                "BoundNormal": 0,
                "VpcId": "xx",
                "AutoRenewFlag": 0,
                "InstanceId": "xx",
                "BoundTotal": 0,
                "ExpireTime": "xx",
                "SpecName": "xx",
                "InstanceChargeType": 0,
                "EnableGrafana": 0,
                "DataRetentionTime": 0,
                "GrafanaURL": "xx",
                "SubnetId": "xx",
                "InstanceName": "xx",
                "ChargeStatus": 0
            }
        ],
        "Total": 1,
        "RequestId": "xx"
    }
}
```

