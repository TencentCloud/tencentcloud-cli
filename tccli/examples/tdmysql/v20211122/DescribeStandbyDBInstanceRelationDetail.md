**Example 1: DescribeStandbyDBinstanceRelations 实例**



Input: 

```
tccli tdmysql DescribeStandbyDBInstanceRelationDetail --cli-unfold-argument  \
    --InstanceIds tdsql3-da028619
```

Output: 
```
{
    "Response": {
        "RelationInfos": [
            {
                "ConnType": "log_service",
                "PrimaryInstanceId": "tdsql3-7a24fc49",
                "PrimaryInstanceName": "tdsql3-7a24fc49",
                "PrimaryRegion": "ap-chengdu",
                "PrimaryStatus": "running",
                "PrimaryVip": "192.168.1.76",
                "PrimaryVport": 3306,
                "PrimaryZones": [
                    "ap-chengdu-1"
                ],
                "SecondaryInstanceId": "tdsql3-af792643",
                "SecondaryInstanceName": "tdsql3-af792643",
                "SecondaryRegion": "ap-chengdu",
                "SecondaryStatus": "running",
                "SecondaryVip": "192.168.1.57",
                "SecondaryVport": 3306,
                "SecondaryZones": [
                    "ap-chengdu-1"
                ],
                "SyncMode": "async",
                "SyncStatus": 1,
                "SyncStatusDesc": ""
            }
        ],
        "RequestId": "abc"
    }
}
```

