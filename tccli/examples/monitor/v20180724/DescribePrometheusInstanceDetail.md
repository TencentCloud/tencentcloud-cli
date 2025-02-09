**Example 1: 查询TMP实例详情**

查询TMP实例详情

Input: 

```
tccli monitor DescribePrometheusInstanceDetail --cli-unfold-argument  \
    --InstanceId prom-abc
```

Output: 
```
{
    "Response": {
        "InstanceId": "prom-skdfj",
        "InstanceName": "test-prom",
        "VpcId": "vpc-sjdh",
        "SubnetId": "subnet-kdhe",
        "InstanceStatus": 3,
        "ChargeStatus": 1,
        "EnableGrafana": 0,
        "GrafanaURL": "http://djeb:9000",
        "InstanceChargeType": 0,
        "SpecName": "name-sjdb",
        "DataRetentionTime": 15,
        "ExpireTime": "2024-07-16 16:28:54",
        "AutoRenewFlag": 0,
        "RequestId": "skdbfdi-akenfhl"
    }
}
```

