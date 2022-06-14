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
                        "DBNodeSet": [
                            {
                                "Role": "xx",
                                "Zone": "xx"
                            }
                        ],
                        "Type": "xx",
                        "ReadOnlyInstanceNum": 0,
                        "DBKernelVersion": "xx",
                        "UpdateTime": "2020-09-22 00:00:00",
                        "VpcId": "xx",
                        "DBMajorVersion": "xx",
                        "IsolatedTime": "2020-09-22 00:00:00",
                        "NetworkAccessList": [
                            {
                                "Vip6": "xx",
                                "VpcId": "xx",
                                "ResourceType": 1,
                                "ResourceId": "xx",
                                "Vip": "xx",
                                "SubnetId": "xx",
                                "Vport": 0,
                                "VpcStatus": 0
                            }
                        ],
                        "DBVersion": "xx",
                        "DBInstanceVersion": "xx",
                        "AutoRenew": 1,
                        "OfflineTime": "xx",
                        "SubnetId": "xx",
                        "DBInstanceMemory": 1,
                        "DBInstanceType": "xx",
                        "DBInstanceStatus": "xx",
                        "ProjectId": 1,
                        "Region": "xx",
                        "StatusInReadonlyGroup": "xx",
                        "MasterDBInstanceId": "xx",
                        "DBInstanceNetInfo": [
                            {
                                "Status": "xx",
                                "VpcId": "xx",
                                "Ip": "xx",
                                "NetType": "xx",
                                "Address": "xx",
                                "SubnetId": "xx",
                                "Port": 1
                            }
                        ],
                        "DBInstanceStorage": 1,
                        "Uid": 1,
                        "IsSupportTDE": 0,
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
                "NetworkAccessList": [
                    {
                        "Vip6": "xx",
                        "VpcId": "xx",
                        "ResourceType": 1,
                        "ResourceId": "xx",
                        "Vip": "xx",
                        "SubnetId": "xx",
                        "Vport": 0,
                        "VpcStatus": 0
                    }
                ],
                "Rebalance": 0,
                "DBInstanceNetInfo": [
                    {
                        "Status": "xx",
                        "VpcId": "xx",
                        "Ip": "xx",
                        "NetType": "xx",
                        "Address": "xx",
                        "SubnetId": "xx",
                        "Port": 1
                    }
                ]
            }
        ]
    }
}
```

