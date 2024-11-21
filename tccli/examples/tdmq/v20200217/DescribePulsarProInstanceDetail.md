**Example 1: 获取Pulsar专业版集群实例详情**



Input: 

```
tccli tdmq DescribePulsarProInstanceDetail --cli-unfold-argument  \
    --ClusterId pulsar-x4r939zkwmm2
```

Output: 
```
{
    "Response": {
        "ClusterInfo": {
            "ClusterId": "pulsar-x4r939zkwmm2",
            "ClusterName": "devTest",
            "Remark": "devTest",
            "CreateTime": "2023-07-20 10:35:17",
            "Status": 0,
            "Version": "2.9.2",
            "NodeDistribution": [
                {
                    "ZoneName": "ap-beijing-4",
                    "ZoneId": "800004",
                    "NodeCount": 1
                }
            ],
            "MaxStorage": 1,
            "CanEditRoute": true,
            "BillingLabelVersion": "PULSAR.P1"
        },
        "NetworkAccessPointInfos": [
            {
                "VpcId": "vpc-8jjua83u",
                "SubnetId": "subnet-1iia83y2",
                "Endpoint": "http://pulsar-x4r939zkwmm2.tdmq.ap-bj.qcloud.tencenttdmq.com:8080",
                "InstanceId": "pulsar-x4r939zkwmm2",
                "RouteType": 1,
                "OperationType": 1,
                "AccessPointsType": null
            }
        ],
        "ClusterSpecInfo": {
            "SpecName": "PULSAR.P1.MINI2",
            "MaxTps": 1,
            "MaxBandWidth": 1,
            "MaxNamespaces": 1,
            "MaxTopics": 1,
            "ScalableTps": 1
        },
        "RequestId": "0799dd77-707b-40d7-a4b5-4140b11f6c97"
    }
}
```

