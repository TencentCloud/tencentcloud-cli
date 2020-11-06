**Example 1: Scheduling deletion**

This example shows you how to delete a specified CMK on the 7th day upon schedule deletion.

Input: 

```
tccli kms ScheduleKeyDeletion --cli-unfold-argument  \
    --KeyId "23e80852-1e38-11e9-b129-5cb9019b4b01" \
    --PendingWindowInDays 7
```

Output: 
```
{
    "Response": {
        "DeletionDate": 1559318399,
        "KeyId": "23e80852-1e38-11e9-b129-5cb9019b4b01"
    }
}
```

