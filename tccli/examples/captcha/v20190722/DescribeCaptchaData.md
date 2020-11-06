**Example 1: 请求和返回示例**



Input: 

```
tccli captcha DescribeCaptchaData --cli-unfold-argument  \
    --CaptchaAppId 201000000 \
    --Start 201911291859 \
    --End 201911291901 \
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
                "Date": "201911291859"
            },
            {
                "Cnt": 0,
                "Date": "201911291900"
            },
            {
                "Cnt": 0,
                "Date": "201911291901"
            }
        ]
    }
}
```

