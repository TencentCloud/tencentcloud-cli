**Example 1: 获取口味王日热度明细**



Input: 

```
tccli trp DescribeFlavorKingCycleBrandProvinceCityScanAnalysis --cli-unfold-argument  \
    --CorpId 10046 \
    --QueryDate 2026-05-01
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Cities": [
                    {
                        "City": "上海",
                        "Ratio": [
                            0.8491
                        ],
                        "Regions": [
                            {
                                "Ratio": [
                                    0.8528
                                ],
                                "Region": "嘉定区"
                            }
                        ]
                    }
                ],
                "Province": "上海",
                "Ratio": [
                    0.8491
                ]
            }
        ],
        "RequestId": "61828e83-6500-4e84-b736-747f9034300b"
    }
}
```

