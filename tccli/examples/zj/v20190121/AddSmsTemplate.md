**Example 1: AddSmsTemplate**



Input: 

```
tccli zj AddSmsTemplate --cli-unfold-argument  \
    --Remark “xxx” \
    --License xsdf \
    --TemplateName 腾讯云 \
    --SmsType 0 \
    --International 0 \
    --SignID 2222222 \
    --TemplateContent "xxx"
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

