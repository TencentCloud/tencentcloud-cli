**Example 1: 请求和返回示例**



Input: 

```
tccli captcha DescribeCaptchaUserAllAppId --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "ea4ba358-8055-4fac-ba2b-e039110b301a",
        "CaptchaCode": 0,
        "CaptchaMsg": "",
        "Data": [
            {
                "TcAppId": 125111111,
                "CaptchaAppId": 201111111,
                "AppName": "短信验证",
                "ChannelInfo": "mini"
            }
        ]
    }
}
```

