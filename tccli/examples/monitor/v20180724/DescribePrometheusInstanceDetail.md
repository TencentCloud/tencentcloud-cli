**Example 1: 查询TMP实例详情**

查询TMP实例详情

Input: 

```
tccli monitor DescribePrometheusInstanceDetail --cli-unfold-argument  \
    --InstanceId xx
```

Output: 
```
{
    "Response": {
        "InstanceStatus": 0,
        "VpcId": "xx",
        "AutoRenewFlag": 0,
        "InstanceId": "xx",
        "ExpireTime": "xx",
        "SpecName": "xx",
        "InstanceChargeType": 0,
        "RequestId": "xx",
        "EnableGrafana": 0,
        "DataRetentionTime": 0,
        "GrafanaURL": "xx",
        "SubnetId": "xx",
        "InstanceName": "xx",
        "ChargeStatus": 0
    }
}
```

