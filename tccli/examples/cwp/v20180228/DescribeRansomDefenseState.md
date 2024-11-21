**Example 1: 获取用户防勒索趋势**

获取用户防勒索趋势

Input: 

```
tccli cwp DescribeRansomDefenseState --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "MachineCount": 1,
        "SnapshotSize": 1,
        "ProgressingSnapshotTaskCount": 1,
        "RollBackTaskCount": 1,
        "StrategyCount": 1,
        "StrategyTotal": 1,
        "MachineTotal": 1,
        "RequestId": "935e27b1-d675-4509-80bf-96fbf0764237",
        "BalanceStatus": 1,
        "BackupMachineCount": 1,
        "ProgressingRollBackTaskCount": 1
    }
}
```

