**Example 1: 请求示例**



Input: 

```
tccli sms AddSmsTemplate --cli-unfold-argument  \
    --SmsType 0 \
    --International 0 \
    --Remark xx \
    --TemplateContent 您的验证码是{1} \
    --TemplateName 验证码
```

Output: 
```
{
    "Response": {
        "AddTemplateStatus": {
            "TemplateId": "1110"
        },
        "RequestId": "f36e4f00-605e-49b1-ad0d-bfaba81c7325"
    }
}
```

