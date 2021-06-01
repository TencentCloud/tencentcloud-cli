**Example 1: 查询日志**



Input: 

```
tccli cls SearchLog --cli-unfold-argument  \
    --TopicId 682d0718-07bb-4ec0-9fda-f1e9a2767e0b \
    --From 1608794854000 \
    --To 1608794855000 \
    --Query http_status:200 \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "Results": [
            {
                "PkgId": "4C581DDA5FC70663-FDA78",
                "TopicId": "682d0718-07bb-4ec0-9fda-f1e9a2767e0b",
                "FileName": "/root/test/nginx.log",
                "Source": "10.0.0.1",
                "Time": 1608794854001,
                "TopicName": "nginx-log",
                "PkgLogId": "655363"
            }
        ],
        "Analysis": false,
        "ListOver": true,
        "Context": "",
        "AnalysisResults": [
            {
                "Data": [
                    {
                        "Value": "xx",
                        "Key": "xx"
                    }
                ]
            }
        ],
        "ColNames": [],
        "RequestId": "b276cb6e-4687-11eb-b378-0242ac130002"
    }
}
```

