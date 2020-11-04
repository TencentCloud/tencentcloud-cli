**Example 1: **



Input: 

```
tccli memcached DescribeInstances --cli-unfold-argument  \
    --Limit 无符号整型\
    --OrderBy 字符串型\
    --OrderType 有符号整型\
    --Offset 无符号整型\
    --SearchKeys 字符串型\
    --ProjectIds 有符号整型\
    --InstanceIds 有符号整型\
    --InstanceNames 字符串型
```

Output: 
```
{
    "Response": {
        "TotalNum": 1,
        "RequestId": "e3d683fc-f2ff-43c9-980d-fae7a1166abc",
        "InstanceList": [
            {
                "InstanceId": 165150,
                "InstanceName": "cmem-a85xwfxm",
                "AppId": 0,
                "ProjectId": 0,
                "InstanceDesc": "cmem-a85xwfxm",
                "Vip": "",
                "Vport": 1030,
                "Status": 1,
                "AutoRenewFlag": 0,
                "VpcId": 0,
                "SubnetId": 0,
                "PayMode": 0,
                "ZoneId": 0,
                "Expire": 0,
                "RegionId": 1,
                "AddTimeStamp": "2019-03-31 15:23:07",
                "ModTimeStamp": "2019-04-03 20:30:06",
                "IsolateTimeStamp": "2019-03-31 15:23:07",
                "UniqVpcId": "",
                "UniqSubnetId": "",
                "DeadlineTimeStamp": "0001-01-01 08:05:52",
                "SetId": 0,
                "InstanceAlias": ""
            }
        ]
    }
}
```

