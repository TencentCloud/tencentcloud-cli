**Example 1: DescribeFieldTransformRules示例**



Input: 

```
tccli rum DescribeFieldTransformRules --cli-unfold-argument  \
    --ProjectId 146662 \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "Result": "{\"FieldTransformRuleSet\":[{\"CreatedAt\":\"2026-04-11T14:32:25Z\",\"CreatedBy\":\"600000563898\",\"Enabled\":true,\"Id\":1,\"MatchPattern\":\"abc\",\"MatchType\":\"contains\",\"Name\":\"abc\",\"Priority\":0,\"ProjectId\":146662,\"ReplaceValue\":\"ddd\",\"TargetField\":\"page_url\",\"TransformAction\":\"replace\",\"UpdatedAt\":\"2026-04-11T14:40:52Z\",\"UpdatedBy\":\"600000563898\"},{\"CreatedAt\":\"2026-04-11T14:35:00Z\",\"CreatedBy\":\"600000563898\",\"Enabled\":true,\"Id\":2,\"MatchPattern\":\"abcde\",\"MatchType\":\"contains\",\"Name\":\"page_url包含abc替换为xxx\",\"Priority\":0,\"ProjectId\":146662,\"ReplaceValue\":\"xxxx\",\"TargetField\":\"page_url\",\"TransformAction\":\"replace\",\"UpdatedAt\":\"2026-04-11T14:35:00Z\",\"UpdatedBy\":\"600000563898\"}],\"TotalCount\":2}",
        "RequestId": "01d1fd6f-99d9-40b3-9c83-14ce72fbf096"
    }
}
```

