**Example 1: 创建数据引擎**

创建数据引擎

Input: 

```
tccli dlc CreateDataEngine --cli-unfold-argument  \
    --EngineType spark \
    --DataEngineName house_test \
    --ClusterType spark \
    --MinClusters 0 \
    --MaxClusters 0 \
    --DefaultDataEngine True \
    --CidrBlock 10.*.*.*/16 \
    --Mode 0 \
    --Message cretate house test \
    --AutoResume True \
    --Size 0 \
    --PayMode 0 \
    --TimeSpan 1 \
    --TimeUnit h \
    --AutoRenew 0 \
    --Tags.0.TagKey key \
    --Tags.0.TagValue value \
    --AutoSuspend True \
    --CrontabResumeSuspend 0 \
    --CrontabResumeSuspendStrategy.ResumeTime 10 \
    --CrontabResumeSuspendStrategy.SuspendTime 10 \
    --CrontabResumeSuspendStrategy.SuspendStrategy 0 \
    --EngineExecType BATCH \
    --MaxConcurrency 10 \
    --TolerableQueueTime 5 \
    --AutoSuspendTime 5 \
    --ResourceType spark_cu \
    --ImageVersionName SuperSQL-P 1.1
```

Output: 
```
{
    "Response": {
        "DataEngineId": "DataEngine-abc123",
        "RequestId": "7348577b-a168-467b-bd68-3c396b78b608"
    }
}
```

