**Example 1: 查询实例列表**



Input: 

```
tccli sqlserver DescribeDBInstances --cli-unfold-argument  \
    --ProjectId 0 \
    --InstanceIdSet mssql-3l3fgqn7 \
    --Status 2 \
    --VipSet 172.1.0.12 \
    --InstanceNameSet 数仓 \
    --VersionSet 2008R2 \
    --Zone ap-guangzhou-2 \
    --TagKeys 测试tag \
    --Offset 0 \
    --Limit 3 \
    --PayMode 1 \
    --VpcId vpc-mknbt351 \
    --SubnetId subnet-f72hylo6 \
    --SearchKey 172.17.0.12
```

Output: 
```
{
    "Response": {
        "DBInstances": [
            {
                "BackupModel": "master_pkg",
                "BackupTime": "06:15:15",
                "Cpu": 1,
                "CreateTime": "2021-05-07 15:26:58",
                "EndTime": "0000-00-00 00:00:00",
                "HAFlag": "MIRROR",
                "InstanceId": "mssql-m0031jhf",
                "IsolateOperator": "",
                "IsolateTime": "0000-00-00 00:00:00",
                "Memory": 2,
                "Model": 1,
                "Name": "2008_1",
                "PayMode": 0,
                "Pid": 10908,
                "ProjectId": 0,
                "ROFlag": "",
                "Region": "ap-guangzhou",
                "RegionId": 1,
                "RenewFlag": 0,
                "ResourceTags": null,
                "StartTime": "2021-05-07 15:26:58",
                "Status": 2,
                "Storage": 10,
                "SubFlag": "",
                "SubnetId": 29802,
                "Type": "TS85",
                "Uid": "gamedb.gz570.cdb.db",
                "UniqSubnetId": "subnet-57pxp1bq",
                "UniqVpcId": "vpc-3p65tezp",
                "UpdateTime": "2021-05-07 16:56:15",
                "UsedStorage": 0,
                "Version": "2008R2",
                "VersionName": "SQL Server 2008 Enterprise",
                "Vip": "172.16.1.116",
                "VpcId": 206194,
                "Vport": 1433,
                "Zone": "ap-guangzhou-2",
                "ZoneId": 100002
            }
        ],
        "RequestId": "de641788-0565-4617-a7f4-639de128772b",
        "TotalCount": 1
    }
}
```

