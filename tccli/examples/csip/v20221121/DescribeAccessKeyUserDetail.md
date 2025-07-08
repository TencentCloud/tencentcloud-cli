**Example 1: 1**



Input: 

```
tccli csip DescribeAccessKeyUserDetail --cli-unfold-argument  \
    --SubUin 1000***1**78
```

Output: 
```
{
    "Response": {
        "RequestId": "85ffe508-b4a0-4125-b2b5-b78519c30d69",
        "User": {
            "AccessKeyAlarmList": [],
            "AccessKeyRiskList": [
                {
                    "Count": 6,
                    "Type": 0
                }
            ],
            "AccessType": 1,
            "ActionFlag": 0,
            "Advice": 2,
            "AppID": 1300008,
            "CheckStatus": 0,
            "ID": 200637,
            "ISP": "电信",
            "LoginFlag": 0,
            "LoginIP": "119.147.10.163",
            "LoginLocation": "中国-广东省-深圳市",
            "LoginTime": "2025-05-22 10:45:34",
            "Name": "cfw-test",
            "Nickname": "天空之蓝",
            "SubNickname": "cfw-test",
            "SubUin": "1000***1**78",
            "Type": 1,
            "Uin": "1000*****18"
        }
    }
}
```

