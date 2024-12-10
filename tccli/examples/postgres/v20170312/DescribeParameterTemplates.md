**Example 1: 查询参数模板信息**

无

Input: 

```
tccli postgres DescribeParameterTemplates --cli-unfold-argument  \
    --Filters.0.Name TemplateName \
    --Filters.0.Values my_custom_template \
    --Limit 0 \
    --Offset 10 \
    --OrderBy CreateTime \
    --OrderByType desc
```

Output: 
```
{
    "Response": {
        "ParameterTemplateSet": [
            {
                "DBEngine": "postgresql",
                "DBMajorVersion": "13",
                "TemplateDescription": "my template1",
                "TemplateId": "674538e8-4a03-5103-896c-9785c960bf02",
                "TemplateName": "my_custom_template"
            },
            {
                "DBEngine": "postgresql",
                "DBMajorVersion": "13",
                "TemplateDescription": "my template2",
                "TemplateId": "423984bb-97fe-5693-a74f-63cc8dfb6c5d",
                "TemplateName": "my_custom_template"
            }
        ],
        "RequestId": "6224e7ed-d7d8-494c-835f-e1612345383f",
        "TotalCount": 2
    }
}
```

