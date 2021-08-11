**Example 1: 获取异步上下文任务结果**



Input: 

```
tccli cls DescribeAsyncContextResult --cli-unfold-argument  \
    --TopicId 682d0718-07bb-4ec0-9fda-f1e9a2767e0b \
    --AsyncContextTaskId ac-251fb2e2-3ac7-4f7b-827b-ad0cff8a22d2 \
    --PkgId 4C581DDA5FC70663-FDA78 \
    --PkgLogId 655363
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
        "PrevOver": true,
        "NextOver": true,
        "RequestId": "b276cb6e-4687-11eb-b378-0242ac130002"
    }
}
```

