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
                "TemplateId": 1110,
                "International": 0,
                "StatusCode": 0,
                "ReviewReply": "xxx",
                "TemplateName": "xxx",
                "CreateTime": 1578899900
            },
            {
                "TemplateId": 1111,
                "International": 0,
                "StatusCode": 0,
                "ReviewReply": "xxx",
                "TemplateName": "xxx",
                "CreateTime": 1578899901
            }
        ],
        "RequestId": "f36e4f00-605e-49b1-ad0d-bfaba81c7325"
    }
}
```

