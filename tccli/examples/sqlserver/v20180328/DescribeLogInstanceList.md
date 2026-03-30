**Example 1: 查询日志实例列表**



Input: 

```
tccli sqlserver DescribeLogInstanceList --cli-unfold-argument  \
    --LogType auditLog \
    --Limit 3 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "CreateAt": "",
                "Deliver": "",
                "DeliverSummary": null,
                "EnableQuery": "",
                "HighLogExpireDay": 0,
                "HighStorage": 0,
                "InstanceId": "mssql-m7v8e9k9",
                "InstanceInfo": {
                    "Architecture": "DOUBLE",
                    "AuditLogHosts": null,
                    "AuditLogStatus": "OFF",
                    "AuditLogStatusMessage": null,
                    "HAFlag": "ALWAYSON",
                    "InstanceId": "mssql-m7v8e9k9",
                    "InstanceName": "sqlsvr_auto_usage_20260314040300",
                    "InstanceType": "cvmHA",
                    "ProjectId": 0,
                    "ROFlag": "",
                    "Region": "ap-guangzhou",
                    "RegionId": 1,
                    "Status": 2,
                    "TagList": null,
                    "Type": "CLOUD_BSSD",
                    "Version": "2017",
                    "VersionName": "SQL Server 2017 Enterprise",
                    "Vip": "172.16.80.46",
                    "Vport": null,
                    "Zone": "ap-guangzhou-7",
                    "ZoneId": 100007
                },
                "LogExpireDay": 0,
                "LogStorage": 0,
                "LowLogExpireDay": 0,
                "LowStorage": 0,
                "Status": ""
            }
        ],
        "TotalCount": 38,
        "RequestId": "0fc9d9c5-0e51-422c-8f93-707670a9f41f"
    }
}
```

