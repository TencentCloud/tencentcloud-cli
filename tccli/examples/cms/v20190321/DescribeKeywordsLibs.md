**Example 1: 获取用户词库列表**

获取用户词库列表

Input: 

```
tccli cms DescribeKeywordsLibs --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --Filters.0.Name LibName \
    --Filters.0.Values test
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Infos": [
            {
                "ID": "abc",
                "LibName": "abc",
                "Describe": "abc",
                "CreateTime": "abc",
                "Suggestion": "abc",
                "MatchType": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

