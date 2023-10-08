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
    --DataEngineName test \
    --Message modify \
    --MinClusters 0 \
    --Size 0
```

Output: 
```
{
    "Response": {
        "RequestId": "xx-xxxx-xxx-xxxx"
    }
}
```

