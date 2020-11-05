**Example 1: Sample request**



Input: 

```
tccli sms AddSmsTemplate --cli-unfold-argument  \
    --TemplateName 'Tencent Cloud'\
    --TemplateContent "xxx"\
    --SmsType test\
    --International 0\
    --Remark “xxx”
```

Output: 
```
{
    "Response": {
        "AddTemplateStatus": {
            "TemplateId": 1110,
            "RequestStatus": "return successfully!"
        },
        "RequestId": "f36e4f00-605e-49b1-ad0d-bfaba81c7325"
    }
}
```

