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
        "ClusterSpecInfo": {
            "MaxTopics": 1,
            "MaxNamespaces": 1,
            "SpecName": "xx",
            "MaxBandWidth": 1,
            "ScalableTps": 1,
            "MaxTps": 1
        },
        "NetworkAccessPointInfos": [
            {
                "SubnetId": "xx",
                "InstanceId": "xx",
                "Endpoint": "xx",
                "VpcId": "xx",
                "RouteType": 1
            }
        ],
        "ClusterInfo": {
            "Status": 0,
            "Remark": "xx",
            "NodeDistribution": [
                {
                    "NodeCount": 1,
                    "ZoneId": "xx",
                    "ZoneName": "xx"
                }
            ],
            "ClusterName": "xx",
            "ClusterId": "xx",
            "MaxStorage": 1,
            "Version": "xx",
            "CreateTime": "xx"
        },
        "RequestId": "xx"
    }
}
```

