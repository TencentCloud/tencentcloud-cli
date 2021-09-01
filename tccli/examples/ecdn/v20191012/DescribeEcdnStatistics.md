**Example 1: 访问数据查询**



Input: 

```
tccli ecdn DescribeEcdnStatistics --cli-unfold-argument  \
    --StartTime '2018-09-04 00:00:00' \
    --EndTime '2018-09-04 12:00:00' \
    --Metrics flux \
    --Interval 60 \
    --Domains www.test.com \
    --Projects 0
```

Output: 
```
{
    "Response": {
        "RequestId": "13d41d37-546f-42ed-a3b9-ff82a51ecd0a",
        "Data": [
            {
                "Resource": "all",
                "EcdnData": {
                    "Metrics": [
                        "flux",
                        "request"
                    ],
                    "DetailData": [
                        {
                            "Time": "2019-12-13 00:00:00",
                            "Value": [
                                10,
                                20
                            ]
                        },
                        {
                            "Time": "2019-12-13 00:05:00",
                            "Value": [
                                20,
                                30
                            ]
                        }
                    ]
                }
            }
        ]
    }
}
```

