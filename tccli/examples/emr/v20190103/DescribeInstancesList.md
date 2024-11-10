**Example 1: 查询实例详情**

查询实例详情

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
        "InstancesList": [
            {
                "AddTime": "2024-11-04 15:54:58",
                "AlarmInfo": "",
                "AppId": 11111,
                "ChargeType": 1,
                "ClusterClass": "Hadoop",
                "ClusterId": "emr-111",
                "ClusterName": "EMR-1111",
                "EmrVersion": "",
                "Id": 1016390,
                "IsDedicatedCluster": false,
                "IsHandsCluster": false,
                "IsMultiZoneCluster": false,
                "IsSupportOutsideCluster": true,
                "IsWoodpeckerCluster": 1,
                "MasterIp": "--",
                "OutSideSoftInfo": [
                    {
                        "Required": true,
                        "SoftName": "hdfs-3.2.2"
                    },
                    {
                        "Required": true,
                        "SoftName": "yarn-3.2.2"
                    },
                    {
                        "Required": false,
                        "SoftName": "hive-3.1.3"
                    },
                    {
                        "Required": false,
                        "SoftName": "hbase-2.4.5"
                    },
                    {
                        "Required": false,
                        "SoftName": "spark-3.2.2"
                    }
                ],
                "ProductId": 44,
                "ProjectId": 1325150,
                "RegionId": 1,
                "RunTime": "1天5小时24分钟6秒",
                "Status": 2,
                "StatusDesc": "集群运行中",
                "SubnetId": 6059972,
                "SubnetName": "zefa-111",
                "Tags": [
                    {
                        "TagKey": "tke-111",
                        "TagValue": "cos-111"
                    }
                ],
                "UniqSubnetId": "subnet-pan0t01q",
                "UniqVpcId": "vpc-hitz5lsz",
                "VpcId": 10412940,
                "VpcName": "zefa-111",
                "Zone": "ap-guangzhou-7",
                "ZoneId": 100007
            }
        ],
        "RequestId": "3664d030-623c-40fb-bf19-f69a2d58dfe2",
        "TotalCnt": 1
    }
}
```

