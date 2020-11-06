**Example 1: 查询用户列表与通话指标**



Input: 

```
tccli trtc DescribeUserInformation --cli-unfold-argument  \
    --CommId 1400353843_218695_1590065777 \
    --StartTime 1590065777 \
    --EndTime 1590065877 \
    --SdkAppId 1400353843
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
        "RequestId": "2e12e365-43e8-4efd-902d-906303e2ee4a"
    }
}
```

