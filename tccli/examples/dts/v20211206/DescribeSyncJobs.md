**Example 1: 查询同步任务列表**

查询同步任务列表

Input: 

```
tccli dts DescribeSyncJobs --cli-unfold-argument  \
    --JobId sync-bkm3mppi
```

Output: 
```
{
    "Response": {
        "JobList": [
            {
                "Actions": [
                    "configure",
                    "release",
                    "view"
                ],
                "AllActions": [
                    "view",
                    "configure",
                    "check",
                    "start",
                    "stop",
                    "release",
                    "resume"
                ],
                "CreateTime": "2022-01-05 10:40:57",
                "Detail": {
                    "CurrentStepProgress": -1,
                    "MasterSlaveDistance": -1,
                    "Message": "",
                    "Progress": 0,
                    "SecondsBehindMaster": -1,
                    "StepAll": 0,
                    "StepInfos": null,
                    "StepNow": 0
                },
                "DstAccessType": "",
                "DstDatabaseType": "mysql",
                "DstInfo": {
                    "Account": "",
                    "AccountMode": "",
                    "AccountRole": "",
                    "CcnId": "",
                    "CvmInstanceId": "",
                    "DbKernel": "",
                    "DbName": "",
                    "EngineVersion": "",
                    "Ip": "",
                    "Password": "",
                    "Port": 0,
                    "RoleExternalId": "",
                    "SubnetId": "",
                    "Supplier": "",
                    "TmpSecretId": "",
                    "TmpSecretKey": "",
                    "TmpToken": "",
                    "UniqDcgId": "",
                    "UniqVpnGwId": "",
                    "User": "",
                    "VpcId": ""
                },
                "DstRegion": "ap-guangzhou",
                "EndTime": "0000-00-00 00:00:00",
                "ExpectRunTime": "0000-00-00 00:00:00",
                "ExpireTime": "0000-00-00 00:00:00",
                "JobId": "sync-bkm3mppi",
                "JobName": "è·¨è´¦å<8f>·tdsql-mysql",
                "PayMode": "PostPay",
                "RunMode": "",
                "SrcAccessType": "",
                "SrcDatabaseType": "tdsqlmysql",
                "SrcInfo": {
                    "Account": "",
                    "AccountMode": "",
                    "AccountRole": "",
                    "CcnId": "",
                    "CvmInstanceId": "",
                    "DbKernel": "",
                    "DbName": "",
                    "EngineVersion": "",
                    "Ip": "",
                    "Password": "",
                    "Port": 0,
                    "RoleExternalId": "",
                    "SubnetId": "",
                    "Supplier": "",
                    "TmpSecretId": "",
                    "TmpSecretKey": "",
                    "TmpToken": "",
                    "UniqDcgId": "",
                    "UniqVpnGwId": "",
                    "User": "",
                    "VpcId": ""
                },
                "SrcRegion": "ap-guangzhou",
                "StartTime": "0000-00-00 00:00:00",
                "Status": "UnInitialized",
                "Tags": []
            }
        ],
        "RequestId": "23c18100-6df2-11ec-9c54-0dbb24194274",
        "TotalCount": 1
    }
}
```

