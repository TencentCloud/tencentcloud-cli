**Example 1: 获取实例列表**

获取实例列表

Input: 

```
tccli monitor DescribePrometheusInstancesOverview --cli-unfold-argument  \
    --Limit 1 \
    --Filters.0.Name Name \
    --Filters.0.Values alert-test \
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
                "VpcId": "xxx",
                "AutoRenewFlag": 0,
                "InstanceId": "xxx",
                "BoundTotal": 0,
                "ExpireTime": "xxx",
                "SpecName": "xxx",
                "InstanceChargeType": 0,
                "EnableGrafana": 0,
                "DataRetentionTime": 0,
                "GrafanaURL": "xxx",
                "SubnetId": "xxx",
                "InstanceName": "xxx",
                "ChargeStatus": 0,
                "ResourcePackageStatus": 1,
                "ResourcePackageSpecName": "fff"
            }
        ],
        "Total": 1,
        "RequestId": "xxx"
    }
}
```

