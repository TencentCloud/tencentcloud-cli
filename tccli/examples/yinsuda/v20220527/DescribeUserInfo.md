**Example 1: 获取用户信息**

获取用户详细信息

Input: 

```
tccli yinsuda DescribeUserInfo --cli-unfold-argument  \
    --AppName test \
    --UserId 111
```

Output: 
```
{
    "Response": {
        "UserInfo": {
            "AppName": "test",
            "UserId": "111",
            "LiveVipUserInfo": {
                "RoomId": "321",
                "LiveVipEndTime": "2020-09-22T00:00:00+00:00",
                "LiveVipStatus": "Valid"
            },
            "UserType": "Normal"
        },
        "RequestId": "abc"
    }
}
```

