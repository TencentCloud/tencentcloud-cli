**Example 1: 获取所有sql查询**



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
        "RequestId": "5ebcba6f-38bf-4023-80d0-2023d51e9b1e",
        "Scripts": [
            {
                "ScriptId": "644980fb-09f3-467a-847f-b9d628c9663d",
                "UpdateTime": 1630498019026,
                "ScriptName": "Script1",
                "ScriptDesc": "create by nick",
                "SQLStatement": "SELECT * FROM `testdb`.`table1` LIMIT 10",
                "DatabaseName": ""
            }
        ],
        "TotalCount": 3
    }
}
```

