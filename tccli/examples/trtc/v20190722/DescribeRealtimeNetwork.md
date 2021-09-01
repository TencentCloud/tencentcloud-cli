**Example 1: 查询实时网络状态**

查询24小时内的网络状态，如上行丢包。下行丢包

Input: 

```
tccli trtc DescribeRealtimeNetwork --cli-unfold-argument  \
    --SdkAppId 1400188366 \
    --StartTime 1587879309 \
    --EndTime 1587882309
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Content": [
                    {
                        "Time": 1587879300,
                        "Value": 0
                    },
                    {
                        "Time": 1587879360,
                        "Value": 0
                    },
                    {
                        "Time": 1587879420,
                        "Value": 0
                    },
                    {
                        "Time": 1587879480,
                        "Value": 0
                    },
                    {
                        "Time": 1587879540,
                        "Value": 0
                    },
                    {
                        "Time": 1587879600,
                        "Value": 0
                    },
                    {
                        "Time": 1587879660,
                        "Value": 0
                    },
                    {
                        "Time": 1587879720,
                        "Value": 0
                    },
                    {
                        "Time": 1587879780,
                        "Value": 0
                    },
                    {
                        "Time": 1587879840,
                        "Value": 0
                    },
                    {
                        "Time": 1587879900,
                        "Value": 0
                    },
                    {
                        "Time": 1587879960,
                        "Value": 0
                    },
                    {
                        "Time": 1587880020,
                        "Value": 0
                    },
                    {
                        "Time": 1587880080,
                        "Value": 0
                    },
                    {
                        "Time": 1587880140,
                        "Value": 0
                    },
                    {
                        "Time": 1587880200,
                        "Value": 0
                    },
                    {
                        "Time": 1587880260,
                        "Value": 0
                    },
                    {
                        "Time": 1587880320,
                        "Value": 0
                    },
                    {
                        "Time": 1587880380,
                        "Value": 0
                    },
                    {
                        "Time": 1587880440,
                        "Value": 0
                    },
                    {
                        "Time": 1587880500,
                        "Value": 0
                    },
                    {
                        "Time": 1587880560,
                        "Value": 0
                    },
                    {
                        "Time": 1587880620,
                        "Value": 0
                    },
                    {
                        "Time": 1587880680,
                        "Value": 0
                    },
                    {
                        "Time": 1587880740,
                        "Value": 0
                    },
                    {
                        "Time": 1587880800,
                        "Value": 0
                    },
                    {
                        "Time": 1587880860,
                        "Value": 0
                    },
                    {
                        "Time": 1587880920,
                        "Value": 0
                    },
                    {
                        "Time": 1587880980,
                        "Value": 0
                    },
                    {
                        "Time": 1587881040,
                        "Value": 0
                    },
                    {
                        "Time": 1587881100,
                        "Value": 0
                    },
                    {
                        "Time": 1587881160,
                        "Value": 0
                    },
                    {
                        "Time": 1587881220,
                        "Value": 0
                    },
                    {
                        "Time": 1587881280,
                        "Value": 0
                    },
                    {
                        "Time": 1587881340,
                        "Value": 0
                    },
                    {
                        "Time": 1587881400,
                        "Value": 0
                    },
                    {
                        "Time": 1587881460,
                        "Value": 0
                    },
                    {
                        "Time": 1587881520,
                        "Value": 0
                    },
                    {
                        "Time": 1587881580,
                        "Value": 0
                    },
                    {
                        "Time": 1587881640,
                        "Value": 0
                    },
                    {
                        "Time": 1587881700,
                        "Value": 0
                    },
                    {
                        "Time": 1587881760,
                        "Value": 0
                    },
                    {
                        "Time": 1587881820,
                        "Value": 0
                    },
                    {
                        "Time": 1587881880,
                        "Value": 0
                    },
                    {
                        "Time": 1587881940,
                        "Value": 0
                    },
                    {
                        "Time": 1587882000,
                        "Value": 0
                    },
                    {
                        "Time": 1587882060,
                        "Value": 0
                    },
                    {
                        "Time": 1587882120,
                        "Value": 0
                    },
                    {
                        "Time": 1587882180,
                        "Value": 0
                    },
                    {
                        "Time": 1587882240,
                        "Value": 0
                    }
                ],
                "DataType": "sendLossRateRaw"
            },
            {
                "Content": [
                    {
                        "Time": 1587879300,
                        "Value": 0
                    },
                    {
                        "Time": 1587879360,
                        "Value": 0
                    },
                    {
                        "Time": 1587879420,
                        "Value": 0
                    },
                    {
                        "Time": 1587879480,
                        "Value": 0
                    },
                    {
                        "Time": 1587879540,
                        "Value": 0
                    },
                    {
                        "Time": 1587879600,
                        "Value": 0
                    },
                    {
                        "Time": 1587879660,
                        "Value": 0
                    },
                    {
                        "Time": 1587879720,
                        "Value": 0
                    },
                    {
                        "Time": 1587879780,
                        "Value": 0
                    },
                    {
                        "Time": 1587879840,
                        "Value": 0
                    },
                    {
                        "Time": 1587879900,
                        "Value": 0
                    },
                    {
                        "Time": 1587879960,
                        "Value": 0
                    },
                    {
                        "Time": 1587880020,
                        "Value": 0
                    },
                    {
                        "Time": 1587880080,
                        "Value": 0
                    },
                    {
                        "Time": 1587880140,
                        "Value": 0
                    },
                    {
                        "Time": 1587880200,
                        "Value": 0
                    },
                    {
                        "Time": 1587880260,
                        "Value": 0
                    },
                    {
                        "Time": 1587880320,
                        "Value": 0
                    },
                    {
                        "Time": 1587880380,
                        "Value": 0
                    },
                    {
                        "Time": 1587880440,
                        "Value": 0
                    },
                    {
                        "Time": 1587880500,
                        "Value": 0
                    },
                    {
                        "Time": 1587880560,
                        "Value": 0
                    },
                    {
                        "Time": 1587880620,
                        "Value": 0
                    },
                    {
                        "Time": 1587880680,
                        "Value": 0
                    },
                    {
                        "Time": 1587880740,
                        "Value": 0
                    },
                    {
                        "Time": 1587880800,
                        "Value": 0
                    },
                    {
                        "Time": 1587880860,
                        "Value": 0
                    },
                    {
                        "Time": 1587880920,
                        "Value": 0
                    },
                    {
                        "Time": 1587880980,
                        "Value": 0
                    },
                    {
                        "Time": 1587881040,
                        "Value": 0
                    },
                    {
                        "Time": 1587881100,
                        "Value": 0
                    },
                    {
                        "Time": 1587881160,
                        "Value": 0
                    },
                    {
                        "Time": 1587881220,
                        "Value": 0
                    },
                    {
                        "Time": 1587881280,
                        "Value": 0
                    },
                    {
                        "Time": 1587881340,
                        "Value": 0
                    },
                    {
                        "Time": 1587881400,
                        "Value": 0
                    },
                    {
                        "Time": 1587881460,
                        "Value": 0
                    },
                    {
                        "Time": 1587881520,
                        "Value": 0
                    },
                    {
                        "Time": 1587881580,
                        "Value": 0
                    },
                    {
                        "Time": 1587881640,
                        "Value": 0
                    },
                    {
                        "Time": 1587881700,
                        "Value": 0
                    },
                    {
                        "Time": 1587881760,
                        "Value": 0
                    },
                    {
                        "Time": 1587881820,
                        "Value": 0
                    },
                    {
                        "Time": 1587881880,
                        "Value": 0
                    },
                    {
                        "Time": 1587881940,
                        "Value": 0
                    },
                    {
                        "Time": 1587882000,
                        "Value": 0
                    },
                    {
                        "Time": 1587882060,
                        "Value": 0
                    },
                    {
                        "Time": 1587882120,
                        "Value": 0
                    },
                    {
                        "Time": 1587882180,
                        "Value": 0
                    },
                    {
                        "Time": 1587882240,
                        "Value": 0
                    }
                ],
                "DataType": "recvLossRateRaw"
            }
        ],
        "RequestId": "bfd7d2b2-2e02-4723-af92-0f66e4fd517c"
    }
}
```

