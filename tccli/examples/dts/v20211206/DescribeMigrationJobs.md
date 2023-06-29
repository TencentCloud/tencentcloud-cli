**Example 1: 查询数据迁移任务列表**



Input: 

```
tccli dts DescribeMigrationJobs --cli-unfold-argument  \
    --JobId dts-amm1jw5q
```

Output: 
```
{
    "Response": {
        "JobList": [
            {
                "Action": {
                    "AllAction": [
                        "view",
                        "modify",
                        "check",
                        "start",
                        "configure",
                        "stop",
                        "complete",
                        "resume",
                        "createCmpTask",
                        "isolate",
                        "offline",
                        "resize",
                        "recover"
                    ],
                    "AllowedAction": [
                        "view",
                        "stop",
                        "complete",
                        "createCmpTask",
                        "view",
                        "isolate",
                        "resize"
                    ]
                },
                "CompareTask": {
                    "CompareTaskId": "dts-amm1jw5q-cmp-bmuum7jk",
                    "Status": "consistent"
                },
                "CreateTime": "2022-07-11 16:20:49",
                "DstInfo": {
                    "AccessType": "cdb",
                    "DatabaseType": "mysql",
                    "ExtraAttr": [],
                    "Info": [
                        {
                            "Account": "",
                            "AccountMode": "",
                            "AccountRole": "",
                            "CcnGwId": "",
                            "CvmInstanceId": "",
                            "DbKernel": "",
                            "EngineVersion": "",
                            "Host": "",
                            "InstanceId": "cdb-o7uph0cj",
                            "Password": "Rogerp@ssw0rd",
                            "Port": 0,
                            "Role": "",
                            "SubnetId": "",
                            "TmpSecretId": "",
                            "TmpSecretKey": "",
                            "TmpToken": "",
                            "UniqDcgId": "",
                            "UniqVpnGwId": "",
                            "User": "root",
                            "VpcId": ""
                        }
                    ],
                    "NodeType": "simple",
                    "Region": "ap-guangzhou",
                    "Supplier": ""
                },
                "EndTime": "0000-00-00 00:00:00",
                "ExpectRunTime": "",
                "JobId": "dts-amm1jw5q",
                "JobName": "test_config_api",
                "RunMode": "immediate",
                "SrcInfo": {
                    "AccessType": "intranet",
                    "DatabaseType": "mysql",
                    "ExtraAttr": [],
                    "Info": [
                        {
                            "Account": "",
                            "AccountMode": "",
                            "AccountRole": "",
                            "CcnGwId": "",
                            "CvmInstanceId": "",
                            "DbKernel": "",
                            "EngineVersion": "5.7",
                            "Host": "9.123.210.37",
                            "InstanceId": "",
                            "Password": "Rogerp@ssw0rd",
                            "Port": 31035,
                            "Role": "",
                            "SubnetId": "",
                            "TmpSecretId": "",
                            "TmpSecretKey": "",
                            "TmpToken": "",
                            "UniqDcgId": "",
                            "UniqVpnGwId": "",
                            "User": "root",
                            "VpcId": ""
                        }
                    ],
                    "NodeType": "simple",
                    "Region": "ap-guangzhou",
                    "Supplier": ""
                },
                "StartTime": "2022-07-11 17:20:56",
                "Status": "readyComplete",
                "Tags": [],
                "TradeInfo": {
                    "BillingType": "billing",
                    "DealName": "20220711715001047929481",
                    "ExpireTime": "0000-00-00 00:00:00",
                    "InstanceClass": "xlarge",
                    "IsolateReason": "",
                    "LastDealName": "",
                    "OfflineReason": "",
                    "PayType": "postpay",
                    "TradeStatus": "normal"
                },
                "UpdateTime": "2022-07-11 17:26:40"
            }
        ],
        "RequestId": "asdfadfasdfasdf",
        "TotalCount": 1
    }
}
```

