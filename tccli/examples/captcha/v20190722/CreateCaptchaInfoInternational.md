**Example 1: 请求和返回示例**

创建验证码

Input: 

```
tccli captcha CreateCaptchaInfoInternational --cli-unfold-argument  \
    --UserSetCapType 13 \
    --AppName aaa \
    --VerifyRank 3 \
    --ChannelInfo web \
    --VerifyDomain "*******.com" \
    --VerifyBundleId "com.******* \
    --VerifyPackage "com.******"
```

Output: 
```
{
    "Response": {
        "RequestId": "63ade1a9-eae8-49d4-b8be-bf803bfffdbe",
        "Data": 179000008,
        "CaptchaCode": 11000,
        "CaptchaMsg": ""
    }
}
```

