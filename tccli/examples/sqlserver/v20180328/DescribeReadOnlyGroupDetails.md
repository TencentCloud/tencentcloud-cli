**Example 1: 查询查询只读组详情**



Input: 

```
tccli sqlserver DescribeReadOnlyGroupDetails --cli-unfold-argument  \
    --InstanceId mssql-6f4ddx2f \
    --ReadOnlyGroupId mssqlrg-552tyamb
```

Output: 
```
{
    "Response": {
        "IsOfflineDelay": 1,
        "MasterInstanceId": "mssql-6f4ddx2f",
        "MinReadOnlyInGroup": 1,
        "ReadOnlyGroupId": "mssqlrg-552tyamb",
        "ReadOnlyGroupName": "default_name",
        "ReadOnlyInstanceSet": [
            {
                "AccountDifference": "user1;user2;user3;user4",
                "Cpu": 1,
                "CreateTime": "2020-01-14 21:45:12",
                "DatabaseDifference": "db1;db2;db3;db4",
                "DelayTime": "0",
                "EndTime": "2020-01-16 10:53:13",
                "InstanceId": "mssqlro-5k508n7p",
                "IsolateTime": "2020-01-16 10:53:13",
                "Memory": 2,
                "Model": 2,
                "Name": "2f2d7800-4c38-4f1e-8522-7cc655763859",
                "PayMode": 1,
                "ProjectId": 1075687,
                "StartTime": "2020-01-14 21:45:12",
                "Status": 2,
                "Storage": 10,
                "SynStatus": "unknow",
                "Type": "TS85",
                "Uid": "gamedb.gz318.cdb.db",
                "UpdateTime": "2020-07-22 15:47:02",
                "Version": "2008R2",
                "Weight": 1
            },
            {
                "AccountDifference": "user1;user2;user3;user4",
                "Cpu": 1,
                "CreateTime": "2020-01-14 21:45:12",
                "DatabaseDifference": "db1;db2;db3;db4",
                "DelayTime": "0",
                "EndTime": "2020-06-01 10:53:12",
                "InstanceId": "mssqlro-91masbl1",
                "IsolateTime": "2020-01-16 10:53:12",
                "Memory": 2,
                "Model": 2,
                "Name": "8d8d8cdd-41fe-4095-9841-a9de01c499da",
                "PayMode": 1,
                "ProjectId": 1075687,
                "StartTime": "2020-01-14 21:45:12",
                "Status": 2,
                "Storage": 10,
                "SynStatus": "unknow",
                "Type": "TS85",
                "Uid": "gamedb.gz317.cdb.db",
                "UpdateTime": "2020-07-22 15:47:03",
                "Version": "2008R2",
                "Weight": 1
            }
        ],
        "ReadOnlyMaxDelayTime": 11,
        "RegionId": "ap-guangzhou",
        "RequestId": "62cba7ef-4441-4652-9787-2ba5d8f8b4af",
        "Status": 1,
        "SubnetId": "subnet-gdy95gfs",
        "Vip": "10.100.0.44",
        "VpcId": "vpc-3xq2t5al",
        "Vport": 1433,
        "ZoneId": "ap-guangzhou-2"
    }
}
```

