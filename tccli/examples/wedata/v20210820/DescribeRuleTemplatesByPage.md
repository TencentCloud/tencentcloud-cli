**Example 1: 规则模版列表**



Input: 

```
tccli wedata DescribeRuleTemplatesByPage --cli-unfold-argument  \
    --OrderFields.0.Name xxx \
    --OrderFields.0.Direction xxxx \
    --Filters.0.Values xx \
    --Filters.0.Name xx \
    --ProjectId 1 \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 1,
            "Items": [
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
            ]
        },
        "RequestId": "xx"
    }
}
```

