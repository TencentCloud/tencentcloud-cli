**Example 1: 获取用户词库列表**

获取用户词库列表

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
    --Filters.0.Values Lib123
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Infos": [
            {
                "ID": "123xxx",
                "LibName": "Lib123",
                "Describe": "Lib123",
                "CreateTime": "2022-06-30 15:32:58",
                "Suggestion": "pass",
                "MatchType": "default",
                "BizTypes": [
                    "biztype1"
                ]
            }
        ],
        "RequestId": "123xxx-234xxx-345xxx"
    }
}
```

