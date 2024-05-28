**Example 1: 获取Pulsar专业版集群实例详情**



Input: 

```
tccli tdmq DescribePulsarProInstanceDetail --cli-unfold-argument  \
    --ClusterId pulsar-test
```

Output: 
```
{
    "Response": {
        "ClusterInfo": {
            "ClusterId": "abc",
            "ClusterName": "abc",
            "Remark": "abc",
            "CreateTime": "abc",
            "Status": 0,
            "Version": "abc",
            "NodeDistribution": [
                {
                    "ZoneName": "abc",
                    "ZoneId": "abc",
                    "NodeCount": 1
                }
            ],
            "MaxStorage": 1,
            "CanEditRoute": true,
            "BillingLabelVersion": "abc"
        },
        "NetworkAccessPointInfos": [
            {
                "VpcId": "abc",
                "SubnetId": "abc",
                "Endpoint": "abc",
                "InstanceId": "abc",
                "RouteType": 1,
                "OperationType": 1,
                "AccessPointsType": "abc"
            }
        ],
        "ClusterSpecInfo": {
            "SpecName": "abc",
            "MaxTps": 1,
            "MaxBandWidth": 1,
            "MaxNamespaces": 1,
            "MaxTopics": 1,
            "ScalableTps": 1
        },
        "RequestId": "abc"
    }
}
```

