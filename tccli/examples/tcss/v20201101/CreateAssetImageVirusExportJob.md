**Example 1: 创建主机列表导出任务**



Input: 

```
tccli tcss CreateAssetImageVirusExportJob --cli-unfold-argument  \
    --Filters.0.Name RiskLevel \
    --Filters.0.Values 1 \
    --Filters.0.ExactMatch True \
    --Limit 1 \
    --Offset 1 \
    --By RiskLevel \
    --Order desc \
    --ExportField FileName RiskLevel Path Size VirusName Tags \
    --ImageID sha256:3cd27ee8bd44dc55e2efecf499e0e8c26216cf535c45891a9b1805fbc39d60a3
```

Output: 
```
{
    "Response": {
        "JobId": "8ddb3db7-6d50-48ee-bdcb-9cc37d49aa3c",
        "RequestId": "15cf63db-11a9-4885-b1a3-211dd54b83b7"
    }
}
```

