**Example 1: 维修任务信息获取**



Input: 

```
tccli bm DescribeTaskInfo --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --OrderField CreateTime \
    --Order 1 \
    --StartDate 2018-07-10 \
    --EndDate 2018-07-19 \
    --TaskStatus 1 \
    --TaskIds b \
    --InstanceIds o \
    --Aliases - \
    --TaskTypeIds 44 49
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "TaskInfoSet": [
            {
                "Zone": "xx",
                "SubnetName": "xx",
                "EndTime": "2020-09-22 00:00:00",
                "VpcId": "xx",
                "TaskSubType": "xx",
                "TaskDetail": "xx",
                "InstanceId": "xx",
                "DeviceStatus": 1,
                "VpcName": "xx",
                "SubnetId": "xx",
                "MgtIp": "xx",
                "SubnetCidrBlock": "xx",
                "Region": "xx",
                "LanIp": "xx",
                "TaskStatus": 1,
                "Alias": "xx",
                "AuthTime": "2020-09-22 00:00:00",
                "OperateStatus": 1,
                "WanIp": "xx",
                "TaskTypeName": "xx",
                "VpcCidrBlock": "xx",
                "TaskTypeId": 1,
                "TaskId": "xx",
                "CreateTime": "2020-09-22 00:00:00"
            },
            {
                "Zone": "xx",
                "SubnetName": "xx",
                "EndTime": "2020-09-22 00:00:00",
                "VpcId": "xx",
                "TaskSubType": "xx",
                "TaskDetail": "xx",
                "InstanceId": "xx",
                "DeviceStatus": 1,
                "VpcName": "xx",
                "SubnetId": "xx",
                "Region": "xx",
                "SubnetCidrBlock": "xx",
                "MgtIp": "xx",
                "LanIp": "xx",
                "TaskStatus": 1,
                "Alias": "xx",
                "AuthTime": "2020-09-22 00:00:00",
                "OperateStatus": 1,
                "WanIp": "xx",
                "TaskTypeName": "xx",
                "VpcCidrBlock": "xx",
                "TaskTypeId": 1,
                "TaskId": "xx",
                "CreateTime": "2020-09-22 00:00:00"
            }
        ],
        "RequestId": "xx"
    }
}
```

