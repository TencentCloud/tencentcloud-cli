**Example 1: 获取组件列表**

获取组件列表

Input: 

```
tccli cwp DescribeComponents --cli-unfold-argument  \
    --ComponentId 100019 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Components": [
            {
                "Id": 1,
                "MachineIp": "10.12.13.22",
                "MachineName": "machine-name",
                "ModifyTime": "2018-01-01 12:12:12",
                "ComponentVersion": "5.7.16",
                "ComponentType": "WEB",
                "ComponentName": "Mysql Server",
                "Uuid": "6b6cd843-6bc1-4011-a74c-dc3fd26a7dd1"
            }
        ],
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "TotalCount": 100
    }
}
```

