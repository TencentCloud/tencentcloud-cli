**Example 1: 获取端口列表**

获取端口列表

Input: 

```
tccli yunjing DescribeOpenPorts --cli-unfold-argument  \
    --Port 3306 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "OpenPorts": [
            {
                "Id": 1,
                "Uuid": "6b6cd843-6bc1-4011-a74c-dc3fd26a7dd1",
                "Port": 3306,
                "MachineIp": "10.12.13.22",
                "MachineName": "h2-stevenyu",
                "ProcessName": "mysql",
                "Pid": 14456,
                "CreateTime": "2018-01-01 12:12:12",
                "ModifyTime": "2018-01-01 12:12:12"
            }
        ],
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "TotalCount": 100
    }
}
```

