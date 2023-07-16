**Example 1: 查询作业启动日志**



Input: 

```
tccli oceanus DescribeJobSubmissionLog --cli-unfold-argument  \
    --JobId cql-ebgioapf \
    --RunningOrderId 0 \
    --StartTime 1586284444 \
    --EndTime 1586327659 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "JobInstanceList": [
            {
                "StartingMillis": 0,
                "RunningOrderId": 4,
                "JobInstanceStartTime": "xx"
            },
            {
                "StartingMillis": 60000,
                "RunningOrderId": 2,
                "JobInstanceStartTime": "xx"
            },
            {
                "StartingMillis": 60000,
                "RunningOrderId": 1,
                "JobInstanceStartTime": "xx"
            }
        ],
        "LogList": [
            "2020-04-08 11:58:35.048 [queuedThreadPool-57106 dfd73175-f8d4-4981-8cd3-8072e0a52fbd cql-ebgioapf 4 20200408115835048] WARN  org.apache.flink.streaming.connectors.kafka.FlinkKafkaProducerBase  - Overwriting the key.serializer is not recommended"
        ],
        "ListOver": false,
        "LogContentList": [
            {
                "PkgId": "xx",
                "PkgLogId": 0,
                "Log": "xx",
                "Time": 0
            }
        ],
        "Cursor": "xx",
        "RequestId": "xx",
        "JobRequestId": "xx"
    }
}
```

**Example 2: 查询指定job实例的启动日志**

持续加载数据

Input: 

```
tccli oceanus DescribeJobSubmissionLog --cli-unfold-argument  \
    --JobId cql-ebgioapf \
    --RunningOrderId 1 \
    --StartTime 1586284444 \
    --EndTime 1586327659 \
    --Cursor Y29udGV4dC0xMzcyM2NmZi03YjAyLTQ2MTgtYWJiOC0zYWQ5ZmU3MzIxMGUxNTg2MzI3OTk0NjEx \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "Cursor": "Y29udGV4dC1hNTI3ZmVhYy01YmE0LTQ5MWMtYjAwZS1kZGQwZWEwZWU2NDAxNTg2MzI4MTQ4Nzkw",
        "JobInstanceList": [],
        "JobRequestId": "dfd73175-f8d4-4981-8cd3-8072e0a52fbd",
        "ListOver": false,
        "LogList": [
            "2020-04-08 11:57:32.703 [queuedThreadPool-57106 dfd73175-f8d4-4981-8cd3-8072e0a52fbd cql-ebgioapf 1 20200408115732703] INFO  com.tencent.cloud.tstream.flink.toolbox.sql.parse.settings.SettingManager  - Registered Setting Handler CHECKPOINT_INTERVAL to CheckpointIntervalHandler for POST_PROCESSING"
        ],
        "RequestId": "db79c5af-adba-484b-8cf0-775e0b0b8070"
    }
}
```

