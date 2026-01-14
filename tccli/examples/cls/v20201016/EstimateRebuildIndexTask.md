**Example 1: 预估索引重建时间**



Input: 

```
tccli cls EstimateRebuildIndexTask --cli-unfold-argument  \
    --TopicId a5ce0c9c-xxxx-44a5-bc79-5f2190626bd0 \
    --StartTime 1234567890123 \
    --EndTime 1234567890456
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7",
        "RemainTime": 10000,
        "WriteTraffic": 1345
    }
}
```

