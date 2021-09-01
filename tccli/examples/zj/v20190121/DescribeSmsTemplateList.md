**Example 1: DescribeSmsTemplateList**



Input: 

```
tccli zj DescribeSmsTemplateList --cli-unfold-argument  \
    --License xsdf \
    --TemplateIdSet 1110 1111 \
    --International 0
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "TemplateId": 1110,
                "International": 0,
                "StatusCode": 0,
                "ReviewReply": "xxx",
                "TemplateName": "xxx",
                "CreateTime": "2020-01-13 15:18:20"
            },
            {
                "TemplateId": 1111,
                "International": 0,
                "StatusCode": 0,
                "ReviewReply": "xxx",
                "TemplateName": "xxx",
                "CreateTime": "2020-01-13 15:18:21"
            }
        ],
        "RequestId": "f36e4f00-605e-49b1-ad0d-bfaba81c7325"
    }
}
```

