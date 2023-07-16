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
        "TotalCnt": 0,
        "InstancesList": [
            {
                "ClusterId": "abc",
                "StatusDesc": "abc",
                "ClusterName": "abc",
                "ZoneId": 1,
                "AppId": 1,
                "AddTime": "abc",
                "RunTime": "abc",
                "MasterIp": "abc",
                "EmrVersion": "abc",
                "ChargeType": 1,
                "Id": 1,
                "ProductId": 1,
                "ProjectId": 1,
                "RegionId": 1,
                "SubnetId": 1,
                "VpcId": 1,
                "Zone": "abc",
                "Status": 1,
                "Tags": [
                    {
                        "TagKey": "abc",
                        "TagValue": "abc"
                    }
                ],
                "AlarmInfo": "abc",
                "IsWoodpeckerCluster": 1,
                "VpcName": "abc",
                "SubnetName": "abc",
                "UniqVpcId": "abc",
                "UniqSubnetId": "abc",
                "ClusterClass": "abc",
                "IsMultiZoneCluster": true,
                "IsHandsCluster": true,
                "OutSideSoftInfo": [
                    {
                        "SoftName": "abc",
                        "Required": true
                    }
                ],
                "IsSupportOutsideCluster": true
            }
        ],
        "RequestId": "abc"
    }
}
```

