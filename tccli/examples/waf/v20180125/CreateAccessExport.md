**Example 1: 创建访问日志导出**



Input: 

```
tccli waf CreateAccessExport --cli-unfold-argument  \
    --TopicId 1ae37c76-df99-4e2b-998c-20f39eba6226 \
    --From 1625395948532 \
    --To 1626000748532 \
    --Count 6221 \
    --Query * \
    --Order desc \
    --Format json
```

Output: 
```
{
    "Response": {
        "ExportId": "export-61daca5c-f341-4796-aeb3-4f2f598a06c7",
        "RequestId": "9b02bf9e-c89c-42c3-9ae1-685f968fa02d"
    }
}
```

