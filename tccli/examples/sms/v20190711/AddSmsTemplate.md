**Example 1: 请求示例**



Input: 

```
tccli sms AddSmsTemplate --cli-unfold-argument  \
    --SmsType 3 \
    --International 0 \
    --Remark 业务验证码 \
    --TemplateContent your code is {1} \
    --TemplateName 腾讯云
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

