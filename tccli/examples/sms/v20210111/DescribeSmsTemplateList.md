**Example 1: 请求示例**



Input: 

```
tccli sms DescribeSmsTemplateList --cli-unfold-argument  \
    --TemplateIdSet 1110 1111 \
    --International 0
```

Output: 
```
{
    "Response": {
        "DescribeTemplateStatusSet": [
            {
                "TemplateName": "xx",
                "TemplateId": 1,
                "International": 1,
                "ReviewReply": "xx",
                "CreateTime": 1,
                "StatusCode": 0
            },
            {
                "TemplateName": "xx",
                "TemplateId": 1,
                "International": 1,
                "ReviewReply": "xx",
                "CreateTime": 1,
                "StatusCode": 0
            }
        ],
        "RequestId": "xx"
    }
}
```

