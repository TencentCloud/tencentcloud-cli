**Example 1: 查询用户列表与通话指标**



Input: 

```
tccli trtc DescribeCallDetail --cli-unfold-argument  \
    --DataType bigvCapFps \
    --CommId 1400188366_218695_1590065777 \
    --EndTime 1590065877 \
    --SdkAppId 1400188366 \
    --StartTime 1590065777
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "UserList": [
            {
                "RoomStr": "218695",
                "UserId": "1716",
                "JoinTs": 1590065777,
                "LeaveTs": 1590067658,
                "Finished": true,
                "DeviceType": "",
                "SdkVersion": "4.3.14",
                "ClientIp": "10.4.1.13"
            }
        ],
        "Data": [
            {
                "Content": [
                    {
                        "Time": 1590065779,
                        "Value": 0
                    },
                    {
                        "Time": 1590065781,
                        "Value": 0
                    },
                    {
                        "Time": 1590065783,
                        "Value": 0
                    },
                    {
                        "Time": 1590065785,
                        "Value": 0
                    },
                    {
                        "Time": 1590065787,
                        "Value": 0
                    },
                    {
                        "Time": 1590065789,
                        "Value": 0
                    }
                ],
                "PeerId": "",
                "UserId": "1716",
                "DataType": "bigvCapFps"
            }
        ],
        "RequestId": "2e12e365-43e8-4efd-902d-906303e2ee4a"
    }
}
```

