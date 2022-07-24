**Example 1: 查询用户列表与通话指标**



Input: 

```
tccli trtc DescribeUserInfo --cli-unfold-argument  \
    --StartTime 1590065777 \
    --CommId 1400188366_218695_1590065777 \
    --UserIds user1_54816741 user2_2107025 \
    --SdkAppId 1400188366 \
    --EndTime 1590065877
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "UserList": [
            {
                "RoomStr": "218695",
                "UserId": "user1_54816741",
                "JoinTs": 1590065777,
                "LeaveTs": 1590067658,
                "Finished": true,
                "DeviceType": "",
                "SdkVersion": "4.3.14",
                "ClientIp": "10.4.1.13"
            },
            {
                "RoomStr": "218695",
                "UserId": "user2_2107025",
                "JoinTs": 1590065700,
                "LeaveTs": 1590067693,
                "Finished": true,
                "DeviceType": "",
                "SdkVersion": "4.3.14",
                "ClientIp": "10.4.1.13"
            }
        ],
        "RequestId": "2e12e365-43e8-4efd-902d-906303e2ee4a"
    }
}
```

