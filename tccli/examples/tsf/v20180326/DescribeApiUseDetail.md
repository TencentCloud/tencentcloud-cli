**Example 1: 查询网关API监控明细数据**



Input: 

```
tccli tsf DescribeApiUseDetail --cli-unfold-argument  \
    --GatewayDeployGroupId group-yo476mrv \
    --ApiId api-megi25v8 \
    --StartTime 2024-12-16 14:52:28 \
    --EndTime 2024-12-23 14:52:28
```

Output: 
```
{
    "Response": {
        "RequestId": "a3fbcf43-9d0e-4f29-b5c3-cd591ab0ad74",
        "Result": {
            "Quantile": {
                "FifthPositionValue": "18.70000",
                "MaxValue": "934.68000",
                "MinValue": "9.13000",
                "NinthPositionValue": "24.88900"
            },
            "TopStatusCode": [
                {
                    "Count": "39788487",
                    "Name": "2xx",
                    "Ratio": "0.9999875593700789"
                }
            ],
            "TopTimeCost": [
                {
                    "Count": "39741921",
                    "Name": "0_100_ms",
                    "Ratio": "0.9988172353844087"
                },
                {
                    "Count": "36896",
                    "Name": "100_200_ms",
                    "Ratio": "9.27291881958679E-4"
                },
                {
                    "Count": "9941",
                    "Name": "200_500_ms",
                    "Ratio": "2.498430344360155E-4"
                },
                {
                    "Count": "224",
                    "Name": "500_2000_ms",
                    "Ratio": "5.629699196626845E-6"
                },
                {
                    "Count": "0",
                    "Name": "2000_ms",
                    "Ratio": "0.0"
                }
            ]
        }
    }
}
```

