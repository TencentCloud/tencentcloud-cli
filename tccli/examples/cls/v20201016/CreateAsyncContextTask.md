**Example 1: 创建异步上下文任务**



Input: 

```
tccli cls CreateAsyncContextTask --cli-unfold-argument  \
    --LogsetId 4463e7b0-3ec8-41a1-ae48-5d24b22167c2 \
    --TopicId 682d0718-07bb-4ec0-9fda-f1e9a2767e0b \
    --Time 1622454759000 \
    --PkgId 528C1318606EFEB8-1A7 \
    --PkgLogId 644564 \
    --AsyncSearchTaskId as-65eff1fb-d552-4603-8966-03703e59188f
```

Output: 
```
{
    "Response": {
        "AsyncContextTaskId": "ac-49ea31d0-1508-4528-8574-155442d1458a",
        "RequestId": "b276cb6e-4687-11eb-b378-0242ac130002"
    }
}
```

