**Example 1: 查询实例列表**



Input: 

```
tccli sqlserver DescribeDBInstances --cli-unfold-argument  \
    --ProjectId 0 \
    --InstanceIdSet mssql-3l3fgqn7 \
    --Status 2 \
    --Offset 0 \
    --Limit 3 \
    --PayMode 1 \
    --VpcId vpc-mknbt351 \
    --SubnetId subnet-f72hylo6
```

Output: 
```
{
    "Response": {
        "DBInstances": [
            {
                "BackupTime": "",
                "Cpu": 1,
                "CreateTime": "2019-06-19 11:59:52",
                "EndTime": "2019-09-20 23:15:06",
                "InstanceId": "mssql-3l3fgqn7",
                "IsolateTime": "0000-00-00 00:00:00",
                "Memory": 4,
                "Model": 1,
                "Name": "字符串",
                "PayMode": 1,
                "Pid": 10908,
                "ProjectId": 0,
                "Region": "ap-guangzhou",
                "RegionId": 1,
                "RenewFlag": 1,
                "StartTime": "2019-06-19 12:00:05",
                "Status": 2,
                "Storage": 10,
                "SubnetId": 3344,
                "Type": "TS85",
                "Uid": "gamedb.gz152.cdb.db",
                "UpdateTime": "2019-09-02 14:30:58",
                "UsedStorage": 0,
                "Version": "2008R2",
                "VersionName": "SQL Server 2008 Enterprise",
                "Vip": "",
                "VpcId": 14,
                "Vport": 1433,
                "Zone": "ap-guangzhou-2",
                "ZoneId": 100002,
                "UniqVpcId": "vpc-mknbt351",
                "UniqSubnetId": "subnet-f72hylo6"
            }
        ],
        "RequestId": "9c65fec1-8bce-4be9-b0fd-5f559553b546",
        "TotalCount": 1
    }
}
```

