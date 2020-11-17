**Example 1: ModifySmsTemplate**



Input: 

```
tccli zj ModifySmsTemplate --cli-unfold-argument  \
    --License xsdf \
    --TemplageId 123 \
    --SignID 2222222 \
    --TemplateName 腾讯云 \
    --TemplateContent "xxx" \
    --SmsType 0 \
    --International 0 \
    --Remark “xxx”
```

Output: 
```
{
    "Response": {
        "Data": {
            "TemplateId": 1110
        },
        "RequestId": "f36e4f00-605e-49b1-ad0d-bfaba81c7325"
    }
}
```

