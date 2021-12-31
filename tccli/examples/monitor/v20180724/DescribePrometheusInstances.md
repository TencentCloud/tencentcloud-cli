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
                "VpcId": "vpcID",
                "SubnetId": "subnetid",
                "IPv4Address": "",
                "DataRetentionTime": 30,
                "EnableGrafana": 0,
                "GrafanaURL": "",
                "CreatedAt": "2020-07-07T10:39:18Z"
            }
        ],
        "RequestId": "3e0dff9d-9ed5-47c3-beb2-a42c1d69e1cc"
    }
}
```

