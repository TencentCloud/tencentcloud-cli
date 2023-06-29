**Example 1: 查询迁移校验任务结果**



Input: 

```
tccli dts DescribeMigrationCheckJob --cli-unfold-argument  \
    --JobId dts-1ewjspuw
```

Output: 
```
{
    "Response": {
        "RequestId": "11d35c90-01bb-11ed-bad9-7b3bbe11abda",
        "CheckFlag": "checkPass",
        "BriefMsg": "success",
        "Status": "success",
        "StepInfo": [
            {
                "DetailCheckItems": [],
                "HasSkipped": false,
                "StepId": "ConnectDBCheck",
                "StepMessage": "",
                "StepName": "连接DB检查",
                "StepNo": 0,
                "StepStatus": "pass"
            },
            {
                "DetailCheckItems": [],
                "HasSkipped": false,
                "StepId": "VersionCheck",
                "StepMessage": "",
                "StepName": "版本检查",
                "StepNo": 1,
                "StepStatus": "pass"
            },
            {
                "DetailCheckItems": [
                    {
                        "CheckItemName": "源实例权限检查",
                        "CheckResult": "warning",
                        "Description": "",
                        "ErrorLog": [
                            "您的授权情况：GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, RELOAD, PROCESS, REFERENCES, INDEX, ALTER, SHOW DATABASES, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, REPLICATION SLAVE, REPLICATION CLIENT, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, CREATE USER, EVENT, TRIGGER, CREATE TABLESPACE ON *.* TO 'root'@'%' WITH GRANT OPTION。 源端账号权限范围大于要求的账号权限范围，腾讯云DTS不会使用超过必要的权限，请按照最小化原则给与授权: https://cloud.tencent.com/document/product/571/58700"
                        ],
                        "FailureReason": "",
                        "HelpDoc": [
                            ""
                        ],
                        "SkipInfo": "",
                        "Solution": ""
                    }
                ],
                "HasSkipped": false,
                "StepId": "SrcPrivilegeCheck",
                "StepMessage": "",
                "StepName": "源实例权限检查",
                "StepNo": 2,
                "StepStatus": "warning"
            },
            {
                "DetailCheckItems": [],
                "HasSkipped": false,
                "StepId": "SimpleParamCheck",
                "StepMessage": "",
                "StepName": "部分实例参数检查",
                "StepNo": 3,
                "StepStatus": "pass"
            },
            {
                "DetailCheckItems": [],
                "HasSkipped": false,
                "StepId": "DstPrivilegeCheck",
                "StepMessage": "",
                "StepName": "目标实例权限检查",
                "StepNo": 4,
                "StepStatus": "pass"
            },
            {
                "DetailCheckItems": [],
                "HasSkipped": false,
                "StepId": "DstEmptyCheck",
                "StepMessage": "",
                "StepName": "目标实例内容冲突检查",
                "StepNo": 5,
                "StepStatus": "pass"
            },
            {
                "DetailCheckItems": [],
                "HasSkipped": false,
                "StepId": "DstSpaceCheck",
                "StepMessage": "",
                "StepName": "目标实例空间检查",
                "StepNo": 6,
                "StepStatus": "pass"
            },
            {
                "DetailCheckItems": [],
                "HasSkipped": false,
                "StepId": "BinlogParamCheck",
                "StepMessage": "",
                "StepName": "binlog参数检查",
                "StepNo": 7,
                "StepStatus": "pass"
            },
            {
                "DetailCheckItems": [],
                "HasSkipped": false,
                "StepId": "ConstraintCheck",
                "StepMessage": "",
                "StepName": "外键依赖检查",
                "StepNo": 8,
                "StepStatus": "pass"
            },
            {
                "DetailCheckItems": [],
                "HasSkipped": false,
                "StepId": "ConstraintRefCheck",
                "StepMessage": "",
                "StepName": "外键部分库表依赖检查",
                "StepNo": 9,
                "StepStatus": "pass"
            },
            {
                "DetailCheckItems": [],
                "HasSkipped": false,
                "StepId": "ViewCheck",
                "StepMessage": "",
                "StepName": "视图检查",
                "StepNo": 10,
                "StepStatus": "pass"
            },
            {
                "DetailCheckItems": [],
                "HasSkipped": false,
                "StepId": "WarningParamCheck",
                "StepMessage": "",
                "StepName": "警告项检查",
                "StepNo": 11,
                "StepStatus": "pass"
            },
            {
                "DetailCheckItems": [
                    {
                        "CheckItemName": "周边检查",
                        "CheckResult": "warning",
                        "Description": "",
                        "ErrorLog": [
                            "skipped"
                        ],
                        "FailureReason": "",
                        "HelpDoc": [
                            ""
                        ],
                        "SkipInfo": "",
                        "Solution": ""
                    }
                ],
                "HasSkipped": true,
                "StepId": "OptimizeCheck",
                "StepMessage": "",
                "StepName": "周边检查",
                "StepNo": 12,
                "StepStatus": "failed"
            }
        ]
    }
}
```

