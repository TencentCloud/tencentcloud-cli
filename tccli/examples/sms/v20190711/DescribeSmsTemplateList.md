**Example 1: 请求示例**



Input: 

```
tccli sms DescribeSmsTemplateList --cli-unfold-argument  \
    --International 0 \
    --TemplateIdSet 1110 1112
```

Output: 
```
{
    "Response": {
        "DescribeTemplateStatusSet": [
            {
                "TemplateId": 1110,
                "International": 0,
                "StatusCode": 0,
                "ReviewReply": "通过",
                "TemplateName": "业务验证码",
                "CreateTime": 1578899900
            },
            {
                "TemplateId": 1112,
                "International": 0,
                "StatusCode": 0,
                "ReviewReply": "通过",
                "TemplateName": "业务验证码",
                "CreateTime": 1578899901
            }
        ],
        "RequestId": "f36e4f00-605e-49b1-ad0d-bfaba81c7325"
    }
}
```

