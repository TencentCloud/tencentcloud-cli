**Example 1: 查询分组已绑定的插件列表**



Input: 

```
tccli tsf DescribePluginInstances --cli-unfold-argument  \
    --ScopeValue grp-83wrlmav \
    --Bound true \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "fa153f44-22b6-4ea3-86ef-6e257d440f26",
        "Result": {
            "TotalCount": 1,
            "Content": [
                {
                    "Id": "pgn-33pk2soi",
                    "Name": "Tag认证插件",
                    "Type": "Tag",
                    "Description": "this is description",
                    "CreatedTime": "2019-11-02 15:43:09",
                    "UpdatedTime": "2019-11-02 17:30:51",
                    "Status": "drafted"
                }
            ]
        }
    }
}
```

