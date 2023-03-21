**Example 1: 查询备份概览**



Input: 

```
tccli postgres DescribeBackupOverview --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AutoBaseBackupCount": 494,
        "AutoBaseBackupSize": 25577154048,
        "LogBackupCount": 4677,
        "LogBackupSize": 89789143040,
        "ManualBaseBackupCount": 20,
        "ManualBaseBackupSize": 1002476032,
        "RequestId": "b4c5f18a-f917-46b4-8689-d4a64e3381fb",
        "TotalFreeSize": 13378823127040,
        "UsedBillingSize": 4329912320,
        "UsedFreeSize": 112038860800
    }
}
```

