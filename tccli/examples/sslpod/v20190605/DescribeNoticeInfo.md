**Example 1: 获取通知额度信息**



Input: 

```
tccli sslpod DescribeNoticeInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "Id": 63692,
            "NoticeType": 4,
            "LimitInfos": [
                {
                    "Type": "limit_email",
                    "Total": 30,
                    "Sent": 0
                },
                {
                    "Type": "limit_wechat",
                    "Total": 30,
                    "Sent": 0
                },
                {
                    "Type": "limit_phone",
                    "Total": 0,
                    "Sent": 0
                }
            ]
        },
        "RequestId": "d69688b9-4e56-467b-a352-b04ba8a13a47"
    }
}
```

