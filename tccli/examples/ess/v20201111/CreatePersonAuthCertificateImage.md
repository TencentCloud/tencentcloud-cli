**Example 1: 创建个人用户证明证书图片**

创建个人用户证明证书图片

Input: 

```
tccli ess CreatePersonAuthCertificateImage --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq**4zjEwg0vjoimj \
    --UserName 典子谦 \
    --IdCardType ID_CARD \
    --IdCardNumber 620000198802020000
```

Output: 
```
{
    "Response": {
        "AuthCertUrl": "https://file.test.ess.tencent.cn/bresource/resource/resource/0/0.JPG?hkey=522d****6cb5",
        "RequestId": "69c19f7e7240",
        "SerialNumber": "23090411***877319694",
        "ValidFrom": 1692788219,
        "ValidTo": 1724324219
    }
}
```

