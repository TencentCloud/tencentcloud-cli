**Example 1: 获取用户信息**

获取用户详细信息

Input: 

```
tccli yinsuda DescribeUserInfo --cli-unfold-argument  \
    --AppName apl_test \
    --UserId user_id_0
```

Output: 
```
{
    "Response": {
        "UserInfo": {
            "AppName": "apl_test",
            "UserId": "user_id_0",
            "LiveVipUserInfo": {
                "RoomId": "roomid_00",
                "LiveVipEndTime": "2020-09-22T00:00:00+00:00",
                "LiveVipStatus": "Valid"
            },
            "UserType": "Normal"
        },
        "RequestId": "1222fiud8946yhok"
    }
}
```

