**Example 1: 获取异步检索任务列表**



Input: 

```
tccli cls DescribeAsyncSearchTasks --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "AsyncSearchTasks": [
            {
                "LogsetId": "4463e7b0-3ec8-41a1-ae48-5d24b22167c2",
                "TopicId": "f28b17c8-d339-4547-bfff-0953b7901355",
                "CreateTime": "2021-04-02 08:00:00",
                "Status": 1,
                "AsyncSearchTaskId": "as-251fb2e2-3ac7-4f7b-827b-ad0cff8a22d2",
                "Query": "ERROR",
                "From": 1620986479000,
                "To": 1620986480000,
                "Sort": "asc"
            }
        ],
        "TotalCount": 1,
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

