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
                "InstanceStatus": 3,
                "BoundNormal": 1,
                "VpcId": "vpc-sjdfb",
                "AutoRenewFlag": 0,
                "InstanceId": "prom-ajsh",
                "BoundTotal": 1,
                "ExpireTime": "2024-07-16 16:28:54",
                "SpecName": "spec-name",
                "InstanceChargeType": 2,
                "EnableGrafana": 0,
                "DataRetentionTime": 15,
                "GrafanaURL": "http://1.1.1.1:9000",
                "SubnetId": "subnet-ljeb",
                "InstanceName": "test-prom",
                "ChargeStatus": 1,
                "ResourcePackageStatus": 1,
                "ResourcePackageSpecName": "pkg-name"
            }
        ],
        "Total": 1,
        "RequestId": "sjehg-jdgrg"
    }
}
```

