**Example 1: 查询同步任务校验结果**

任务发起校验为异步操作，需要通过此接口查询同步任务校验结果

Input: 

```
tccli dts DescribeCheckSyncJobResult --cli-unfold-argument  \
    --JobId sync-bllmn8x9
```

Output: 
```
{
    "Response": {
        "Progress": 100,
        "RequestId": "948377d0-b8a2-11ed-b8ff-e9277ed2f336",
        "Status": "success",
        "StepCount": 14,
        "StepCur": 14,
        "StepInfos": [
            {
                "Errors": [],
                "Progress": 100,
                "StartTime": "",
                "Status": "finished",
                "StepId": "ConnectDBCheck",
                "StepName": "连接DB检查",
                "StepNo": 1,
                "Warnings": []
            },
            {
                "Errors": [],
                "Progress": 100,
                "StartTime": "",
                "Status": "finished",
                "StepId": "OptimizeCheck",
                "StepName": "周边检查",
                "StepNo": 2,
                "Warnings": []
            },
            {
                "Errors": [],
                "Progress": 100,
                "StartTime": "",
                "Status": "finished",
                "StepId": "VersionCheck",
                "StepName": "版本检查",
                "StepNo": 3,
                "Warnings": []
            },
            {
                "Errors": [],
                "Progress": 100,
                "StartTime": "",
                "Status": "finished",
                "StepId": "SrcPrivilegeCheck",
                "StepName": "源实例权限检查",
                "StepNo": 4,
                "Warnings": [
                    {
                        "Code": "Warning: SrcPrivilegeCheck",
                        "HelpDoc": "",
                        "Message": "您的授权情况：GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, RELOAD, PROCESS, REFERENCES, INDEX, ALTER, SHOW DATABASES, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, REPLICATION SLAVE, REPLICATION CLIENT, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, CREATE USER, EVENT, TRIGGER, CREATE TABLESPACE ON *.* TO 'root'@'%' WITH GRANT OPTION。 源端账号权限范围大于要求的账号权限范围，腾讯云DTS不会使用超过必要的权限，请按照最小化原则给与授权: https://cloud.tencent.com/document/product/571/58700",
                        "SkipInfo": "",
                        "Solution": ""
                    }
                ]
            },
            {
                "Errors": [],
                "Progress": 100,
                "StartTime": "",
                "Status": "finished",
                "StepId": "SimpleParamCheck",
                "StepName": "部分实例参数检查",
                "StepNo": 5,
                "Warnings": []
            },
            {
                "Errors": [],
                "Progress": 100,
                "StartTime": "",
                "Status": "finished",
                "StepId": "DstPrivilegeCheck",
                "StepName": "目标实例权限检查",
                "StepNo": 6,
                "Warnings": []
            },
            {
                "Errors": [],
                "Progress": 100,
                "StartTime": "",
                "Status": "finished",
                "StepId": "DstEmptyCheck",
                "StepName": "目标实例内容冲突检查",
                "StepNo": 7,
                "Warnings": []
            },
            {
                "Errors": [],
                "Progress": 100,
                "StartTime": "",
                "Status": "finished",
                "StepId": "DstSpaceCheck",
                "StepName": "目标实例空间检查",
                "StepNo": 8,
                "Warnings": []
            },
            {
                "Errors": [],
                "Progress": 100,
                "StartTime": "",
                "Status": "finished",
                "StepId": "BinlogParamCheck",
                "StepName": "binlog参数检查",
                "StepNo": 9,
                "Warnings": []
            },
            {
                "Errors": [],
                "Progress": 100,
                "StartTime": "",
                "Status": "finished",
                "StepId": "ConstraintCheck",
                "StepName": "外键依赖检查",
                "StepNo": 10,
                "Warnings": []
            },
            {
                "Errors": [],
                "Progress": 100,
                "StartTime": "",
                "Status": "finished",
                "StepId": "ConstraintRefCheck",
                "StepName": "外键部分库表依赖检查",
                "StepNo": 11,
                "Warnings": []
            },
            {
                "Errors": [],
                "Progress": 100,
                "StartTime": "",
                "Status": "finished",
                "StepId": "ViewCheck",
                "StepName": "视图检查",
                "StepNo": 12,
                "Warnings": []
            },
            {
                "Errors": [],
                "Progress": 100,
                "StartTime": "",
                "Status": "finished",
                "StepId": "WarningParamCheck",
                "StepName": "警告项检查",
                "StepNo": 13,
                "Warnings": [
                    {
                        "Code": "Warn: WarningParamCheck",
                        "HelpDoc": "",
                        "Message": "对于既没有主键、也没有不能为null的唯一键的表，有数据重复的风险。 请参考 https://cloud.tencent.com/document/product/571/58739",
                        "SkipInfo": "",
                        "Solution": ""
                    },
                    {
                        "Code": "Warn: WarningParamCheck",
                        "HelpDoc": "",
                        "Message": "源实例中sql_mode为 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION'， 目标实例中sql_mode为 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION'。建议设置为相同",
                        "SkipInfo": "",
                        "Solution": ""
                    }
                ]
            },
            {
                "Errors": [],
                "Progress": 100,
                "StartTime": "",
                "Status": "finished",
                "StepId": "AdvancedStoreObjectCheck",
                "StepName": "高级对象检查",
                "StepNo": 14,
                "Warnings": []
            }
        ]
    }
}
```

