**Example 1: 获取设备动作历史**



Input: 

```
tccli iotvideo DescribeDeviceActionHistory --cli-unfold-argument  \
    --ProductId TDCZ2WD29Z \
    --DeviceName autotest_33842121_13 \
    --MinTime 1612235884839 \
    --MaxTime 1612237684839
```

Output: 
```
{
    "Response": {
        "ActionHistories": [],
        "Context": "DnF1ZXJ5VGhlbkZldGNoBQAAAAAAgnMbFnZpOEh2MVNWUm95SjdoYTNGUGtGR1EAAAAAAJNMzBZwaXcxNlFBOFJWdVJxbU44SHlfNUx3AAAAAABDhPQWaUdjOWIxWTBUQ3lWNGxVOC1CeGQ5ZwAAAAAAgpygFkNOenVGZk81UVVHWksxYXhDdXl4M1EAAAAAAF9k3BZfQkg2bHZxNVJDaW5id1N5XzU1Rl9B",
        "Listover": false,
        "RequestId": "1f6b8618-7fdf-4983-90b8-2816a1ea25dd",
        "TotalCounts": 0
    }
}
```

