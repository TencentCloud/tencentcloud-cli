**Example 1: 查询SQL脚本列表**

查询SQL脚本列表

Input: 

```
tccli dlc DescribeScripts --cli-unfold-argument  \
    --Sorting update-time \
    --Limit 1 \
    --SortBy desc \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Scripts": [
            {
                "ScriptId": "abc",
                "ScriptName": "abc",
                "ScriptDesc": "abc",
                "DatabaseName": "abc",
                "SQLStatement": "abc",
                "UpdateTime": 0
            }
        ],
        "TotalCount": 0,
        "RequestId": "abc"
    }
}
```

