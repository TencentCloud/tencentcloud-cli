**Example 1: 按时间范围查询任务列表**



Input: 

```
tccli tcb DescribeHTTPServiceCachePurgeTask --cli-unfold-argument  \
    --EnvId **********-1gz1k5qkc06a0da4 \
    --Domain *********************.cn \
    --StartTime 2026-09-02T09:10:51Z \
    --EndTime 2026-09-02T09:19:51Z
```

Output: 
```
{
    "Response": {
        "Tasks": [
            {
                "CacheType": "EO",
                "CreateTime": "2026-09-02T09:17:51Z",
                "Method": "DELETE",
                "PurgeType": "PURGE_URL",
                "Status": "SUCCESS",
                "Targets": [
                    "https://*********************.cn/cloudbaseenv.json"
                ],
                "TaskId": "3uijg0e6qmu2",
                "UpdateTime": "2026-09-02T09:18:00Z"
            }
        ],
        "TotalCount": 2,
        "RequestId": "94229944-e6d8-4d82-8ed2-9607e6ba4792"
    }
}
```

