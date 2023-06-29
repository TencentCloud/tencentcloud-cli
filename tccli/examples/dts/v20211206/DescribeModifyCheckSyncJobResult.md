**Example 1: 查询修改对象校验任务的结果**

在创建修改对象校验任务后、查询校验任务的结果

Input: 

```
tccli dts DescribeModifyCheckSyncJobResult --cli-unfold-argument  \
    --JobId sync-xxsasa
```

Output: 
```
{
    "Response": {
        "Progress": 100,
        "RequestId": "00ba3080-f61d-11ed-926c-37ede6ab7ad5",
        "Status": "success",
        "StepCount": 15,
        "StepCur": 15,
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
                        "Message": "您的授权情况：GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, RELOAD, PROCESS, REFERENCES, INDEX, ALTER, SHOW DATABASES, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, REPLICATION SLAVE, REPLICATION CLIENT, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, CREATE USER, EVENT, TRIGGER, CREATE TABLESPACE, CREATE ROLE, DROP ROLE ON *.* TO `root`@`%` WITH GRANT OPTION,GRANT APPLICATION_PASSWORD_ADMIN,ROLE_ADMIN,SHOW_ROUTINE,XA_RECOVER_ADMIN ON *.* TO `root`@`%` WITH GRANT OPTION。 源端账号权限范围大于要求的账号权限范围，腾讯云DTS不会使用超过必要的权限，请按照最小化原则给与授权: https://cloud.tencent.com/document/product/571/58700",
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
                "Warnings": [
                    {
                        "Code": "Error: AdvancedStoreObjectCheck",
                        "HelpDoc": "",
                        "Message": "检测到进行了库表重命名，可能导致视图、函数，存储过程不能正常工作",
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
                "StepId": "ModifyConfigCheck",
                "StepName": "配置修改检查",
                "StepNo": 15,
                "Warnings": []
            }
        ]
    }
}
```

