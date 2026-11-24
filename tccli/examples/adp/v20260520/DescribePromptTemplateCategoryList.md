**Example 1: 查询提示词模板分类列表**



Input: 

```
tccli adp DescribePromptTemplateCategoryList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "CategoryGroupList": [
            {
                "CategoryList": [
                    {
                        "Key": "PromptTemplateTypeMultiAgent",
                        "Name": "Multi-Agent模式"
                    }
                ],
                "Module": "PromptTemplateModeMultiAgent"
            }
        ],
        "RequestId": "31beecd9-9859-4cf1-b25b-392eee422155"
    }
}
```

