**Example 1: 创建日志导出**



Input: 

```
tccli cls CreateExport --cli-unfold-argument  \
    --TopicId ee20bb16-3025-4048-b81a-dd436373062e \
    --Query status:200 \
    --Count 100 \
    --Order desc \
    --Format json \
    --From 1607499107000 \
    --To 1607499207000
```

Output: 
```
{
    "Response": {
        "ExportId": "57196a6a-7622-47be-bc92-d2ebea959a0f",
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

