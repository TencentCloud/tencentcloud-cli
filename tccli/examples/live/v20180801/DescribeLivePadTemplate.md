**Example 1: 请求示例**



Input: 

```
tccli live DescribeLivePadTemplate --cli-unfold-argument  \
    --TemplateId 1
```

Output: 
```
{
    "Response": {
        "Template": {
            "UpdateTime": "2020-01-01 08:00:00",
            "Description": "template",
            "TemplateName": "mytemplate",
            "Url": "https://test.com/a.mp4",
            "TemplateId": 1,
            "CreateTime": "2020-01-01 08:00:00",
            "WaitDuration": 1,
            "MaxDuration": 1,
            "Type": 1
        },
        "RequestId": "3fefec28-3f95-4055-8a22-714cc271251e"
    }
}
```

