**Example 1: 创建数据检索策略**

仅 Turbo 系列文件系统支持数据检索

Input: 

```
tccli cfs CreateDataRetrieval --cli-unfold-argument  \
    --FileSystemId cfs-4e5e76ff8 \
    --DataRetrievalName default \
    --DayOfWeek 3,4 \
    --Hour 12,13
```

Output: 
```
{
    "Response": {
        "DataRetrievalId": "dataretrieval-1234bdbc",
        "RequestId": "b3df3eb8-cd14-4c0a-8b8d-11a7ad082b40"
    }
}
```

