**Example 1: 创建Pod关联服务列表导出任务示例**



Input: 

```
tccli csip CreatePodServiceListExportJob --cli-unfold-argument  \
    --PodUniqueID pod-unique-id-12345 \
    --Filter.Filters.0.Name ServiceType \
    --Filter.Filters.0.Values LoadBalancer \
    --ExportFields Name ServiceType Selector Namespace CreateTime
```

Output: 
```
{
    "Response": {
        "JobId": "export-job-99999",
        "RequestId": "5cd96106-1d72-466c-9bcf-9876543210ab"
    }
}
```

