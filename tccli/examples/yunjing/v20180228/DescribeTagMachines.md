**Example 1: 获取指定标签关联的服务器信息**

获取指定标签关联的服务器信息

Input: 

```
tccli yunjing DescribeTagMachines --cli-unfold-argument  \
    --Id 1
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "Machines": [
            {
                "MachineName": "h2-stevenyu",
                "MachineIp": "10.104.86.62",
                "MachineWanIp": "132.104.86.62",
                "MachineOs": "centos6.5",
                "MachineStatus": "ONLINE",
                "Quuid": "6b6cd843-6bc1-4011-a74c-dc3fd26a7dd1",
                "Uuid": "9c6cd943-dbc1-4011-a74c-x4d9d26a7891",
                "IsProVersion": true,
                "PayMode": "PREPAY",
                "Tag": [
                    {
                        "Name": "Name",
                        "Rid": 100
                    }
                ],
                "VulNum": 10
            }
        ],
        "TotalCount": 100
    }
}
```

