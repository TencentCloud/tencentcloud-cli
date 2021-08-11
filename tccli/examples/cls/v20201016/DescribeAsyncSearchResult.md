**Example 1: 获取异步检索任务结果**



Input: 

```
tccli cls DescribeAsyncSearchResult --cli-unfold-argument  \
    --TopicId 682d0718-07bb-4ec0-9fda-f1e9a2767e0b \
    --AsyncSearchTaskId as-65eff1fb-d552-4603-8966-03703e59188f \
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
                "LogJson": "{\"content\":\"test\"}",
                "FileName": "/root/test/nginx.log",
                "Source": "10.0.0.1",
                "Time": 1608794854001,
                "TopicName": "nginx-log",
                "PkgLogId": "655363"
            }
        ],
        "ListOver": true,
        "Context": "",
        "RequestId": "b276cb6e-4687-11eb-b378-0242ac130002"
    }
}
```

