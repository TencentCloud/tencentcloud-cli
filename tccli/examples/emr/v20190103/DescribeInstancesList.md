**Example 1: 查询实例详情**



Input: 

```
tccli emr DescribeInstancesList --cli-unfold-argument  \
    --Asc 0 \
    --DisplayStrategy clusterList \
    --Limit 10 \
    --OrderField clusterid \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCnt": 1,
        "InstancesList": [
            {
                "Zone": "xx",
                "IsMultiZoneCluster": true,
                "SubnetName": "xx",
                "Status": 1,
                "VpcId": 1,
                "AlarmInfo": "xx",
                "Tags": [
                    {
                        "TagKey": "xx",
                        "TagValue": "xx"
                    },
                    {
                        "TagKey": "xx",
                        "TagValue": "xx"
                    },
                    {
                        "TagKey": "xx",
                        "TagValue": "xx"
                    }
                ],
                "RegionId": 1,
                "ClusterId": "xx",
                "IsHandsCluster": true,
                "VpcName": "xx",
                "AddTime": "xx",
                "SubnetId": 1,
                "MasterIp": "xx",
                "ProjectId": 1,
                "ZoneId": 1,
                "StatusDesc": "xx",
                "ProductId": 1,
                "UniqVpcId": "xx",
                "ClusterName": "xx",
                "EmrVersion": "xx",
                "IsWoodpeckerCluster": 1,
                "UniqSubnetId": "xx",
                "ChargeType": 1,
                "AppId": 1,
                "ClusterClass": "xx",
                "RunTime": "xx",
                "Id": 1,
                "OutSideSoftInfo": [
                    {
                        "SoftName": "hdfs-2.8.5",
                        "Required": true
                    }
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```

