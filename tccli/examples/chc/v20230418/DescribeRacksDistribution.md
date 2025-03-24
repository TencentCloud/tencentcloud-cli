**Example 1: 获取机架分布列表**



Input: 

```
tccli chc DescribeRacksDistribution --cli-unfold-argument  \
    --IdcUnitId 2555
```

Output: 
```
{
    "Response": {
        "DistributionSet": [
            {
                "RackNumber": "C",
                "RackUsageSet": [
                    {
                        "RackId": 91831,
                        "RackShortName": "C01",
                        "TotalNum": 10,
                        "UnusedNum": 8,
                        "UsedNum": 2,
                        "UsedRate": 0.2
                    },
                    {
                        "RackId": 91840,
                        "RackShortName": "C04",
                        "TotalNum": 25,
                        "UnusedNum": 5,
                        "UsedNum": 20,
                        "UsedRate": 0.8
                    },
                    {
                        "RackId": 91843,
                        "RackShortName": "C05",
                        "TotalNum": 26,
                        "UnusedNum": 10,
                        "UsedNum": 16,
                        "UsedRate": 0.62
                    },
                    {
                        "RackId": 91846,
                        "RackShortName": "C06",
                        "TotalNum": 25,
                        "UnusedNum": 19,
                        "UsedNum": 6,
                        "UsedRate": 0.24
                    },
                    {
                        "RackId": 91849,
                        "RackShortName": "C07",
                        "TotalNum": 25,
                        "UnusedNum": 22,
                        "UsedNum": 3,
                        "UsedRate": 0.12
                    },
                    {
                        "RackId": 91852,
                        "RackShortName": "C08",
                        "TotalNum": 26,
                        "UnusedNum": 26,
                        "UsedNum": 0,
                        "UsedRate": 0
                    },
                    {
                        "RackId": 91855,
                        "RackShortName": "C09",
                        "TotalNum": 25,
                        "UnusedNum": 23,
                        "UsedNum": 2,
                        "UsedRate": 0.08
                    },
                    {
                        "RackId": 91858,
                        "RackShortName": "C10",
                        "TotalNum": 10,
                        "UnusedNum": 10,
                        "UsedNum": 0,
                        "UsedRate": 0
                    },
                    {
                        "RackId": 91867,
                        "RackShortName": "C13",
                        "TotalNum": 25,
                        "UnusedNum": 11,
                        "UsedNum": 14,
                        "UsedRate": 0.56
                    },
                    {
                        "RackId": 91870,
                        "RackShortName": "C14",
                        "TotalNum": 26,
                        "UnusedNum": 15,
                        "UsedNum": 11,
                        "UsedRate": 0.42
                    },
                    {
                        "RackId": 91873,
                        "RackShortName": "C15",
                        "TotalNum": 25,
                        "UnusedNum": 23,
                        "UsedNum": 2,
                        "UsedRate": 0.08
                    }
                ]
            },
            {
                "RackNumber": "D",
                "RackUsageSet": [
                    {
                        "RackId": 91885,
                        "RackShortName": "D01",
                        "TotalNum": 25,
                        "UnusedNum": 22,
                        "UsedNum": 3,
                        "UsedRate": 0.12
                    },
                    {
                        "RackId": 91894,
                        "RackShortName": "D04",
                        "TotalNum": 25,
                        "UnusedNum": 25,
                        "UsedNum": 0,
                        "UsedRate": 0
                    },
                    {
                        "RackId": 91897,
                        "RackShortName": "D05",
                        "TotalNum": 26,
                        "UnusedNum": 17,
                        "UsedNum": 9,
                        "UsedRate": 0.35
                    },
                    {
                        "RackId": 91900,
                        "RackShortName": "D06",
                        "TotalNum": 25,
                        "UnusedNum": 15,
                        "UsedNum": 10,
                        "UsedRate": 0.4
                    },
                    {
                        "RackId": 91903,
                        "RackShortName": "D07",
                        "TotalNum": 25,
                        "UnusedNum": 23,
                        "UsedNum": 2,
                        "UsedRate": 0.08
                    },
                    {
                        "RackId": 91906,
                        "RackShortName": "D08",
                        "TotalNum": 26,
                        "UnusedNum": 19,
                        "UsedNum": 7,
                        "UsedRate": 0.27
                    },
                    {
                        "RackId": 91909,
                        "RackShortName": "D09",
                        "TotalNum": 25,
                        "UnusedNum": 12,
                        "UsedNum": 13,
                        "UsedRate": 0.52
                    },
                    {
                        "RackId": 91912,
                        "RackShortName": "D10",
                        "TotalNum": 25,
                        "UnusedNum": 14,
                        "UsedNum": 11,
                        "UsedRate": 0.44
                    },
                    {
                        "RackId": 91915,
                        "RackShortName": "D11",
                        "TotalNum": 26,
                        "UnusedNum": 18,
                        "UsedNum": 8,
                        "UsedRate": 0.31
                    },
                    {
                        "RackId": 91918,
                        "RackShortName": "D12",
                        "TotalNum": 25,
                        "UnusedNum": 20,
                        "UsedNum": 5,
                        "UsedRate": 0.2
                    },
                    {
                        "RackId": 91921,
                        "RackShortName": "D13",
                        "TotalNum": 25,
                        "UnusedNum": 18,
                        "UsedNum": 7,
                        "UsedRate": 0.28
                    },
                    {
                        "RackId": 91924,
                        "RackShortName": "D14",
                        "TotalNum": 26,
                        "UnusedNum": 23,
                        "UsedNum": 3,
                        "UsedRate": 0.12
                    },
                    {
                        "RackId": 91927,
                        "RackShortName": "D15",
                        "TotalNum": 25,
                        "UnusedNum": 12,
                        "UsedNum": 13,
                        "UsedRate": 0.52
                    }
                ]
            },
            {
                "RackNumber": "E",
                "RackUsageSet": [
                    {
                        "RackId": 91948,
                        "RackShortName": "E04",
                        "TotalNum": 10,
                        "UnusedNum": 8,
                        "UsedNum": 2,
                        "UsedRate": 0.2
                    },
                    {
                        "RackId": 91951,
                        "RackShortName": "E05",
                        "TotalNum": 10,
                        "UnusedNum": 10,
                        "UsedNum": 0,
                        "UsedRate": 0
                    }
                ]
            }
        ],
        "RequestId": "d83e0740-e3c6-4e67-b194-2b9081f50e0a"
    }
}
```

