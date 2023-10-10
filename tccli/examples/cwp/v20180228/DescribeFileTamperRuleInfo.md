**Example 1: 示例**



Input: 

```
tccli cwp DescribeFileTamperRuleInfo --cli-unfold-argument  \
    --Id 1
```

Output: 
```
{
    "Response": {
        "FileTamperRuleDetail": {
            "Status": 1,
            "Name": "xx",
            "Level": 1,
            "IsGlobal": 1,
            "Rule": [
                {
                    "Action": "xx",
                    "ProcessPath": "xx",
                    "Target": "xx"
                }
            ],
            "Id": 1,
            "Uuids": [
                "xx"
            ],
            "ModifyTime": "xx",
            "CreateTime": "xx"
        },
        "RequestId": "sdfiajei2x7878fa7vjs"
    }
}
```

