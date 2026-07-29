**Example 1: 查询实例列表**



Input: 

```
tccli tdata DescribeInstances --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --OrderBy CREATETIME \
    --OrderByType DESC \
    --Filters.0.Name InstanceId \
    --Filters.0.Values ora-fsv1gq23
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "AppId": 1251006373,
                "AutoRenewFlag": 2,
                "BackupSize": 1500,
                "Capacity": 1000,
                "Cpu": 14,
                "CreateTime": "2018-09-27 17:45:37",
                "DbName": "SZJRT",
                "InstanceId": "ora-fsv1gq23",
                "InstanceName": "newName",
                "InstanceNum": 3,
                "Memory": 64,
                "OracleVersion": "12.1.0.2",
                "PayMode": 1,
                "PeriodEndTime": "2018-10-28 20:13:05",
                "ProjectId": 120002,
                "Region": "ap-guangzhou",
                "ServiceName": "SZJRT",
                "Status": "running",
                "StatusDesc": "运行中",
                "SubnetId": "subnet-o3p3evv4",
                "Type": "high performance",
                "Uin": "20548499",
                "UpdateTime": "2018-10-31 17:51:12",
                "Vip": "172.16.32.22",
                "VpcId": "vpc-kppg4pm1",
                "Vport": 1521,
                "Zone": "ap-guangzhou-1"
            }
        ],
        "RequestId": "7eeb8929-bbee-4dda-9d31-0f6da57a7a51",
        "TotalCount": 1
    }
}
```

