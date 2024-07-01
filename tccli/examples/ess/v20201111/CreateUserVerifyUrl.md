**Example 1: 获取c端用户实名跳转链接**

获取c端用户实名链接

Input: 

```
tccli ess CreateUserVerifyUrl --cli-unfold-argument  \
    --Operator.UserId 19561039c99fe825a934a132520fde6a \
    --Operator.ClientIp 8.8.8.8 \
    --Name 典子谦 \
    --Endpoint HTTP_SHORT_URL \
    --IdCardType ID_CARD \
    --IdCardNumber 420101XXXXXXXX4059 \
    --Mobile 13200000015
```

Output: 
```
{
    "Response": {
        "ExpireTime": 1713080196,
        "MiniAppId": "",
        "RequestId": "s1712475396892401448",
        "UserVerifyUrl": "https://test.essurl.cn/RTo****6X6"
    }
}
```

