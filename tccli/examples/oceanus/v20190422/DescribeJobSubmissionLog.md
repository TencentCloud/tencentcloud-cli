**Example 1: 查询启动日志**

查询启动日志

Input: 

```
tccli oceanus DescribeJobSubmissionLog --cli-unfold-argument  \
    --JobId cql-067opv7l \
    --RunningOrderId 1 \
    --StartTime 1698044059122 \
    --EndTime 1698045059131
```

Output: 
```
{
    "Response": {
        "Cursor": "",
        "JobInstanceList": null,
        "JobRequestId": "9acab4fc-d101-47ca-96a6-da08fe3fc130",
        "ListOver": true,
        "LogContentList": [
            {
                "ContainerName": "",
                "Log": "2023-10-23 14:54:18.158 [pool-1-thread-14] INFO  org.apache.flink.kubernetes.utils.KubernetesUtils  - Kubernetes deployment requires a fixed port. Configuration blob.server.port will be set to 6124",
                "PkgId": "",
                "PkgLogId": 0,
                "Time": 1698044059131
            },
            {
                "ContainerName": "",
                "Log": "2023-10-23 14:54:18.158 [pool-1-thread-14] INFO  org.apache.flink.kubernetes.utils.KubernetesUtils  - Kubernetes deployment requires a fixed port. Configuration taskmanager.rpc.port will be set to 6122",
                "PkgId": "",
                "PkgLogId": 0,
                "Time": 1698044059131
            },
            {
                "ContainerName": "",
                "Log": "2023-10-23 14:54:18.590 [pool-1-thread-14] INFO  com.qcloud.oceanus.ca.service.RunJobService  - Finish invoking clusterClient.run (run job)",
                "PkgId": "",
                "PkgLogId": 0,
                "Time": 1698044059132
            }
        ],
        "LogList": [
            "2020-04-08 11:58:35.048 [queuedThreadPool-57106 dfd73175-f8d4-4981-8cd3-8072e0a52fbd cql-ebgioapf 4 20200408115835048] WARN  org.apache.flink.streaming.connectors.kafka.FlinkKafkaProducerBase  - Overwriting the key.serializer is not recommended"
        ],
        "RequestId": "9270beec-295b-42dd-836b-11ec47b6bff7"
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
        "LogContentList": [
            {
                "Log": "2023-09-11 15:37:23.094 [jobmanager-future-thread-4] INFO  org.apache.flink.runtime.checkpoint.CheckpointCoordinator - Completed checkpoint 2767 for job 00000000000000000000000000000000 (0 bytes in 269 ms).",
                "Time": 1694417844009,
                "PkgId": "11CBB7C1649A91DD-1741",
                "PkgLogId": 131073,
                "ContainerName": "cql-07zmx8tv-318940-64f4dbfcb6-vtf67"
            }
        ],
        "RequestId": "db79c5af-adba-484b-8cf0-775e0b0b8070"
    }
}
```

