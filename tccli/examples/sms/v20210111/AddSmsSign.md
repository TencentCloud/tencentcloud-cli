**Example 1: 请求示例**



Input: 

```
tccli sms AddSmsSign --cli-unfold-argument  \
    --Remark 业务自用申请 \
    --SignPurpose 0 \
    --SignType 0 \
    --CommissionImage base64 \
    --SignName 腾讯云 \
    --DocumentType 1 \
    --International 0 \
    --ProofImage base64
```

Output: 
```
{
    "Response": {
        "AddSignStatus": {
            "SignId": 1110
        },
        "RequestId": "f36e4f00-605e-49b1-ad0d-bfaba81c7325"
    }
}
```

