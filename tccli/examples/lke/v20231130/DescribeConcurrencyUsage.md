**Example 1: 并发详情示例**

并发详情示例

Input: 

```
tccli lke DescribeConcurrencyUsage --cli-unfold-argument  \
    --AppBizIds 1812732010083385344 \
    --ModelName cs-normal-70b \
    --StartTime 1724688000 \
    --EndTime 1724774400
```

Output: 
```
{
    "Response": {
        "AvailableConcurrency": 0,
        "ConcurrencyPeak": 0,
        "ExceedUsageTime": 1,
        "RequestId": "0683ec32-da98-450a-acc9-671a1abf1553"
    }
}
```

