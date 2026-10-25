**Example 1: 创建字段值替换规则**



Input: 

```
tccli rum CreateTDEMFieldTransformRule --cli-unfold-argument  \
    --AppId 11 \
    --TargetField user_id \
    --MatchType prefix \
    --MatchPattern test_ \
    --TransformAction mask \
    --Name 脱敏用户 ID \
    --Enabled True
```

Output: 
```
{
    "Response": {
        "Rule": {
            "AppId": "11",
            "CreatedAt": "2026-09-22 11:16:11",
            "CreatedBy": "7**********6",
            "Enabled": true,
            "Id": 32,
            "MatchPattern": "test_",
            "MatchType": "prefix",
            "Name": "脱敏用户 ID",
            "Priority": 0,
            "ReplaceValue": "",
            "TargetField": "user_id",
            "TransformAction": "mask",
            "UpdatedAt": "2026-09-22 11:16:11",
            "UpdatedBy": "700001860566"
        },
        "RequestId": "19ea6869-84dd-44ca-9f49-a6edae4cec0a"
    }
}
```

