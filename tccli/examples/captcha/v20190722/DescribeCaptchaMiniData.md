**Example 1: 请求和返回示例**



Input: 

```
tccli captcha DescribeCaptchaMiniData --cli-unfold-argument  \
    --CaptchaAppId 201000000 \
    --Start 2019112900 \
    --End 2019112902 \
    --Type 1
```

Output: 
```
{
    "Response": {
        "RequestId": "9631f24e-6789-4620-b250-746549226514",
        "CaptchaCode": 0,
        "CaptchaMsg": "",
        "Data": [
            {
                "Cnt": 0,
                "Date": "2019112900"
            },
            {
                "Cnt": 0,
                "Date": "2019112901"
            },
            {
                "Cnt": 0,
                "Date": "2019112902"
            }
        ]
    }
}
```

