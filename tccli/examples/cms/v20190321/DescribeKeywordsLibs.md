**Example 1: 获取用户词库列表**



Input: 

```
tccli cms DescribeKeywordsLibs --cli-unfold-argument  \
    --UserAppID 123 \
    --UserSubUin 123 \
    --Limit 10 \
    --Offset 0 \
    --UserUin 123 \
    --Type Text \
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
                "LibName": "xx",
                "Describe": "xx",
                "ID": "xx",
                "Suggestion": "xx",
                "MatchType": "xx",
                "CreateTime": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

**Example 2: 查询词库示例**



Input: 

```
tccli cms DescribeKeywordsLibs --cli-unfold-argument  \
    --UserAppID 123 \
    --UserSubUin 123 \
    --Limit 10 \
    --Offset 0 \
    --UserUin 123 \
    --Type Text \
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
                "LibName": "xx",
                "Describe": "xx",
                "ID": "xx",
                "Suggestion": "xx",
                "MatchType": "xx",
                "CreateTime": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

