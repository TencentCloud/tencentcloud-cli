**Example 1: 查询参数模板信息**



Input: 

```
tccli cynosdb DescribeParamTemplates --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Items": [
            {
                "Id": 1234,
                "TemplateName": "test",
                "TemplateDescription": "useforttest",
                "EngineVersion": "5.7"
            }
        ],
        "RequestId": "xxx"
    }
}
```

