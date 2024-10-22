**Example 1: 请求和返回示例**



Input: 

```
tccli captcha GetTicketStatistics --cli-unfold-argument  \
    --CaptchaAppId 199999164 \
    --EndTimeStr 2022-05-14 01:00 \
    --StartTimeStr 2022-06-15 20:00 \
    --Dimension 3
```

Output: 
```
{
    "Response": {
        "RequestId": "458e90ab-4bcb-45ee-b8fd-f5e79e85ffff",
        "Data": null,
        "CaptchaCode": 11000,
        "CaptchaMsg": ""
    }
}
```

