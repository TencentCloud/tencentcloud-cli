**Example 1: 创建异步检索任务**



Input: 

```
tccli cls CreateAsyncSearchTask --cli-unfold-argument  \
    --LogsetId 4463e7b0-3ec8-41a1-ae48-5d24b22167c2 \
    --TopicId f28b17c8-d339-4547-bfff-0953b7901355 \
    --From 1608794854000 \
    --To 1608794855000 \
    --Query ERROR
```

Output: 
```
{
    "Response": {
        "RequestId": "b276cb6e-4687-11eb-b378-0242ac130002"
    }
}
```

