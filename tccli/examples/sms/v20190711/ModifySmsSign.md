**Example 1: 请求示例**

修改短信签名

Input: 

```
tccli sms ModifySmsSign --cli-unfold-argument  \
    --Remark 测试使用 \
    --SignType 0 \
    --CommissionImage base64 \
    --SignName 腾讯云 \
    --DocumentType 1 \
    --International 0 \
    --SignId 1110 \
    --ProofImage base64 \
    --UsedMethod 1
```

Output: 
```
{
    "Response": {
        "ModifySignStatus": {
            "SignId": 1110,
            "SignApplyId": "1109"
        },
        "RequestId": "f36e4f00-605e-49b1-ad0d-bfaba81c7325"
    }
}
```

