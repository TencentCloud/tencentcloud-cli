**Example 1: 1**



Input: 

```
tccli csip DescribeAccessKeyUserList --cli-unfold-argument  \
    --Filter.Limit 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AccessKeyAlarmList": [
                    {
                        "Count": 12,
                        "Type": 0
                    }
                ],
                "AccessKeyRiskList": [
                    {
                        "Count": 1,
                        "Type": 0
                    }
                ],
                "AccessType": 1,
                "ActionFlag": 0,
                "Advice": 1,
                "AppID": 13000008,
                "CheckStatus": 0,
                "ID": 200631,
                "ISP": "电信",
                "LoginFlag": 0,
                "LoginIP": "113.108.**.73",
                "LoginLocation": "中国-广东省-深圳市",
                "LoginTime": "2025-05-07 15:21:05",
                "Name": "jose***li_blue",
                "Nickname": "天空之蓝",
                "SubNickname": "josephlkli_blue",
                "SubUin": "1000***72635",
                "Type": 1,
                "Uin": "1000***6646"
            }
        ],
        "RequestId": "fabb0428-3853-46df-b473-afbc7021fed4",
        "Total": 22
    }
}
```

