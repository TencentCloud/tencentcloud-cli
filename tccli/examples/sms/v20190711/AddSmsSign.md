**Example 1: 请求示例**



Input: 

```
tccli sms AddSmsSign --cli-unfold-argument  \
    --SignName “test” \
    --SignType 0 \
    --DocumentType 1 \
    --International 0 \
    --UsedMethod 1 \
    --ProofImage "xxxx" \
    --CommissionImage "xxxx" \
    --Remark "xxxx"
```

Output: 
```
{
    "Response": {
        "AddSignStatus": {
            "SignId": 1110,
            "SignApplyId": 1109
        },
        "RequestId": "f36e4f00-605e-49b1-ad0d-bfaba81c7325"
    }
}
```

