**Example 1: 无录像切片**



Input: 

```
tccli iss DescribeRecordSlice --cli-unfold-argument  \
    --StartTime 1692374400 \
    --EndTime 1692457260 \
    --ChannelId 223d7c52-****-4a12-****-82e983dfc08f
```

Output: 
```
{
    "Response": {
        "Data": null,
        "RequestId": "712711ca-6ef2-4b15-aa74-74c289621b2a"
    }
}
```

**Example 2: 有录像切片**



Input: 

```
tccli iss DescribeRecordSlice --cli-unfold-argument  \
    --StartTime 1692374400 \
    --EndTime 1692457260 \
    --ChannelId 223d7c52-****-4a12-****-82e983dfc08f
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "List": [
                    {
                        "Begin": 1692374406,
                        "End": 1692374426
                    },
                    {
                        "Begin": 1692374426,
                        "End": 1692374446
                    },
                    {
                        "Begin": 1692374446,
                        "End": 1692374466
                    },
                    {
                        "Begin": 1692374466,
                        "End": 1692374486
                    },
                    {
                        "Begin": 1692374486,
                        "End": 1692374506
                    }
                ],
                "PlanId": "572fa953e07********94c0387397748"
            }
        ],
        "RequestId": "fba7981b-d6a4-4177-b11d-e53a6110e4cd"
    }
}
```

