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
                "GrafanaInstanceId": "grafana-as2sad2",
                "AuthToken": "zh32ksa~wq(a",
                "RecordingRuleLimit": 0,
                "VpcId": "vpcID",
                "SubnetId": "subnetid",
                "MigrationType": 0,
                "IPv4Address": "",
                "RemoteWrite": "http://10.0.16.63:9090/api/v1/prom/write",
                "DataRetentionTime": 30,
                "EnableGrafana": 0,
                "ExpireTime": "2020-07-07T10:39:18Z",
                "SpecName": "共享版",
                "Grant": {
                    "HasChargeOperation": 0,
                    "HasVpcDisplay": 0,
                    "HasGrafanaStatusChange": 0,
                    "HasAgentManage": 0,
                    "HasTkeManage": 0,
                    "HasApiOperation": 0
                },
                "ProxyAddress": "10.0.16.63:9090",
                "IsNearExpire": 0,
                "GrafanaStatus": 0,
                "GrafanaIpWhiteList": "",
                "ApiRootPath": "10.0.16.63:9090",
                "TagSpecification": [
                    {
                        "Key": "creator",
                        "Value": "tmp"
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

