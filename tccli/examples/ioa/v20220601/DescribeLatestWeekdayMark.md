**Example 1: 示例1**



Input: 

```
tccli ioa DescribeLatestWeekdayMark --cli-unfold-argument  \
    --Date 2022-12-20 \
    --GroupId 392
```

Output: 
```
{
    "Response": {
        "RequestId": "5f6eb864-adc1-4cae-ab83-b43a45257e52",
        "Data": {
            "Mark": [
                0,
                1,
                2,
                3,
                4,
                5,
                6
            ]
        }
    }
}
```

