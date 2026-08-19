**Example 1: 创建集群容器列表导出任务**



Input: 

```
tccli csip CreateClusterContainerListExportJob --cli-unfold-argument  \
    --Filter.Limit 10 \
    --Filter.Offset 0 \
    --ClusterCaMD5 d1f7e8a9b2c3d4e5f6a7b8c9d0e1f2a3
```

Output: 
```
{
    "Response": {
        "JobId": "job-abc123def456",
        "RequestId": "12345cef-0bf7-4020-a6e8-b1f1ae4de7e2"
    }
}
```

