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
            "UpdateTime": "xx",
            "Description": "xx",
            "TemplateName": "xx",
            "Url": "xx",
            "TemplateId": 1,
            "CreateTime": "xx",
            "WaitDuration": 1,
            "MaxDuration": 1
        },
        "RequestId": "xx"
    }
}
```

