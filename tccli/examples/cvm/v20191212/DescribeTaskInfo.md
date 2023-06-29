**Example 1: 查询维修任务列表**

根据指定过滤条件查询云服务器维修任务列表及详细信息。

Input: 

```
tccli cvm DescribeTaskInfo --cli-unfold-argument  \
    --StartDate 2023-01-01 00:00:00 \
    --EndDate 2023-02-01 00:00:00 \
    --Limit 20 \
    --Offset 0 \
    --OrderField CreateTime \
    --Order 1 \
    --TaskStatus 1 2 3 4 5 6
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RepairTaskInfoSet": [
            {
                "TaskId": "rep-xxxxxxxx",
                "InstanceId": "ins-xxxxxxxx",
                "Alias": "test",
                "TaskTypeId": "107",
                "TaskStatus": 3,
                "CreateTime": "2023-01-12 21:00:00",
                "AuthTime": "2023-01-14 21:00:00",
                "EndTime": "2023-01-14 22:00:00",
                "TaskDetail": "监控到您的云服务器存在隐患，可能导致云服务器高负载或宕机。为尽快修复隐患，需要您授权我们在线迁移。感谢您的支持与理解。",
                "DeviceStatus": 3,
                "OperateStatus": 3,
                "Zone": "ap-guangzhou-7",
                "Region": "ap-guangzhou",
                "VpcId": "vpc-xxxxxxxx",
                "SubnetId": "subnet-xxxxxxxx",
                "SubnetName": "Default-Subnet",
                "VpcName": "Default-VPC",
                "AuthSource": "System_mandatory_auth",
                "WanIp": "xxx.xx.xx.xx",
                "LanIp": "xxx.xx.xx.xx",
                "TaskTypeName": "实例维护升级",
                "TaskSubType": null,
                "AuthType": 2,
                "Product": "CVM"
            }
        ],
        "RequestId": "3ec66f17-0f5c-43df-85dd-6be2929dbef1"
    }
}
```

