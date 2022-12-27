**Example 1: 请求示例**



Input: 

```
tccli sms AddSmsSign --cli-unfold-argument  \
    --Remark "xxxx" \
    --SignType 0 \
    --CommissionImage "xxxx" \
    --SignName “test” \
    --DocumentType 1 \
    --International 0 \
    --UsedMethod 1 \
    --ProofImage "xxxx"
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

