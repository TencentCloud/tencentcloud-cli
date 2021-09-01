**Example 1: 创建签名**



Input: 

```
tccli zj AddSmsSign --cli-unfold-argument  \
    --License KA3431QZPU \
    --SignName “test” \
    --SignType 0 \
    --DocumentType 1 \
    --International 0 \
    --ProofImage "xxxx" \
    --Remark "xxxx"
```

Output: 
```
{
    "Response": {
        "Data": {
            "SignId": 1047
        },
        "RequestId": "111111"
    }
}
```

