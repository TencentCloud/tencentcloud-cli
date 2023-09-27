**Example 1: 请求示例**

修改短信签名

Input: 

```
tccli sms ModifySmsSign --cli-unfold-argument  \
    --Remark 自用业务申请 \
    --SignPurpose 0 \
    --SignType 0 \
    --CommissionImage  \
    --SignName 腾讯云 \
    --DocumentType 1 \
    --International 0 \
    --SignId 1110 \
    --ProofImage 
```

Output: 
```
{
    "Response": {
        "ModifySignStatus": {
            "SignId": 1110
        },
        "RequestId": "f36e4f00-605e-49b1-ad0d-bfaba81c7325"
    }
}
```

