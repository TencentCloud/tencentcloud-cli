**Example 1: 并发折线图示例**

并发折线图示例

Input: 

```
tccli lke DescribeConcurrencyUsageGraph --cli-unfold-argument  \
    --ModelName cs-normal-70b \
    --StartTime 1724688000 \
    --EndTime 1724774400 \
    --AppBizIds 1812732010083385344
```

Output: 
```
{
    "Response": {
        "AvailableY": [
            5,
            4,
            3
        ],
        "RequestId": "ad439868-ed56-44f5-a716-81cc7402e83e",
        "SuccessCallY": [
            1,
            2,
            3
        ],
        "X": [
            "2024082700",
            "2024082701",
            "2024082702"
        ]
    }
}
```

