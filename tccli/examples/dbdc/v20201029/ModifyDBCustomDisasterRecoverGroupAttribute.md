**Example 1: 修改 DB Custom 置放群组的名称和亲和性**



Input: 

```
tccli dbdc ModifyDBCustomDisasterRecoverGroupAttribute --cli-unfold-argument  \
    --DisasterRecoverGroupId dbps-81aqu2cs \
    --Name 置放群组CD1 \
    --Affinity 6
```

Output: 
```
{
    "Response": {
        "TaskId": 2503,
        "RequestId": "76229e50-bdae-4ae9-a630-e1a98bdcd4c4"
    }
}
```

