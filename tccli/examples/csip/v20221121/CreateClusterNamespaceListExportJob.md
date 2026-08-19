**Example 1: 创建集群命名空间列表导出任务示例**



Input: 

```
tccli csip CreateClusterNamespaceListExportJob --cli-unfold-argument  \
    --ClusterCaMD5 a1b2c3d4e5f6789012345678901234ab \
    --Filter.Limit 20 \
    --Filter.Offset 0 \
    --ExportFields Name Labels CreateTime
```

Output: 
```
{
    "Response": {
        "JobId": "export-job-12345",
        "RequestId": "5cd96106-1d72-466c-9bcf-9876543210ab"
    }
}
```

