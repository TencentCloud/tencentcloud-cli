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
                    "ClusterDesc": "desc",
                    "ClusterType": "C",
                    "VpcId": "vpc-6a79x94v",
                    "CreateTime": "2025",
                    "UpdateTime": "2025",
                    "ClusterStatus": "status",
                    "ClusterCIDR": "cidr",
                    "ClusterTotalCpu": 1,
                    "ClusterTotalMem": 2,
                    "ClusterUsedCpu": 1,
                    "ClusterUsedMem": 2,
                    "ClusterLimitCpu": 1,
                    "ClusterLimitMem": 2,
                    "InstanceCount": 1,
                    "RunInstanceCount": 1,
                    "RunServiceInstanceCount": 1,
                    "NormalInstanceCount": 1,
                    "DeleteFlag": false,
                    "DeleteFlagReason": "reason",
                    "OperationInfo": {
                        "AddInstance": {
                            "DisabledReason": "",
                            "Enabled": true,
                            "Supported": true
                        },
                        "Init": {
                            "DisabledReason": "",
                            "Enabled": true,
                            "Supported": true
                        },
                        "Destroy": {
                            "DisabledReason": "",
                            "Enabled": true,
                            "Supported": true
                        }
                    },
                    "TsfRegionId": "region-id",
                    "TsfRegionName": "name",
                    "TsfZoneId": "zone-id",
                    "TsfZoneName": "zone-name"
                }
            ]
        }
    }
}
```

