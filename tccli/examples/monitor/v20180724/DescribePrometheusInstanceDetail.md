**Example 1: 查询TMP实例详情**

查询TMP实例详情

Input: 

```
tccli monitor DescribePrometheusInstanceDetail --cli-unfold-argument  \
    --InstanceId abc
```

Output: 
```
{
    "Response": {
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
        "RequestId": "abc"
    }
}
```

