**Example 1: 查询参数模板信息**

无

Input: 

```
tccli postgres DescribeParameterTemplates --cli-unfold-argument  \
    --OrderBy CreateTime \
    --OrderByType desc \
    --Limit 0 \
    --Filters.0.Values test \
    --Filters.0.Name TemplateName \
    --Offset 10
```

Output: 
```
{
    "Response": {
        "ParameterTemplateSet": [
            {
                "DBEngine": "postgresql",
                "DBMajorVersion": "13",
                "TemplateDescription": "test1",
                "TemplateId": "674538e8-4a03-5103-896c-9785c960bf02",
                "TemplateName": "test1"
            },
            {
                "DBEngine": "postgresql",
                "DBMajorVersion": "13",
                "TemplateDescription": "test2",
                "TemplateId": "423984bb-97fe-5693-a74f-63cc8dfb6c5d",
                "TemplateName": "test2"
            }
        ],
        "RequestId": "6224e7ed-d7d8-494c-835f-e1612345383f",
        "TotalCount": 2
    }
}
```

