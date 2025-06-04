**Example 1: 查询资产同步最近时间**



Input: 

```
tccli tcss DescribeAssetSyncLastTime --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AssetSyncLastTime": "2024-10-30 11:48:49",
        "TaskStatus": "PROCESSED",
        "TaskProcess": 10,
        "FailedHostCount": 10,
        "TaskId": 100,
        "RequestId": "c826b9fa-68b5-4603-bf25-a5eb918846666"
    }
}
```

