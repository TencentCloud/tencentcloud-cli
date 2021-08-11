**Example 1: 获取异步上下文任务列表**



Input: 

```
tccli cls DescribeAsyncContextTasks --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "AsyncContextTasks": [
            {
                "LogsetId": "4463e7b0-3ec8-41a1-ae48-5d24b22167c2",
                "TopicId": "f28b17c8-d339-4547-bfff-0953b7901355",
                "CreateTime": 1623225367000,
                "FinishTime": 1623225367000,
                "Status": 1,
                "AsyncContextTaskId": "ac-251fb2e2-3ac7-4f7b-827b-ad0cff8a22d2",
                "AsyncSearchTaskId": "as-60a2e99b-24a5-4bc3-97b3-ffaac2f1c3eb",
                "PkgLogId": "644564",
                "Time": 1620986479000,
                "PkgId": "528C1318606EFEB8-1A7"
            }
        ],
        "TotalCount": 1,
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

