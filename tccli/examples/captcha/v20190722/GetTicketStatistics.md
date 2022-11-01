**Example 1: 请求和返回示例**



Input: 

```
tccli captcha GetTicketStatistics --cli-unfold-argument  \
    --CaptchaAppId 字符串 \
    --EndTimeStr 字符串 \
    --StartTimeStr 字符串 \
    --Dimension 字符串
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

