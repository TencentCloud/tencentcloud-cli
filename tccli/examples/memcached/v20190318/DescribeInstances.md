**Example 1: 请求示例**



Input: 

```
tccli memcached DescribeInstances --cli-unfold-argument  \
    --OrderBy xx \
    --SearchKeys 字符串型 \
    --UniqSubnetIds xx \
    --Vips xx \
    --OrderType 0 \
    --InstanceNames 字符串型 \
    --UniqVpcIds xx \
    --Limit 1 \
    --Offset 1 \
    --ProjectIds 0 \
    --InstanceIds 有符号整型
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
                "SetId": 0
            }
        ]
    }
}
```

**Example 2: 测试返回**



Input: 

```
tccli memcached DescribeInstances --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "50084d05-cbd9-4fd6-9ee6-03504521a1f2",
        "TotalNum": 1,
        "InstanceList": [
            {
                "InstanceId": "cmem-nksuaveq",
                "InstanceName": "cmem-nksuaveq",
                "AppId": 251009545,
                "ProjectId": 10,
                "InstanceDesc": "cmem-nksuaveq",
                "Vip": "",
                "Vport": 9101,
                "Status": 0,
                "AutoRenewFlag": 0,
                "VpcId": 0,
                "SubnetId": 0,
                "PayMode": 0,
                "ZoneId": 100002,
                "Expire": 0,
                "RegionId": 1,
                "AddTimeStamp": "2022-02-11 11:12:45",
                "ModTimeStamp": "2022-02-11 11:12:45",
                "IsolateTimeStamp": "2022-02-11 11:12:45",
                "UniqVpcId": "",
                "UniqSubnetId": "",
                "DeadlineTimeStamp": "0001-01-01 08:05:43",
                "SetId": 500728,
                "CmemId": 0,
                "Tags": []
            }
        ]
    }
}
```

