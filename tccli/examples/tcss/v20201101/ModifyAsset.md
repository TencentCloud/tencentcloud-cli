**Example 1: 主机资产刷新**



Input: 

```
tccli tcss ModifyAsset --cli-unfold-argument  \
    --All True \
    --AllSuperHost True \
    --TimeoutSec 3600
```

Output: 
```
{
    "Response": {
        "RequestId": "33ec689a-e026-4700-8dc4-b559b97f0667",
        "Status": "SUCCESS",
        "TaskId": 10086
    }
}
```

