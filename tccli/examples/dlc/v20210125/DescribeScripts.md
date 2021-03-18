**Example 1: 获取所有sql查询**



Input: 

```
tccli dlc DescribeScripts --cli-unfold-argument  \
    --Sorting xx \
    --Limit 0 \
    --SortBy xx \
    --Filters.0.Values xx \
    --Filters.0.Name xx \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "xx",
        "Scripts": [
            {
                "UpdateTime": 0,
                "DatabaseName": "xx",
                "ScriptName": "xx",
                "ScriptDesc": "xx",
                "SQLStatement": "xx",
                "ScriptId": "xx"
            }
        ]
    }
}
```

