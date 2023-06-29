**Example 1: 效果数据反馈**

接收客户反馈的各环节数据



Input: 

```
tccli trp EffectFeedback --cli-unfold-argument  \
    --BusinessSecurityData.IsAuthorized 0 \
    --BusinessSecurityData.EncryptMethod 0 \
    --BusinessSecurityData.EncryptMode 0 \
    --BusinessSecurityData.PaddingType 0 \
    --BusinessSecurityData.EncryptData abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "Code": 0,
            "Message": "abc",
            "Value": "abc"
        },
        "RequestId": "abc"
    }
}
```

