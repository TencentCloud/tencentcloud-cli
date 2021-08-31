**Example 1: 示例**



Input: 

```
tccli cwp DescribeProtectDirRelatedServer --cli-unfold-argument  \
    --Id /tmp \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Id": "/temp",
                "AutoRestoreSwitchStatus": 1,
                "HostName": "目录名称1",
                "HostIp": "10.0.0.1",
                "MachineOs": "Linux",
                "RelateDirNum": 1,
                "ProtectSwitch": 1,
                "ProtectStatus": 1,
                "Quuid": "服务器唯一ID",
                "Authorization": true,
                "Exception": 0,
                "Progress": 10,
                "ExceptionMessage": "启动中"
            }
        ],
        "RequestId": "7eb47586-e1e9-40eb-a3e1-bc73cf1e475f",
        "TotalCount": 1,
        "ProtectServerCount": 1
    }
}
```

