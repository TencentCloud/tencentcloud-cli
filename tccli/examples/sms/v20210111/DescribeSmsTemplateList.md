**Example 1: 请求示例**



Input: 

```
tccli sms DescribeSmsTemplateList --cli-unfold-argument  \
    --International 0 \
    --TemplateIdSet 1110 1111
```

Output: 
```
{
    "Response": {
        "DescribeTemplateStatusSet": [
            {
                "TemplateName": "验证码",
                "TemplateId": 1110,
                "International": 0,
                "ReviewReply": "",
                "CreateTime": 1617379200,
                "TemplateContent": "您的验证码是{1}",
                "StatusCode": 0
            },
            {
                "TemplateName": "通知",
                "TemplateId": 1111,
                "International": 0,
                "ReviewReply": "",
                "CreateTime": 1617508800,
                "TemplateContent": "请尽快参加{1}会议",
                "StatusCode": 0
            }
        ],
        "RequestId": "f36e4f00-605e-49b1-ad0d-bfaba81c7325"
    }
}
```

