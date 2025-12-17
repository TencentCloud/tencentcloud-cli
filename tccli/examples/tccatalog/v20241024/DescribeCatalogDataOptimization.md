**Example 1: DescribeCatalogDataOptimization**

查询catalog级数据优化

Input: 

```
tccli tccatalog DescribeCatalogDataOptimization --cli-unfold-argument  \
    --CatalogName justtestdlc \
    --StartTime 2025-06-25 10:00:00 \
    --EndTime 2025-06-25 10:00:00
```

Output: 
```
{
    "Response": {
        "RequestId": "e634125c-b612-471a-90a2-d85a4e368ab2",
        "TaskCount": 24,
        "FileCount": 512,
        "DataCount": 512,
        "BeforeAverageFileSize": 512,
        "AfterAverageFileSize": 256
    }
}
```

