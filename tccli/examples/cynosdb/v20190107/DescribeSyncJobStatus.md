**Example 1: 查询同步任务状态**

查询同步任务状态

Input: 

```
tccli cynosdb DescribeSyncJobStatus --cli-unfold-argument  \
    --SrcClusterId cynosdbmysql-a289dag1 \
    --DstClusterId cynosdbmysql-ixf5jckr
```

Output: 
```
{
    "Response": {
        "DtsJobId": "sync-2im0oo9a",
        "ErrInfo": {
            "Message": "连接源或者目标实例出现网络错误。",
            "Reason": "dial tcp : i/o timeout",
            "Solution": "请检查是否存在以上情况并解决。"
        },
        "MasterSlaveDistance": -1,
        "RequestId": "48b7cd8a-f6dd-4e47-a78a-dragon",
        "SecondsBehindMaster": -1,
        "Status": "ResumableErr",
        "StepInfos": [
            {
                "Errors": [],
                "Progress": 100,
                "Status": "finished",
                "StepId": "ConnectDBCheck",
                "StepName": "连接DB检查",
                "StepNo": 1,
                "Warnings": []
            },
            {
                "Errors": [],
                "Progress": 100,
                "Status": "finished",
                "StepId": "OptimizeCheck",
                "StepName": "周边检查",
                "StepNo": 2,
                "Warnings": []
            },
            {
                "Errors": [],
                "Progress": 100,
                "Status": "finished",
                "StepId": "VersionCheck",
                "StepName": "版本检查",
                "StepNo": 3,
                "Warnings": []
            },
            {
                "Errors": [],
                "Progress": 100,
                "Status": "finished",
                "StepId": "SrcPrivilegeCheck",
                "StepName": "源实例权限检查",
                "StepNo": 4,
                "Warnings": []
            },
            {
                "Errors": [],
                "Progress": 100,
                "Status": "finished",
                "StepId": "SimpleParamCheck",
                "StepName": "部分实例参数检查",
                "StepNo": 5,
                "Warnings": []
            },
            {
                "Errors": [],
                "Progress": 100,
                "Status": "finished",
                "StepId": "DstPrivilegeCheck",
                "StepName": "目标实例权限检查",
                "StepNo": 6,
                "Warnings": [
                    {
                        "Code": "Warning: DstPrivilegeCheck",
                        "ExtraInfo": "",
                        "HelpDoc": "",
                        "Message": "修改目标库session级别innodb_strict_mode参数为OFF失败，错误信息详情 failed to run query SET innodb_strict_mode = OFF;, err: Error 1227: Access denied; you need (at least one of) the SYSTEM_VARIABLES_ADMIN or SESSION_VARIABLES_ADMIN privilege(s) for this operation 。如果innodb_strict_mode参数为ON，在目标库重放不标准的 DDL（CREATE TABLE 和 ALTER TABLE）时，可能导致任务中断",
                        "Solution": "尝试以下方式后重新校验：\n 1、登录目标数据库，修改目标库innodb_strict_mode参数为OFF，并且在任务运行中保持innodb_strict_mode参数不变 \n请确保有权限做上述调整。"
                    }
                ]
            },
            {
                "Errors": [],
                "Progress": 100,
                "Status": "finished",
                "StepId": "DstEmptyCheck",
                "StepName": "目标实例内容冲突检查",
                "StepNo": 7,
                "Warnings": []
            },
            {
                "Errors": [],
                "Progress": 100,
                "Status": "finished",
                "StepId": "DstSpaceCheck",
                "StepName": "目标实例空间检查",
                "StepNo": 8,
                "Warnings": []
            },
            {
                "Errors": [],
                "Progress": 100,
                "Status": "finished",
                "StepId": "BinlogParamCheck",
                "StepName": "binlog参数检查",
                "StepNo": 9,
                "Warnings": []
            },
            {
                "Errors": [],
                "Progress": 100,
                "Status": "finished",
                "StepId": "ConstraintCheck",
                "StepName": "外键依赖检查",
                "StepNo": 10,
                "Warnings": []
            },
            {
                "Errors": [],
                "Progress": 100,
                "Status": "finished",
                "StepId": "ConstraintRefCheck",
                "StepName": "外键部分库表依赖检查",
                "StepNo": 11,
                "Warnings": []
            },
            {
                "Errors": [],
                "Progress": 100,
                "Status": "finished",
                "StepId": "ViewCheck",
                "StepName": "视图检查",
                "StepNo": 12,
                "Warnings": []
            },
            {
                "Errors": [],
                "Progress": 100,
                "Status": "finished",
                "StepId": "WarningParamCheck",
                "StepName": "警告项检查",
                "StepNo": 13,
                "Warnings": [
                    {
                        "Code": "Warn: WarningParamCheck",
                        "ExtraInfo": "",
                        "HelpDoc": "",
                        "Message": "对于既没有主键、也没有不能为null的唯一键的表，有数据重复的风险。 请参考 https://cloud.tencent.com/document/product/571/58739",
                        "Solution": ""
                    },
                    {
                        "Code": "Warning: WarningParamCheck",
                        "ExtraInfo": "",
                        "HelpDoc": "警告项检查: cloud.tencent.com/document/product/571/58739",
                        "Message": "请在任务运行中保持explicit_defaults_for_timestamp参数不变；修改该参数(包括session级别)可能导致表结构不一致。",
                        "Solution": ""
                    },
                    {
                        "Code": "Warn: WarningParamCheck",
                        "ExtraInfo": "",
                        "HelpDoc": "",
                        "Message": "到目标实例网络延迟较高(35.162ms)，可能会影响 DTS 同步数据的性能",
                        "Solution": ""
                    }
                ]
            }
        ]
    }
}
```

