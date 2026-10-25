**Example 1: 修改字段值替换规则**



Input: 

```
tccli rum ModifyTDEMFieldTransformRule --cli-unfold-argument  \
    --Id 31 \
    --AppId 11 \
    --TargetField user_id \
    --MatchType prefix \
    --MatchPattern test2_ \
    --TransformAction mask \
    --Name 修改名称 \
    --ReplaceValue * \
    --Enabled True
```

Output: 
```
{
    "Response": {
        "Rule": {
            "AppId": "11",
            "CreatedAt": "2026-09-22 11:16:06",
            "CreatedBy": "7**********6",
            "Enabled": true,
            "Id": 31,
            "MatchPattern": "test2_",
            "MatchType": "prefix",
            "Name": "修改名称",
            "Priority": 0,
            "ReplaceValue": "*",
            "TargetField": "user_id",
            "TransformAction": "mask",
            "UpdatedAt": "2026-09-22 11:22:38",
            "UpdatedBy": "7**********6"
        },
        "RequestId": "820f8d13-00a1-4998-918e-80e4bf657595"
    }
}
```

