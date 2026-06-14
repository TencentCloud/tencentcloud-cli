**Example 1: CreateSlowLogPatternDownloadTask**



Input: 

```
tccli mongodb CreateSlowLogPatternDownloadTask --cli-unfold-argument  \
    --InstanceId cmgo-dlm2vwnd \
    --StartTime 2026-05-27 12:00:00 \
    --EndTime 2026-05-27 14:00:00 \
    --ThresholdMs 100
```

Output: 
```
{
    "Response": {
        "Status": [
            0
        ],
        "RequestId": "cca56ed7-3e9d-4f92-8432-47198229b64a"
    }
}
```

