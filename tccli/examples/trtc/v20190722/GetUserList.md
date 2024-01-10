**Example 1: 获取用户列表**

用于TRTC控制台获取房间用户列表

Input: 

```
tccli trtc GetUserList --cli-unfold-argument  \
    --CommId 1400188366_666_1570864946 \
    --StartTs 1570864946 \
    --EndTs 1570866037
```

Output: 
```
{
    "Response": {
        "UserList": [
            {
                "UserId": "666",
                "JoinTs": 1570864946,
                "LeaveTs": 1570866037,
                "Duration": 1091,
                "Finished": true,
                "TinyId": "xx",
                "UserRole": "xx",
                "Role": "both",
                "Location": "中国广东深圳",
                "SdkVersion": "6.6.0.7415",
                "Os": "Android",
                "OsVersion": "",
                "DeviceType": "",
                "Network": "WIFI",
                "UserType": "xx",
                "ClientIp": "59.37.125.38",
                "AccessIp": "10.1.2.8",
                "ConnRoomNum": 0,
                "ConnCommId": ""
            }
        ],
        "TotalSender": 1,
        "Total": 1,
        "RequestId": "4fae8a9b-d338-4d73-b452-7e3f1c31487e"
    }
}
```

