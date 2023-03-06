**Example 1: 创建引擎**

创建引擎的

Input: 

```
tccli dlc CreateDataEngine --cli-unfold-argument  \
    --EngineType xx \
    --DataEngineName xx \
    --ClusterType xx \
    --MinClusters 0 \
    --MaxClusters 0 \
    --DefaultDataEngine True \
    --CidrBlock xx \
    --Mode 0 \
    --Message xx \
    --AutoResume True \
    --Size 0 \
    --PayMode 0 \
    --TimeSpan 0 \
    --TimeUnit xx \
    --AutoRenew 0 \
    --Tags.0.TagKey xx \
    --Tags.0.TagValue xx \
    --AutoSuspend True \
    --CrontabResumeSuspend 0 \
    --CrontabResumeSuspendStrategy.ResumeTime xx \
    --CrontabResumeSuspendStrategy.SuspendTime xx \
    --CrontabResumeSuspendStrategy.SuspendStrategy 0 \
    --EngineExecType xx \
    --MaxConcurrency 0 \
    --TolerableQueueTime 0 \
    --AutoSuspendTime 0 \
    --ResourceType xx \
    --ImageVersionName SuperSQL-P 1.1
```

Output: 
```
{
    "Response": {
        "DataEngineId": "xx",
        "RequestId": "xx"
    }
}
```

