**Example 1: 查询数据迁移任务**



Input: 

```
tccli dts DescribeMigrateJobs --cli-unfold-argument  \
    --Order CreateTime \
    --OrderSeq DESC \
    --Offset 0 \
    --Limit 2
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "JobList": [
            {
                "JobId": "dts-1kl0iy0v",
                "JobName": "userdts",
                "MigrateOption": {
                    "RunMode": 1,
                    "ExpectTime": "0000-00-00 00:00:00",
                    "MigrateType": 2,
                    "MigrateObject": 2,
                    "ConsistencyType": 5,
                    "IsOverrideRoot": 0,
                    "ExternParams": "[]",
                    "ConsistencyParams": {
                        "SelectRowsPerTable": 0,
                        "TablesSelectAll": 0,
                        "TablesSelectCount": 0
                    }
                },
                "SrcAccessType": "extranet",
                "SrcDatabaseType": "mysql",
                "SrcInfo": {
                    "AccessKey": "",
                    "Ip": "9.18.84.24",
                    "Port": 10304,
                    "User": "root",
                    "Password": "",
                    "RdsInstanceId": "",
                    "CvmInstanceId": "",
                    "UniqDcgId": "",
                    "SubnetId": "",
                    "UniqVpnGwId": "",
                    "InstanceId": "",
                    "Region": "ap-guangzhou",
                    "VpcId": ""
                },
                "DstAccessType": "cdb",
                "DstDatabaseType": "mysql",
                "DstInfo": {
                    "InstanceId": "cdb-l78e0nbv",
                    "Ip": "",
                    "Port": 0,
                    "Region": "ap-shanghai",
                    "ReadOnly": 0
                },
                "Tags": [
                    {
                        "TagKey": "负责人",
                        "TagValue": "alice"
                    }
                ],
                "Detail": {
                    "StepAll": 0,
                    "StepNow": 0,
                    "Progress": "0",
                    "CurrentStepProgress": "0",
                    "MasterSlaveDistance": 0,
                    "SecondsBehindMaster": 0,
                    "StepInfo": []
                },
                "Status": 1,
                "DatabaseInfo": "[]",
                "CreateTime": "2018-05-24 15:06:03",
                "StartTime": "0000-00-00 00:00:00",
                "EndTime": "0000-00-00 00:00:00",
                "ErrorInfo": []
            }
        ],
        "RequestId": "c032aab5-b56a-428d-9cf7-e5f324ee408b"
    }
}
```

