**Example 1: 创建集群节点列表导出任务示例**



Input: 

```
tccli csip CreateClusterNodeListExportJob --cli-unfold-argument  \
    --ClusterCaMD5 a1b2c3d4e5f6789012345678901234ab \
    --Filter.Filters.0.Name ClientStatus \
    --Filter.Filters.0.Values ONLINE \
    --ExportFields NodeId NodeName PublicIP InternalIP NodeType CoresCount ClientStatus RunStatus
```

Output: 
```
{
    "Response": {
        "JobId": "export-job-node-12345",
        "RequestId": "5cd96106-1d72-466c-9bcf-9876543210ab"
    }
}
```

