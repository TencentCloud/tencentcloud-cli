**Example 1: 查询脚本模板**



Input: 

```
tccli pts DescribeScriptTemplates --cli-unfold-argument  \
    --OrderBy name \
    --Ascend True \
    --Limit 1 \
    --Categories http \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "ScriptTemplateSet": [
            {
                "Category": "http",
                "Status": 1,
                "Name": "abc",
                "ScriptTemplateID": "123",
                "Internal": true,
                "UpdatedAt": "2020-09-22T00:00:00+00:00",
                "Description": "test",
                "CreatedAt": "2020-09-22T00:00:00+00:00",
                "EncodedContent": "test"
            }
        ],
        "RequestId": "c2lcbdvsgxaoc7yp5dxveh3mtpf27c4o"
    }
}
```

