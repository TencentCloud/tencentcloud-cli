**Example 1: 查询校验任务结果**



Input: 

```
tccli dts DescribeCheckSyncJobResult --cli-unfold-argument  \
    --JobId sync-7r1cz016
```

Output: 
```
{
    "Response": {
        "Progress": 100,
        "RequestId": "972f5d3e-9144-4ce3-9825-980eccf549a9",
        "Status": "success",
        "StepCount": 12,
        "StepCur": 12,
        "StepInfos": [
            {
                "Errors": [],
                "Progress": 100,
                "StartTime": "",
                "Status": "finished",
                "StepId": "ConnectDBCheck",
                "StepName": "connect db check",
                "StepNo": 1,
                "Warnings": []
            },
            {
                "Errors": [],
                "Progress": 100,
                "StartTime": "",
                "Status": "finished",
                "StepId": "OptimizeCheck",
                "StepName": "necessary check",
                "StepNo": 2,
                "Warnings": []
            },
            {
                "Errors": [],
                "Progress": 100,
                "StartTime": "",
                "Status": "finished",
                "StepId": "VersionCheck",
                "StepName": "version check",
                "StepNo": 3,
                "Warnings": []
            },
            {
                "Errors": [],
                "Progress": 100,
                "StartTime": "",
                "Status": "finished",
                "StepId": "SrcPrivilegeCheck",
                "StepName": "source instance privilege check",
                "StepNo": 4,
                "Warnings": [
                    {
                        "Code": "Warning: SrcPrivilegeCheck",
                        "HelpDoc": "",
                        "Message": "Your grants is: GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, RELOAD, PROCESS, REFERENCES, INDEX, ALTER, SHOW DATABASES, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, REPLICATION SLAVE, REPLICATION CLIENT, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, CREATE USER, EVENT, TRIGGER, CREATE TABLESPACE ON *.* TO 'root'@'%' WITH GRANT OPTION. Tencent Cloud DTS don't need any privilege may modify your source instance data, suggest removing it based on minimization principle: https://cloud.tencent.com/document/product/571/13706",
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
                "StepName": "simpe instance param check",
                "StepNo": 5,
                "Warnings": []
            },
            {
                "Errors": [],
                "Progress": 100,
                "StartTime": "",
                "Status": "finished",
                "StepId": "DstPrivilegeCheck",
                "StepName": "target instance privilege check",
                "StepNo": 6,
                "Warnings": []
            },
            {
                "Errors": [],
                "Progress": 100,
                "StartTime": "",
                "Status": "finished",
                "StepId": "DstEmptyCheck",
                "StepName": "check if target instance has conflict content",
                "StepNo": 7,
                "Warnings": []
            },
            {
                "Errors": [],
                "Progress": 100,
                "StartTime": "",
                "Status": "finished",
                "StepId": "DstSpaceCheck",
                "StepName": "check if there's enough space in target instance",
                "StepNo": 8,
                "Warnings": []
            },
            {
                "Errors": [],
                "Progress": 100,
                "StartTime": "",
                "Status": "finished",
                "StepId": "BinlogParamCheck",
                "StepName": "source instance binlog param check",
                "StepNo": 9,
                "Warnings": []
            },
            {
                "Errors": [],
                "Progress": 100,
                "StartTime": "",
                "Status": "finished",
                "StepId": "ConstraintCheck",
                "StepName": "foreign key constraint check",
                "StepNo": 10,
                "Warnings": []
            },
            {
                "Errors": [],
                "Progress": 100,
                "StartTime": "",
                "Status": "finished",
                "StepId": "ViewCheck",
                "StepName": "view check",
                "StepNo": 11,
                "Warnings": []
            },
            {
                "Errors": [],
                "Progress": 100,
                "StartTime": "",
                "Status": "finished",
                "StepId": "WarningParamCheck",
                "StepName": "warning param check",
                "StepNo": 12,
                "Warnings": [
                    {
                        "Code": "Warn: WarningParamCheck",
                        "HelpDoc": "",
                        "Message": "Tables without primary key and unique key without any NULL columns have the risk of data duplication. Reference: https://cloud.tencent.com/document/product/571/58739",
                        "Solution": ""
                    },
                    {
                        "Code": "Error: WarningParamCheck",
                        "HelpDoc": "",
                        "Message": "Source instance would hold Flush Table With Read Lock for a short time, meanwhile, the MyISAM tables would be locked untill full dump finished. Current wait lock timeout is 70s. Error will be reported if lock can not be acquired within this time. Reference: https://cloud.tencent.com/document/product/571/58739",
                        "Solution": ""
                    }
                ]
            }
        ]
    }
}
```

