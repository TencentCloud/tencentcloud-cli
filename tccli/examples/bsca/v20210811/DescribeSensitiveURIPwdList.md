**Example 1: 查询敏感URI文件列表**



Input: 

```
tccli bsca DescribeSensitiveURIPwdList --cli-unfold-argument  \
    --AnalysisId 4a49ab59-cea9-4d19-bed3-326a27465d92 \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "SensitiveFileSet": [
            {
                "File": {
                    "Name": "/path/demo_text",
                    "Type": "TEXT"
                },
                "SubClass": "Password in URI",
                "ContentList": [
                    "http://user:pass@test.com"
                ]
            }
        ],
        "FieldValuesSet": [],
        "TotalCount": 1,
        "RequestId": "936d5f0e-4746-4c61-a746-fa35e6bb3b54"
    }
}
```

