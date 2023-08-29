**Example 1: 创建个人用户证明证书图片**

创建个人用户证明证书图片

Input: 

```
tccli ess CreatePersonAuthCertificateImage --cli-unfold-argument  \
    --Operator.Channel string \
    --Operator.ClientIp 1.1.1.1 \
    --Operator.OpenId 321654 \
    --Operator.ProxyIp 2.2.2.2 \
    --Operator.UserId 11234567890123456789012345678901 \
    --UserName 姓名 \
    --IdCardType ID_CARD \
    --IdCardNumber 110xxxxxxxx1717
```

Output: 
```
{
    "Response": {
        "AuthCertUrl": "https://file.test.ess.tencent.cn/bresource/resource/resource/0/0.JPG?hkey=522d****6cb5",
        "RequestId": "s169329230***84920859",
        "SerialNumber": "1000000000095674",
        "ValidFrom": 1692788219,
        "ValidTo": 1724324219
    }
}
```

