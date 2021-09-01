**Example 1: 查询postgres-6bwgamo3实例下只读组详情**



Input: 

```
tccli postgres DescribeReadOnlyGroups --cli-unfold-argument  \
    --PageSize 10 \
    --PageNumber 0 \
    --OrderBy Name \
    --OrderByType desc \
    --Filters.0.Name db-master-instance-id \
    --Filters.0.Values postgres-6bwgamo3
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "ReadOnlyGroupList": [
            {
                "Status": "xx",
                "MaxReplayLag": 0.0,
                "ReplayLagEliminate": 1,
                "Zone": "xx",
                "MaxReplayLatency": 0,
                "ProjectId": 1,
                "Region": "xx",
                "ReadOnlyDBInstanceList": [
                    {
                        "Zone": "xx",
                        "DBInstanceName": "xx",
                        "Type": "xx",
                        "ReadOnlyInstanceNum": 0,
                        "UpdateTime": "2020-09-22 00:00:00",
                        "VpcId": "xx",
                        "IsolatedTime": "2020-09-22 00:00:00",
                        "DBVersion": "xx",
                        "DBInstanceVersion": "xx",
                        "AutoRenew": 1,
                        "StatusInReadonlyGroup": "xx",
                        "SubnetId": "xx",
                        "DBInstanceMemory": 1,
                        "DBInstanceType": "xx",
                        "DBInstanceStatus": "xx",
                        "ProjectId": 1,
                        "Region": "xx",
                        "MasterDBInstanceId": "xx",
                        "DBInstanceNetInfo": [
                            {
                                "Status": "xx",
                                "Ip": "xx",
                                "Port": 1,
                                "NetType": "xx",
                                "Address": "xx"
                            }
                        ],
                        "DBInstanceStorage": 1,
                        "Uid": 1,
                        "DBCharset": "xx",
                        "DBInstanceId": "xx",
                        "PayType": "xx",
                        "ExpireTime": "2020-09-22 00:00:00",
                        "SupportIpv6": 1,
                        "AppId": 1,
                        "DBInstanceClass": "xx",
                        "CreateTime": "2020-09-22 00:00:00",
                        "DBInstanceCpu": 1,
                        "TagList": [
                            {
                                "TagKey": "xx",
                                "TagValue": "xx"
                            }
                        ]
                    }
                ],
                "MasterDBInstanceId": "xx",
                "MinDelayEliminateReserve": 3,
                "ReadOnlyGroupName": "xx",
                "VpcId": "xx",
                "ReadOnlyGroupId": "xx",
                "ReplayLatencyEliminate": 0,
                "SubnetId": "xx",
                "Rebalance": 0,
                "DBInstanceNetInfo": [
                    {
                        "Status": "xx",
                        "Ip": "xx",
                        "Port": 1,
                        "NetType": "xx",
                        "Address": "xx"
                    }
                ]
            }
        ]
    }
}
```

