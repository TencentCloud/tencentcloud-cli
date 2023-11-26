**Example 1: 查询作业配置**

查询指定的作业配置

Input: 

```
tccli oceanus DescribeJobConfigs --cli-unfold-argument  \
    --JobId cql-ahnkqtay \
    --WorkSpaceId space-1257058945ap-guangzhou
```

Output: 
```
{
    "Response": {
        "JobConfigSet": [
            {
                "AutoRecover": 1,
                "COSBucket": "autotest-gz-bucket-1257058945",
                "CheckpointRetainedNum": 0,
                "ClazzLevels": [],
                "ClsLogsetId": "",
                "ClsTopicId": "",
                "CreateTime": "2023-10-20 10:55:12",
                "CreatorUin": "100032959577",
                "DefaultParallelism": 1,
                "EntrypointClass": "",
                "ExpertModeOn": false,
                "JobId": "cql-ahnkqtay",
                "JobManagerSpec": 1,
                "LogCollect": 4,
                "LogLevel": "INFO",
                "MaxParallelism": 2048,
                "ProgramArgs": "{\"CheckpointInterval\":600,\"Metadata\":\"{\\\"Metadata\\\":{\\\"ReferenceTables\\\":[],\\\"Variables\\\":[]}}\",\"SqlCode\":\"-- Datagen Connector 可以随机生成一些数据用于测试\\n-- 参见 https://cloud.tencent.com/document/product/849/58713\\nCREATE TABLE datagen_source_table_b ( \\n    id INT, \\n    name STRING \\n) WITH ( \\n    'connector' = 'datagen',\\n    'rows-per-second'='1'  -- 每秒产生的数据条数\\n);\\n\\n\\n-- 输入到 Blackhole Sink 的数据, 会被全部丢弃。这个 Sink 适合做性能测试。\\n-- 参见 https://ci.apache.org/projects/flink/flink-docs-release-1.11/zh/dev/table/connectors/blackhole.html\\nCREATE TABLE blackhole_sink_b ( \\n    id INT, \\n    name STRING \\n) WITH ( \\n    'connector' = 'blackhole'\\n);\\n\\nINSERT INTO blackhole_sink_b SELECT * FROM datagen_source_table_b;\\n\\n\\n\"}",
                "Properties": [
                    {
                        "Key": "pipeline.max-parallelism",
                        "Value": "2048"
                    }
                ],
                "PythonVersion": "",
                "Remark": "v1",
                "ResourceRefDetails": null,
                "TaskManagerSpec": 1,
                "TraceModeConfiguration": null,
                "TraceModeOn": false,
                "UpdateTime": "2023-11-13 17:19:04",
                "Version": 1
            }
        ],
        "RequestId": "21ac3206-2b1a-4095-93cd-ceed11cf5379",
        "TotalCount": 1
    }
}
```

