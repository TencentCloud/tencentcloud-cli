**Example 1: 请求示例**

修改短信签名

Input: 

```
tccli sms ModifySmsSign --cli-unfold-argument  \
    --Remark "xxxx" \
    --SignType 0 \
    --CommissionImage "xxxx" \
    --SignName “test” \
    --DocumentType 1 \
    --International 0 \
    --SignId 1110 \
    --ProofImage "xxxx" \
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

