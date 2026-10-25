**Example 1: 查询字段值替换规则**



Input: 

```
tccli rum DescribeTDEMFieldTransformRules --cli-unfold-argument  \
    --AppId 11 \
    --Offset 0 \
    --Limit 200
```

Output: 
```
{
    "Response": {
        "FieldTransformRuleSet": [
            {
                "AppId": "11",
                "CreatedAt": "2026-09-22 11:16:06",
                "CreatedBy": "7**********6",
                "Enabled": true,
                "Id": 31,
                "MatchPattern": "test_",
                "MatchType": "prefix",
                "Name": "脱敏用户 ID",
                "Priority": 0,
                "ReplaceValue": "",
                "TargetField": "user_id",
                "TransformAction": "mask",
                "UpdatedAt": "2026-09-22 11:16:06",
                "UpdatedBy": "7**********6"
            }
        ],
        "TotalCount": 2,
        "RequestId": "ab1bbef2-387b-4df1-811f-79644a4c2ff6"
    }
}
```

