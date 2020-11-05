**Example 1: Querying the Check Result of a Disaster Recovery Sync Task**



Input: 

```
tccli dts DescribeSyncCheckJob --cli-unfold-argument  \
    --JobId sync-blj8wnt1
```

Output: 
```
{
    "Response": {
        "Status": "finished",
        "ErrorCode": 0,
        "ErrorMessage": "Disaster recovery check succeeded",
        "StepInfo": [
            {
                "StepNo": 1,
                "StepName": "Check the parameters",
                "StepCode": 0,
                "StepMessage": "Check succeeded"
            },
            {
                "StepNo": 2,
                "StepName": "Check the source instance",
                "StepCode": 0,
                "StepMessage": "Check succeeded"
            },
            {
                "StepNo": 3,
                "StepName": "Check the target instance",
                "StepCode": 0,
                "StepMessage": "Check succeeded"
            },
            {
                "StepNo": 4,
                "StepName": "Check the instance status",
                "StepCode": 0,
                "StepMessage": "Check succeeded"
            },
            {
                "StepNo": 5,
                "StepName": "Check the instance specification",
                "StepCode": 0,
                "StepMessage": "Check succeeded"
            },
            {
                "StepNo": 6,
                "StepName": "Check the instance version",
                "StepCode": 0,
                "StepMessage": "Check succeeded"
            },
            {
                "StepNo": 7,
                "StepName": "Check whether the target instance is empty",
                "StepCode": 0,
                "StepMessage": "Check succeeded"
            },
            {
                "StepNo": 8,
                "StepName": "Check whether encryption is enabled",
                "StepCode": 0,
                "StepMessage": "Check succeeded"
            },
            {
                "StepNo": 9,
                "StepName": "Check the synced table information of the instance",
                "StepCode": 0,
                "StepMessage": "Check succeeded"
            },
            {
                "StepNo": 10,
                "StepName": "Check the cold backup data of the instance",
                "StepCode": 0,
                "StepMessage": "Check succeeded"
            }
        ],
        "CheckFlag": 1,
        "RequestId": "b3951c71-1da4-4b8f-9de5-ad71ab1e2917"
    }
}
```

