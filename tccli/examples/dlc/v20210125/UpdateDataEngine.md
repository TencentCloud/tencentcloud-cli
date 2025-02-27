**Example 1: 引擎变配**

引擎变配

Input: 

```
tccli dlc UpdateDataEngine --cli-unfold-argument  \
    --MaxClusters 0 \
    --CrontabResumeSuspend 0 \
    --AutoSuspend True \
    --CrontabResumeSuspendStrategy.SuspendTime 0 \
    --CrontabResumeSuspendStrategy.SuspendStrategy 0 \
    --CrontabResumeSuspendStrategy.ResumeTime 0 \
    --AutoResume True \
    --DataEngineName engine_presto \
    --Message modify \
    --MinClusters 0 \
    --Size 0
```

Output: 
```
{
    "Response": {
        "RequestId": "8eb4c0da-bf0d-4e63-859e-62378668bdaa"
    }
}
```

