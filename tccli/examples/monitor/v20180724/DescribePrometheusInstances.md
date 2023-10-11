**Example 1: 查看 Prometheus 实例列表**



Input: 

```
tccli monitor DescribePrometheusInstances --cli-unfold-argument  \
    --InstanceIds prom-ncxkwqr8
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "InstanceSet": [
            {
                "InstanceName": "name",
                "InstanceChargeType": 1,
                "InstanceId": "prom-xxxxx",
                "InstanceStatus": 1,
                "RegionId": 1,
                "Zone": "ap-guangzhou-1",
                "GrafanaInstanceId": "abc",
                "AuthToken": "abc",
                "RecordingRuleLimit": 0,
                "VpcId": "vpcID",
                "SubnetId": "subnetid",
                "MigrationType": 0,
                "IPv4Address": "",
                "RemoteWrite": "abc",
                "DataRetentionTime": 30,
                "EnableGrafana": 0,
                "ExpireTime": "abc",
                "SpecName": "abc",
                "Grant": {
                    "HasChargeOperation": 0,
                    "HasVpcDisplay": 0,
                    "HasGrafanaStatusChange": 0,
                    "HasAgentManage": 0,
                    "HasTkeManage": 0,
                    "HasApiOperation": 0
                },
                "ProxyAddress": "abc",
                "IsNearExpire": 0,
                "GrafanaStatus": 0,
                "GrafanaIpWhiteList": "abc",
                "ApiRootPath": "abc",
                "TagSpecification": [
                    {
                        "Key": "abc",
                        "Value": "abc"
                    }
                ],
                "AutoRenewFlag": 0,
                "AlertRuleLimit": 0,
                "ChargeStatus": 0,
                "GrafanaURL": "",
                "CreatedAt": "2020-07-07T10:39:18Z"
            }
        ],
        "RequestId": "3e0dff9d-9ed5-47c3-beb2-a42c1d69e1cc"
    }
}
```

