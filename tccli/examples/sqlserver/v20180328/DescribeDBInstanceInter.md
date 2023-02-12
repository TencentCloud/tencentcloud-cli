**Example 1: 查询实例在互通组中的状态**

查询实例在互通组中的状态，内网互通ip用于在SSIS服务中使用。

Input: 

```
tccli sqlserver DescribeDBInstanceInter --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --InstanceId mssqlbi-q1atet3b
```

Output: 
```
{
    "Response": {
        "InterInstanceSet": [
            {
                "InstanceId": "mssql-30vft2ix",
                "InterPort": 1028,
                "InterVip": "192.168.0.1",
                "Name": "xxx",
                "Region": "ap-guangzhou",
                "Status": 1,
                "Version": "2012SP3",
                "VersionName": "SQL Server 2012 Enterprise",
                "Vip": "192.168.0.2",
                "Vport": 1433,
                "Zone": "ap-guangzhou-3"
            },
            {
                "InstanceId": "mssql-iqnuxv3j",
                "InterPort": 1026,
                "InterVip": "192.168.0.1",
                "Name": "xxxx",
                "Region": "ap-guangzhou",
                "Status": 1,
                "Version": "2017",
                "VersionName": "SQL Server 2017 Enterprise",
                "Vip": "192.168.0.2",
                "Vport": 1433,
                "Zone": "ap-guangzhou-3"
            },
            {
                "InstanceId": "mssql-ngc6786l",
                "InterPort": 1029,
                "InterVip": "192.168.0.1",
                "Name": "xxxx",
                "Region": "ap-guangzhou",
                "Status": 1,
                "Version": "2008R2",
                "VersionName": "SQL Server 2008 Enterprise",
                "Vip": "192.168.0.2",
                "Vport": 1433,
                "Zone": "ap-guangzhou-3"
            }
        ],
        "RequestId": "ff9c5a56-1d33-4707-b656-a715240635ad",
        "TotalCount": 3
    }
}
```

