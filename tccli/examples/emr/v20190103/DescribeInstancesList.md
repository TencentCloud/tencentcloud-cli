**Example 1: 查询实例详情**



Input: 

```
tccli emr DescribeInstancesList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --OrderField clusterid \
    --Asc 0 \
    --DisplayStrategy clusterList
```

Output: 
```
{
    "Response": {
        "TotalCnt": 1,
        "InstancesList": [
            {
                "Zone": "xx",
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
                "RunTime": "xx",
                "Id": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

