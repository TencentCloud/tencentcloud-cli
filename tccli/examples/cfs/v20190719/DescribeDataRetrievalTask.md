**Example 1: 查询数据检索任务**

仅 Turbo 系列文件系统支持数据检索

Input: 

```
tccli cfs DescribeDataRetrievalTask --cli-unfold-argument  \
    --StartTime 2026-03-11 11:50:42 \
    --EndTime 2026-03-12 11:50:42 \
    --DataRetrievalId dataretrieval-589fa03c \
    --Offset 0 \
    --Limit 8
```

Output: 
```
{
    "Response": {
        "DataRetrievalTasks": [
            {
                "CompoundCondition": "from entries|where size &gt;4096",
                "CreateTime": "2026-03-12 11:05:15",
                "DataRetrievalId": "dataretrieval-589fa03c",
                "DataRetrievalTaskID": "dataretrievaltask-d54f5d2c",
                "DirNum": 0,
                "FileList": "",
                "FileNum": 0,
                "FileSystemId": "cfs-44b3b2f23",
                "QueryCondition": "from entries|where size &gt;4096",
                "Size": 0,
                "State": "waiting"
            }
        ],
        "TotalCount": 20,
        "RequestId": "6cf33841-7379-4801-9c6b-d55be465680f"
    }
}
```

