**Example 1: 设备状态查询**

正常响应

Input: 

```
tccli weilingwith DescribeDeviceStatusList --cli-unfold-argument  \
    --WorkspaceId 1016 \
    --ApplicationToken YVySZSL1Lp5UtSJ5uJVLJYOKDEGfCCH2 \
    --WIDSet be2ea997-b7f4-4167-9545-9aa275158a92 \
    --PageNumber 1 \
    --PageSize 1
```

Output: 
```
{
    "Response": {
        "RequestId": "1286216c-1022-4bd6-83a2-3dfb0bee6fe2",
        "Result": {
            "DeviceStatusSet": [
                {
                    "DeviceStatus": "online",
                    "DeviceStatusUpdateTime": "2023-08-31 00:57:28",
                    "IsAlive": true,
                    "Status": "normal",
                    "WID": "be2ea997-b7f4-4167-9545-9aa275158a92"
                }
            ],
            "PageNumber": 1,
            "PageSize": 1,
            "TotalPage": 1,
            "TotalRow": 1
        }
    }
}
```

