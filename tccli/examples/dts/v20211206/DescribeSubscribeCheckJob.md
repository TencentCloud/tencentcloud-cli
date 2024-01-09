**Example 1: 查询订阅校验任务结果**

查询订阅校验任务结果

Input: 

```
tccli dts DescribeSubscribeCheckJob --cli-unfold-argument  \
    --SubscribeId subs-l4d3a7izai
```

Output: 
```
{
    "Response": {
        "Message": "success",
        "Progress": 100,
        "RequestId": "b048a800-f2fe-11ed-a211-5df19a912eab",
        "Status": "success",
        "StepAll": 5,
        "StepNow": 5,
        "Steps": [
            {
                "Errors": [],
                "Percent": 100,
                "Status": "finished",
                "StepId": "ConnectDBCheck",
                "StepName": "连接DB检查",
                "StepNo": 1,
                "Warnings": []
            },
            {
                "Errors": [],
                "Percent": 100,
                "Status": "finished",
                "StepId": "OptimizeCheck",
                "StepName": "周边检查",
                "StepNo": 2,
                "Warnings": []
            },
            {
                "Errors": [],
                "Percent": 100,
                "Status": "finished",
                "StepId": "VersionCheck",
                "StepName": "版本检查",
                "StepNo": 3,
                "Warnings": []
            },
            {
                "Errors": [],
                "Percent": 100,
                "Status": "finished",
                "StepId": "SrcPrivilegeCheck",
                "StepName": "源实例权限检查",
                "StepNo": 4,
                "Warnings": [
                    {
                        "HelpDoc": "",
                        "Message": "我们不需要能修改您源端数据的权限，请取消他们。例如，您的授权情况：GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, RELOAD, PROCESS, REFERENCES, INDEX, ALTER, SHOW DATABASES, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, REPLICATION SLAVE, REPLICATION CLIENT, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, CREATE USER, EVENT, TRIGGER, CREATE TABLESPACE, CREATE ROLE, DROP ROLE ON *.* TO `root`@`%` WITH GRANT OPTION,GRANT APPLICATION_PASSWORD_ADMIN,ROLE_ADMIN,SHOW_ROUTINE,XA_RECOVER_ADMIN ON *.* TO `root`@`%` WITH GRANT OPTION 请参考 https://cloud.tencent.com/document/product/571/52412"
                    }
                ]
            },
            {
                "Errors": [],
                "Percent": 100,
                "Status": "finished",
                "StepId": "BinlogParamCheck",
                "StepName": "binlog参数检查",
                "StepNo": 5,
                "Warnings": []
            }
        ],
        "SubscribeId": "subs-9jyki7hniw"
    }
}
```

