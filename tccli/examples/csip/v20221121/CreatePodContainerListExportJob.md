**Example 1: 创建Pod关联容器列表导出任务示例**



Input: 

```
tccli csip CreatePodContainerListExportJob --cli-unfold-argument  \
    --ClusterCaMD5 a1b2c3d4e5f6789012345678901234ab \
    --PodUniqueID pod-unique-id-12345 \
    --Filter.Filters.0.Name RunStatus \
    --Filter.Filters.0.Values Running \
    --ExportFields ContainerId ContainerName RunStatus NodeId NodeType ImageId ImageName IsolateStatus
```

Output: 
```
{
    "Response": {
        "JobId": "export-job-67890",
        "RequestId": "5cd96106-1d72-466c-9bcf-9876543210ab"
    }
}
```

