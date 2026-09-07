**Example 1: 请求和返回示例**

修改验证码信息

Input: 

```
tccli captcha ModifyCaptchaInfoInternational --cli-unfold-argument  \
    --CaptchaAppId 179****56 \
    --UserSetCapType "17" \
    --AppName "web-1" \
    --VerifyRank "3" \
    --VerifyDomain “*******.com" \
    --VerifyBundleId "com*******" \
    --VerifyPackage **
```

Output: 
```
{
    "Response": {
        "RequestId": "b28640bd-7d81-4a6f-b659-be0a2a383f52",
        "Data": null,
        "CaptchaCode": 11000,
        "CaptchaMsg": ""
    }
}
```

