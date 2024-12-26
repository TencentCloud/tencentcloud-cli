**Example 1: 查询分组已绑定的插件列表**



Input: 

```
tccli tsf DescribePluginInstances --cli-unfold-argument  \
    --ScopeValue grp-v446jrhc \
    --Bound True \
    --Offset 0 \
    --Limit 10 \
    --Type QQMiniProgramLogin \
    --SearchWord pgnName
```

Output: 
```
{
    "Response": {
        "RequestId": "b6b81196-b506-4758-a2ea-80ee688cf3b3",
        "Result": {
            "Content": [
                {
                    "CreatedTime": "2023-11-28 16:11:28",
                    "Description": "This is desc",
                    "Id": "pgn-if8otbfp",
                    "Name": "pgnName",
                    "Status": "released",
                    "Type": "QQMiniProgramLogin",
                    "UpdatedTime": "2023-11-28 16:11:27"
                }
            ],
            "TotalCount": 1
        }
    }
}
```

