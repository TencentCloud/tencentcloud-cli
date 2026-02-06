**Example 1: 获取集群产生的事件**



Input: 

```
tccli cdwch DescribeEventTasks --cli-unfold-argument  \
    --InstanceId cdwch-l9hnzxps \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "EventTasks": [
            {
                "CreateTime": "2025-09-05T10:52:31+08:00",
                "EventCode": "EmptyPassword",
                "EventDetail": "检测到该实例存在安全隐患，创建集群时的默认 default 账户使用了空密码或弱密码，建议您及时对 default 账户密码进行增强，以提升安全防护能力。您可以通过 TCHouse-C 控制台>参数配置>XML模式>user.xml 对 default 密码进行更换。",
                "EventNameDescribe": "default账户使用空密码",
                "EventPriority": 3,
                "EventTaskId": 5,
                "FinishTime": "",
                "HandleUser": "",
                "IP": "",
                "InstanceId": "",
                "NeedAuthorization": 1,
                "OperationType": [
                    "ModifyPassword"
                ],
                "RepairId": "",
                "Status": 1
            },
            {
                "CreateTime": "2025-09-05T10:52:31+08:00",
                "EventCode": "InstanceMaintenance",
                "EventDetail": "检测到当前底层服务器因架构、软件升级等原因需要发起在线维护，以提升实例性能及安全性。为尽快修复异常，需要您授权我们进行后台处理，超过48小时未处理将认为您自动授权通过。",
                "EventNameDescribe": "实例维护升级",
                "EventPriority": 3,
                "EventTaskId": 6,
                "FinishTime": "",
                "HandleUser": "100025004453",
                "IP": "",
                "InstanceId": "",
                "NeedAuthorization": 2,
                "OperationType": [
                    "OnlineMaintenanceForInstance",
                    "ShutdownForInstance"
                ],
                "RepairId": "",
                "Status": 3
            },
            {
                "CreateTime": "2025-09-05T10:52:31+08:00",
                "EventCode": "InstanceDiskAlter",
                "EventDetail": "检测到节点当前底层服务器的本地硬盘存在坏盘隐患或使用寿命即将耗尽，可能导致实例 I/O 异常或磁盘掉线等数据层面异常。为尽快修复异常，需要您授权我们进行后台处理。",
                "EventNameDescribe": "实例硬盘预警",
                "EventPriority": 3,
                "EventTaskId": 7,
                "FinishTime": "",
                "HandleUser": "100025004453",
                "IP": "",
                "InstanceId": "",
                "NeedAuthorization": 2,
                "OperationType": [
                    "OnlineMaintenanceForDisk",
                    "ShutdownForLocal",
                    "AbandonedDiskMigration"
                ],
                "RepairId": "",
                "Status": 3
            },
            {
                "CreateTime": "2025-09-05T10:52:31+08:00",
                "EventCode": "AbnormalInstanceDisk",
                "EventDetail": "检测到当前底层服务器的本地硬盘突发故障，可能导致节点 I/O 性能降低或硬盘功能受损。为尽快修复异常，需要您授权我们进行后台处理，超过48小时未处理将认为您自动授权通过。",
                "EventNameDescribe": "实例硬盘异常",
                "EventPriority": 3,
                "EventTaskId": 8,
                "FinishTime": "",
                "HandleUser": "100000951792",
                "IP": "",
                "InstanceId": "",
                "NeedAuthorization": 2,
                "OperationType": [
                    "ShutdownForLocal",
                    "AbandonedDiskMigration"
                ],
                "RepairId": "",
                "Status": 3
            },
            {
                "CreateTime": "2025-09-05T10:52:31+08:00",
                "EventCode": "InstanceRisk",
                "EventDetail": "检测到当前底层服务器存在软硬件隐患，可能导致节点性能抖动或存在异常宕机风险。为尽快修复异常，需要您授权我们进行后台处理，超过48小时未处理将认为您自动授权通过。",
                "EventNameDescribe": "实例运行隐患",
                "EventPriority": 3,
                "EventTaskId": 9,
                "FinishTime": "",
                "HandleUser": "100000951792",
                "IP": "",
                "InstanceId": "",
                "NeedAuthorization": 2,
                "OperationType": [
                    "ShutdownForLocal",
                    "AbandonedDiskMigration"
                ],
                "RepairId": "",
                "Status": 3
            },
            {
                "CreateTime": "2025-09-05T10:52:31+08:00",
                "EventCode": "InstanceRisk",
                "EventDetail": "检测到当前底层服务器存在软硬件隐患，可能导致节点性能抖动或存在异常宕机风险。为尽快修复异常，需要您授权我们进行后台处理，超过48小时未处理将认为您自动授权通过。",
                "EventNameDescribe": "实例运行隐患",
                "EventPriority": 3,
                "EventTaskId": 10,
                "FinishTime": "",
                "HandleUser": "100000951792",
                "IP": "",
                "InstanceId": "",
                "NeedAuthorization": 2,
                "OperationType": [
                    "ShutdownForSSD",
                    "OnlineMigrationForInstance"
                ],
                "RepairId": "",
                "Status": 3
            }
        ],
        "RequestId": "141981e2-81ec-4182-bf97-4f31a2735675",
        "TotalCount": 6
    }
}
```

