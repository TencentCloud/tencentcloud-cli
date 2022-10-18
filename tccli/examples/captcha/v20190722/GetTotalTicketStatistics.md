**Example 1: 请求和返回示例**



Input: 

```
tccli captcha GetTotalTicketStatistics --cli-unfold-argument  \
    --EndTimeStr "2022-08-14 14:00" \
    --StartTimeStr “2022-05-14 10:00” \
    --Dimension "3"
```

Output: 
```
{
    "Response": {
        "RequestId": "e6e4b75e504c43b88fd9db327df6d2b5",
        "Data": {
            "ActionTotal": 0,
            "VerifyTotal": 0,
            "VerifyThroughTotal": 0,
            "VerifyInterceptTotal": 0,
            "TicketTotal": 2,
            "TicketThroughTotal": 2,
            "TicketInterceptTotal": 0,
            "RequestTrend": [
                {
                    "Ftime": "10-18 11:11",
                    "RequestAction": 0,
                    "RequestVerify": 0,
                    "RequestThroughput": 0,
                    "RequestIntercept": 0
                }
            ],
            "InterceptPerTrend": [
                {
                    "Ftime": "10-18 11:11",
                    "RequestInterceptPer": 0,
                    "AnswerInterceptPer": 0,
                    "PolicyInterceptPer": 0
                }
            ],
            "TicketCheckTrend": [
                {
                    "Ftime": "10-18 11:11",
                    "TicketCount": 0,
                    "TicketThroughput": 0,
                    "TicketIntercept": 0
                }
            ]
        },
        "CaptchaCode": 0,
        "CaptchaMsg": "success"
    }
}
```

