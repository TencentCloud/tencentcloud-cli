**Example 1: 域名统计指标查询**



Input: 

```
tccli ecdn DescribeEcdnDomainStatistics --cli-unfold-argument  \
    --StartTime '2018-09-04 00:00:00' \
    --EndTime '2018-09-04 12:00:00' \
    --Metrics flux delay request bandwidth \
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
                "Resource": "stsdk.vivo.com.cn",
                "DetailData": [
                    {
                        "Name": "request",
                        "Value": 5628872958
                    },
                    {
                        "Name": "flux",
                        "Value": 3535122082980
                    },
                    {
                        "Name": "delay",
                        "Value": 87
                    },
                    {
                        "Name": "bandwidth",
                        "Value": 825782981
                    }
                ]
            }
        ],
        "TotalCount": 20
    }
}
```

