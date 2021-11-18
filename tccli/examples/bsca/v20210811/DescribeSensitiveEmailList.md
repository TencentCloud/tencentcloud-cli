**Example 1: 查询某个根域名下的敏感邮箱信息列表**



Input: 

```
tccli bsca DescribeSensitiveEmailList --cli-unfold-argument  \
    --AnalysisId 4a49ab59-cea9-4d19-bed3-326a27465d92 \
    --RootDomain gmail.com
```

Output: 
```
{
    "Response": {
        "SensitiveDomainDetailSet": [
            {
                "Content": "demo@gmail.com",
                "Count": 2,
                "FileList": [
                    {
                        "Name": "/path/demo_text",
                        "Type": "TEXT"
                    },
                    {
                        "Name": "/path/demo_binary",
                        "Type": "BINARY"
                    }
                ]
            }
        ],
        "RequestId": "c6f2c1dc-b48d-4c81-a324-eb12a47dc635"
    }
}
```

