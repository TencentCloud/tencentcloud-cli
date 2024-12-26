**Example 1: 请求示例**



Input: 

```
tccli live DescribeLivePadTemplates --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Templates": [
            {
                "UpdateTime": "2020-01-01 08:00:00",
                "Description": "template",
                "TemplateName": "mytemplate",
                "Url": "https://test.com/a.mp4",
                "TemplateId": 1,
                "CreateTime": "2020-01-01 08:00:00",
                "WaitDuration": 1,
                "MaxDuration": 1,
                "Type": 1
            }
        ],
        "RequestId": "1047d0dc-6dc8-4898-a7f3-03726a822b0e"
    }
}
```

