**Example 1: CancelEdrAlertIgnore**



Input: 

```
tccli csip CancelEdrAlertIgnore --cli-unfold-argument  \
    --Targets.0.Id 2000000106409 \
    --Targets.0.AppId 260083796 \
    --Targets.0.AlertId 225ea956c3c07197e342bf82c3400ac2 \
    --MemberId mem-*********************429
```

Output: 
```
{
    "Response": {
        "CancelledCount": 1,
        "RequestId": "1b3cd4cc-9cb2-4fb4-bcbf-69d40ab12b32"
    }
}
```

