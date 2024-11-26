**Example 1: 接口调用折线图**

接口调用折线图

Input: 

```
tccli lke DescribeCallStatsGraph --cli-unfold-argument  \
    --ModelName cs-normal \
    --StartTime 1726070400 \
    --EndTime 1726156799
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "X": "202411190930",
                "Y": 12
            },
            {
                "X": "202411190915",
                "Y": 11
            }
        ],
        "RequestId": "85e7259e-7810-4301-8f44-cf2d94ec0a0f"
    }
}
```

