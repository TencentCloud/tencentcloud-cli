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
                "ScriptId": "2c15fe4e-9a71-443a-a079-10b681cd173c",
                "ScriptName": "createScript_autotest",
                "ScriptDesc": "2c15fe4e-9a71-443a-a079-10b681cd173c",
                "DatabaseName": "dlc_database",
                "SQLStatement": "select* from abc",
                "UpdateTime": 0
            }
        ],
        "TotalCount": 0,
        "RequestId": "2c15fe4e-9a71-443a-a079-10b681cd173c"
    }
}
```

