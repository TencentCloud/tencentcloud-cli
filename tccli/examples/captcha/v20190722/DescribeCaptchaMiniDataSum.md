**Example 1: 请求和返回示例**



Input: 

```
tccli captcha DescribeCaptchaMiniDataSum --cli-unfold-argument  \
    --CaptchaAppId 2010000000 \
    --Start 20191201 \
    --End 20191201
```

Output: 
```
{
    "Response": {
        "RequestId": "c7151640-8351-46d5-86f9-ce886cf37111",
        "CaptchaCode": 0,
        "CaptchaMsg": "OK",
        "GetSum": 123,
        "VfySuccSum": 112,
        "VfySum": 110,
        "AttackSum": 13,
        "CheckTicketSum": 100,
        "TicketThroughputSum": 90,
        "TicketInterceptSum": 10
    }
}
```

