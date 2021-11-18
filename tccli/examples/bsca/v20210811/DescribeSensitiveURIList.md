**Example 1: 查询某个根域名下的敏感URI信息列表**



Input: 

```
tccli bsca DescribeSensitiveURIList --cli-unfold-argument  \
    --AnalysisId 4a49ab59-cea9-4d19-bed3-326a27465d92 \
    --RootDomain example.com
```

Output: 
```
{
    "Response": {
        "SensitiveDomainDetailSet": [
            {
                "Content": "http://www.example.com/path/to/files",
                "Count": 1,
                "FileList": [
                    {
                        "Name": "/ptah/demo_text",
                        "Type": "TEXT"
                    }
                ]
            }
        ],
        "RequestId": "7a8aaac8-8188-41c3-84cd-28e206671b4c"
    }
}
```

