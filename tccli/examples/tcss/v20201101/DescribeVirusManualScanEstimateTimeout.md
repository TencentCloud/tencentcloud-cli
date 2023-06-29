**Example 1: 查询木马一键检测预估超时时间**



Input: 

```
tccli tcss DescribeVirusManualScanEstimateTimeout --cli-unfold-argument  \
    --ScanIds xx \
    --ScanRangeAll True \
    --ScanRangeType 1
```

Output: 
```
{
    "Response": {
        "Timeout": 5,
        "ContainerScanConcurrencyCount": 2,
        "RequestId": "29b37d86-f63d-43d1-b21a-640e82965198"
    }
}
```

