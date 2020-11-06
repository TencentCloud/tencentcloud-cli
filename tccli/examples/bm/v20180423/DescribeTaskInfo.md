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
        "RequestId": "56b1bc7b-c97c-4f17-a42d-bb9c181b9b83",
        "TotalCount": 2,
        "TaskInfoSet": [
            {
                "TaskId": "bm-repair-pygkh5q7",
                "TaskTypeId": 49,
                "TaskStatus": 1,
                "CreateTime": "2018-07-16 10:42:29",
                "AuthTime": "",
                "EndTime": "",
                "TaskDetail": "内存出现故障会导致存储数据发生改变、程序出错，严重情况下会导致系统出现异常直接影响业务。",
                "InstanceId": "tcpm-rewhxuo7",
                "Alias": "jason - 黑石 - 织云测试1",
                "DeviceStatus": 4,
                "OperateStatus": 20,
                "VpcId": "vpc-34cxlz7z",
                "SubnetId": "subnet-1so5ae8m",
                "WanIp": "115.159.240.68",
                "LanIp": "10.10.1.60",
                "MgtIp": "100.73.46.196",
                "Region": "ap-beijing",
                "SubnetName": "sub1",
                "VpcName": "test",
                "VpcCidrBlock": "10.0.0.0/16",
                "SubnetCidrBlock": "10.0.0.0/24",
                "Zone": "ap-beijing-bls-1"
            },
            {
                "TaskId": "bm-repair-6ofdlrht",
                "TaskTypeId": 44,
                "TaskStatus": 1,
                "CreateTime": "2018-07-13 17:47:33",
                "AuthTime": "",
                "EndTime": "",
                "TaskDetail": "设备己停机，业务己中断。",
                "InstanceId": "cpm-cbqm5mo8",
                "Alias": "ami - NAT日志版本测试",
                "DeviceStatus": 4,
                "OperateStatus": 1,
                "VpcId": "vpc-4vk5e4bu",
                "SubnetId": "subnet-mkziizg3",
                "WanIp": "",
                "LanIp": "10.123.0.30",
                "MgtIp": "100.81.198.66",
                "Region": "ap-beijing",
                "SubnetName": "sub13",
                "VpcName": "HEISHI_VPCk",
                "VpcCidrBlock": "10.1.0.0/16",
                "SubnetCidrBlock": "10.1.55.0/24",
                "Zone": "ap-beijing-bls-1"
            }
        ]
    }
}
```

