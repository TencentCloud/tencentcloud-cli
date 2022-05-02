**Example 1: 查询脚本模板**



Input: 

```
tccli pts DescribeScriptTemplates --cli-unfold-argument  \
    --OrderBy xx \
    --Ascend True \
    --Limit 1 \
    --Categories xx \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "ScriptTemplateSet": [
            {
                "Category": "xx",
                "Status": 1,
                "Name": "xx",
                "ScriptTemplateID": "xx",
                "Internal": true,
                "UpdatedAt": "2020-09-22T00:00:00+00:00",
                "Description": "xx",
                "CreatedAt": "2020-09-22T00:00:00+00:00",
                "EncodedContent": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

