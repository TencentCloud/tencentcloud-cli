**Example 1: 故障切换**



Input: 

```
tccli bdrc RunFailoverCopyPairs --cli-unfold-argument  \
    --CopyPairIds cvmcopypair-ifytsjpr \
    --CopyPairType INSTANCE \
    --FailoverType NOW
```

Output: 
```
{
    "Response": {
        "TaskId": 12156,
        "RequestId": "abfb2ffc-c5eb-493f-892b-fd5e6e111cf6"
    }
}
```

