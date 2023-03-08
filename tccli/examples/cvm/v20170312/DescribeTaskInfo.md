**Example 1: 查询待授权的维修任务列表**

根据以下条件，查询并获取维修任务返回列表：

- 任务的创建时间在 `2023-03-01 00:00:00` ~ `2023-04-01 00:00:00` 范围内。
- 任务当前的状态为`待授权`。
- 返回的任务列表按照`CreateTime`创建时间降序返回，偏移量为`0`，最多返回`20`条数据。

Input: 

```
tccli cvm DescribeTaskInfo --cli-unfold-argument  \
    --StartDate 2023-03-01 00:00:00 \
    --EndDate 2023-04-01 00:00:00 \
    --TaskStatus 1 \
    --Limit 20 \
    --Offset 0 \
    --OrderField CreateTime \
    --Order 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "RepairTaskInfoSet": [
            {
                "TaskId": "rep-xxxxxxxx",
                "InstanceId": "ins-xxxxxxxx",
                "Alias": "test-1",
                "TaskTypeId": 107,
                "TaskStatus": 1,
                "CreateTime": "2023-03-08 12:00:00",
                "AuthTime": "2023-03-10 12:00:00",
                "EndTime": null,
                "TaskDetail": "监控到您的云服务器因底层宿主机架构、软件升级需要发起在线维护，处理过程中云服务器可能出现短时间高负载或者网络抖动。为尽快完成维护以提升实例性能及安全性，需要您授权我们在线维护。感谢您的支持与理解。",
                "DeviceStatus": 1,
                "OperateStatus": 1,
                "Zone": "ap-guangzhou-7",
                "Region": "ap-guangzhou",
                "VpcId": "vpc-xxxxxxxx",
                "SubnetId": "subnet-xxxxxxxx",
                "SubnetName": "Default-Subnet",
                "VpcName": "Default-VPC",
                "AuthSource": "System_mandatory_auth",
                "WanIp": "xxx.xxx.xxx.xxx",
                "LanIp": "xxx.xxx.xxx.xxx",
                "TaskTypeName": "实例维护升级",
                "TaskSubType": null,
                "AuthType": 6,
                "Product": "CVM"
            },
            {
                "TaskId": "rep-xxxxxxxx",
                "InstanceId": "ins-xxxxxxxx",
                "Alias": "test-2",
                "TaskTypeId": 101,
                "TaskStatus": 1,
                "CreateTime": "2023-03-07 12:00:00",
                "AuthTime": "2023-03-09 12:00:00",
                "EndTime": null,
                "TaskDetail": "监控到您的云服务器存在隐患，可能导致云服务器高负载或宕机。为尽快修复隐患，需要您授权我们停机处理。感谢您的支持与理解。",
                "DeviceStatus": 1,
                "OperateStatus": 1,
                "Zone": "ap-guangzhou-7",
                "Region": "ap-guangzhou",
                "VpcId": "vpc-xxxxxxxx",
                "SubnetId": "subnet-xxxxxxxx",
                "SubnetName": "Default-Subnet",
                "VpcName": "Default-VPC",
                "AuthSource": "System_mandatory_auth",
                "WanIp": "xxx.xxx.xxx.xxx",
                "LanIp": "xxx.xxx.xxx.xxx",
                "TaskTypeName": "实例运行隐患",
                "TaskSubType": null,
                "AuthType": 2,
                "Product": "CVM"
            }
        ],
        "RequestId": "4dc8d1d7-bd0f-4216-b7c5-e8a13d6a850c"
    }
}
```

