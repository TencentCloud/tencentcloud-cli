**Example 1: 查询模板详情**

查询模板详情

Input: 

```
tccli wedata DescribeRuleTemplate --cli-unfold-argument  \
    --ProjectId 1 \
    --TemplateId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "UserName": "xx",
            "SourceEngineTypes": [
                1
            ],
            "UpdateTime": "xx",
            "Name": "xx",
            "MultiSourceFlag": true,
            "SourceObjectDataType": 1,
            "SourceContent": "xx",
            "UserId": 1,
            "CitationCount": 1,
            "WhereFlag": true,
            "QualityDim": 1,
            "RuleTemplateId": 1,
            "CompareType": 1,
            "SqlExpression": "xx",
            "Type": 1,
            "SourceObjectType": 1,
            "Description": "xx"
        },
        "RequestId": "xx"
    }
}
```

