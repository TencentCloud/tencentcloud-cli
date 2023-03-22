**Example 1: 查询账号下所有回调URL列表**

查询账号下所有回调URL列表

Input: 

```
tccli monitor DescribeAlarmNoticeCallbacks --cli-unfold-argument  \
    --Module monitor
```

Output: 
```
{
    "Response": {
        "URLNotices": [
            {
                "URL": "http://www.test1.com/validate",
                "IsValid": 0
            },
            {
                "URL": "http://www.test2.com/validate",
                "IsValid": 0
            },
            {
                "URL": "https://www.test3.com/validate",
                "IsValid": 1
            }
        ],
        "RequestId": "neh390an4opw0-45nw"
    }
}
```

