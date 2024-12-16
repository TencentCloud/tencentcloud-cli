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
                    "ClusterId": "cls-6a79x94v",
                    "ClusterVersion": "1.18",
                    "SubnetId": "subnet-6a79x94v",
                    "ClusterName": "示例",
                    "ClusterDesc": null,
                    "ClusterType": "C",
                    "VpcId": "vpc-6a79x94v",
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

