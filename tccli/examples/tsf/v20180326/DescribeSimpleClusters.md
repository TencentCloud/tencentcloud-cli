**Example 1: 查询简单集群列表**



Input: 

```
tccli tsf DescribeSimpleClusters --cli-unfold-argument  \
    --Offset 0 \
    --Limit 50
```

Output: 
```
{
    "Response": {
        "RequestId": "73d633f3-1d91-443a-a5bb-b4d419a56721",
        "Result": {
            "TotalCount": 2,
            "Content": [
                {
                    "ClusterId": "cls-xxxxxxx",
                    "ClusterName": "示例",
                    "ClusterDesc": null,
                    "ClusterType": "C",
                    "VpcId": "vpc-xxxxxxx",
                    "CreateTime": null,
                    "UpdateTime": null,
                    "ClusterStatus": null,
                    "ClusterCIDR": null,
                    "ClusterTotalCpu": null,
                    "ClusterTotalMem": null,
                    "ClusterUsedCpu": null,
                    "ClusterUsedMem": null,
                    "ClusterLimitCpu": null,
                    "ClusterLimitMem": null,
                    "InstanceCount": null,
                    "RunInstanceCount": null,
                    "RunServiceInstanceCount": null,
                    "NormalInstanceCount": null,
                    "DeleteFlag": null,
                    "DeleteFlagReason": null,
                    "OperationInfo": null,
                    "TsfRegionId": null,
                    "TsfRegionName": null,
                    "TsfZoneId": null,
                    "TsfZoneName": null
                },
                {
                    "ClusterId": "cls-xxxxxxx",
                    "ClusterName": "示例",
                    "ClusterDesc": null,
                    "ClusterType": "C",
                    "VpcId": "vpc-xxxxxxx",
                    "CreateTime": null,
                    "UpdateTime": null,
                    "ClusterStatus": null,
                    "ClusterCIDR": null,
                    "ClusterTotalCpu": null,
                    "ClusterTotalMem": null,
                    "ClusterUsedCpu": null,
                    "ClusterUsedMem": null,
                    "ClusterLimitCpu": null,
                    "ClusterLimitMem": null,
                    "InstanceCount": null,
                    "RunInstanceCount": null,
                    "RunServiceInstanceCount": null,
                    "NormalInstanceCount": null,
                    "DeleteFlag": null,
                    "DeleteFlagReason": null,
                    "OperationInfo": null,
                    "TsfRegionId": null,
                    "TsfRegionName": null,
                    "TsfZoneId": null,
                    "TsfZoneName": null
                }
            ]
        }
    }
}
```

