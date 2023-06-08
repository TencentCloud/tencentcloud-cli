**Example 1: 查询指定主实例下只读组列表**

指定主实例ID（postgres-kpol3zgp）条件过滤查询只读组列表

Input: 

```
tccli postgres DescribeReadOnlyGroups --cli-unfold-argument  \
    --Filters.0.Name db-master-instance-id \
    --Filters.0.Values postgres-kpol3zgp
```

Output: 
```
{
    "Response": {
        "ReadOnlyGroupList": [
            {
                "DBInstanceNetInfo": [
                    {
                        "Address": "",
                        "Ip": "172.16.0.88",
                        "NetType": "private",
                        "Port": 5432,
                        "ProtocolType": "postgresql",
                        "Status": "opened",
                        "SubnetId": "subnet-7aheme8u",
                        "VpcId": "vpc-ql6jst9h"
                    }
                ],
                "MasterDBInstanceId": "postgres-kpol3zgp",
                "MaxReplayLag": 0,
                "MaxReplayLatency": 0,
                "MinDelayEliminateReserve": 0,
                "NetworkAccessList": null,
                "ProjectId": 1076910,
                "ReadOnlyDBInstanceList": [
                    {
                        "AppId": 251197262,
                        "AutoRenew": 0,
                        "CreateTime": "2023-05-17 15:24:26",
                        "DBCharset": "UTF8",
                        "DBEngine": "postgresql",
                        "DBEngineConfig": "",
                        "DBInstanceClass": "cdb.pg.sh1.2g",
                        "DBInstanceCpu": 1,
                        "DBInstanceId": "pgro-5objz9hu",
                        "DBInstanceMemory": 2,
                        "DBInstanceName": "auto_rotest",
                        "DBInstanceNetInfo": [
                            {
                                "Address": "",
                                "Ip": "172.16.0.134",
                                "NetType": "private",
                                "Port": 5432,
                                "ProtocolType": "postgresql",
                                "Status": "opened",
                                "SubnetId": "subnet-7aheme8u",
                                "VpcId": "vpc-ql6jst9h"
                            }
                        ],
                        "DBInstanceStatus": "running",
                        "DBInstanceStorage": 10,
                        "DBInstanceType": "readonly",
                        "DBInstanceVersion": "standard",
                        "DBKernelVersion": "v9.5.25_r1.5",
                        "DBMajorVersion": "9.5",
                        "DBNodeSet": null,
                        "DBVersion": "9.5.25",
                        "ExpireTime": "0000-00-00 00:00:00",
                        "IsSupportTDE": 0,
                        "IsolatedTime": "0000-00-00 00:00:00",
                        "MasterDBInstanceId": "postgres-kpol3zgp",
                        "NetworkAccessList": null,
                        "OfflineTime": "0001-01-04 00:00:00",
                        "PayType": "postpaid",
                        "ProjectId": 0,
                        "ReadOnlyInstanceNum": 0,
                        "Region": "ap-guangzhou",
                        "StatusInReadonlyGroup": "running",
                        "SubnetId": "subnet-7aheme8u",
                        "SupportIpv6": 0,
                        "TagList": [],
                        "Type": "SH02",
                        "Uid": 49,
                        "UpdateTime": "2023-05-17 07:25:35",
                        "VpcId": "vpc-ql6jst9h",
                        "Zone": "ap-guangzhou-3"
                    }
                ],
                "ReadOnlyGroupId": "pgrogrp-htrtddr0",
                "ReadOnlyGroupName": "autotest",
                "Rebalance": 0,
                "Region": "ap-guangzhou",
                "ReplayLagEliminate": 0,
                "ReplayLatencyEliminate": 0,
                "Status": "ok",
                "SubnetId": "subnet-7aheme8u",
                "VpcId": "vpc-ql6jst9h",
                "Zone": "ap-guangzhou-3"
            }
        ],
        "RequestId": "a28a102a-8c70-451c-96d7-04291218fbc1"
    }
}
```

