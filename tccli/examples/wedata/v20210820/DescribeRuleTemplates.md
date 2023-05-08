**Example 1: 查询规则模版列表**



Input: 

```
tccli wedata DescribeRuleTemplates --cli-unfold-argument  \
    --Type 1 \
    --SourceObjectType 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "SourceEngineTypes": [
                    1
                ],
                "QualityDim": 1,
                "SourceObjectDataType": 1,
                "SourceContent": "xx",
                "CitationCount": 1,
                "RuleTemplateId": 1,
                "CompareType": 1,
                "Name": "xx",
                "Type": 1,
                "SourceObjectType": 1,
                "Description": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

