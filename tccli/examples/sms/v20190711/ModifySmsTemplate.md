**Example 1: 请求示例**



Input: 

```
tccli sms ModifySmsTemplate --cli-unfold-argument  \
    --TemplateId 1110 \
    --TemplateName 腾讯云 \
    --TemplateContent "xxx" \
    --SmsType 1 \
    --International 0 \
    --Remark “xxx”
```

Output: 
```
{
    "Response": {
        "ModifyTemplateStatus": {
            "TemplateId": 1110
        },
        "RequestId": "f36e4f00-605e-49b1-ad0d-bfaba81c7325"
    }
}
```

