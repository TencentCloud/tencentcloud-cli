**Example 1: 请求和返回示例**

查询验证码列表信息

Input: 

```
tccli captcha DescribeCaptchaInfoListInternational --cli-unfold-argument  \
    --CaptchaAppId 179*****2 \
    --OrderBy.CreateTime 字符串 \
    --PageIndex 整型 \
    --UserSetCapTypeArr 字符串 \
    --ChannelInfoArr 字符串 \
    --PageSize 整型 \
    --AppName 字符串 \
    --VerifyRankArr 字符串
```

Output: 
```
{
    "Response": {
        "RequestId": "5b320902-54f3-4b70-8663-6e86e99dffff",
        "Data": {
            "DataList": [],
            "Total": 0,
            "PageIndex": 0
        },
        "CaptchaCode": 0,
        "CaptchaMsg": "success"
    }
}
```

