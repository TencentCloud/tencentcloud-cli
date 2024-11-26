**Example 1: 搜索服务折线图详情**

搜索服务折线图详情

Input: 

```
tccli lke DescribeSearchStatsGraph --cli-unfold-argument  \
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
                "Y": 23
            },
            {
                "X": "202411190915",
                "Y": 41
            }
        ],
        "RequestId": "b547fd5a-4d82-4fcc-adb8-899e63c166fc"
    }
}
```

