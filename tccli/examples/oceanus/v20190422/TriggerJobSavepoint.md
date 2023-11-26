**Example 1: 触发快照**



Input: 

```
tccli oceanus TriggerJobSavepoint --cli-unfold-argument  \
    --JobId cql-52xkpymp
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "",
        "FinalSavepointPath": "",
        "SavepointTrigger": true,
        "RequestId": "cc75a49d-a99b-4840-b3cb-7d3bdd9a0e33",
        "SavepointId": "svp-asdf5678"
    }
}
```

