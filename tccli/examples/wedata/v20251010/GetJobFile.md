**Example 1: 获取自定义文件内容**



Input: 

```
tccli wedata GetJobFile --cli-unfold-argument  \
    --WorkspaceId 17623497097012366 \
    --JobId 6820260120165151013 \
    --FileName metrics.log \
    --Offset 0 \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "Data": {
            "Content": [
                "{\"writeSucceedRecords\": 8, \"readSucceedRecords\": 8, \"writeSucceedBytes\": 8, \"byteSpeed\": 0, \"waitReaderTime\": 0, \"duration\": 80, \"sourceDatasource\": \"dashboard.t_chat_table\", \"runEndTime\": 1768899239586, \"waitWriterTime\": 62215, \"percentage\": 1, \"totalReadRecords\": 8, \"writeReceivedRecords\": 8, \"readSucceedBytes\": 8, \"timestamp\": 1768899239653, \"totalErrorBytes\": 0, \"sinkDatasource\": \"c4.ss.tb2\", \"ddl\": \"\", \"totalErrorRecords\": 0, \"recordSpeed\": 0, \"jobId\": \"6820260120165151013\", \"runStartTime\": 1768899159366, \"writeReceivedBytes\": 8, \"stage\": 1, \"totalReadBytes\": 8, \"status\": \"SUCCEEDED\"}"
            ],
            "NextOffset": 597
        },
        "RequestId": "29b03329-d4ea-4047-b2e0-2a662110c98f"
    }
}
```

