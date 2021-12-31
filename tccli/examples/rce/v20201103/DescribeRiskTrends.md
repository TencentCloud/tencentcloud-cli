**Example 1: DescribeRiskTrends**



Input: 

```
tccli rce DescribeRiskTrends --cli-unfold-argument  \
    --BusinessSecurityData.EventId -1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Code": 0,
            "Message": "OK",
            "Value": [
                {
                    "Name": "请求总量",
                    "Value": [
                        {
                            "Requests": 0,
                            "Index": "2020-06-10 00:00:00"
                        },
                        {
                            "Requests": 0,
                            "Index": "2020-06-11 00:00:00"
                        },
                        {
                            "Requests": 0,
                            "Index": "2020-06-12 00:00:00"
                        },
                        {
                            "Requests": 0,
                            "Index": "2020-06-13 00:00:00"
                        },
                        {
                            "Requests": 0,
                            "Index": "2020-06-14 00:00:00"
                        },
                        {
                            "Requests": 0,
                            "Index": "2020-06-15 00:00:00"
                        },
                        {
                            "Requests": 0,
                            "Index": "2020-06-16 00:00:00"
                        },
                        {
                            "Requests": 0,
                            "Index": "2020-06-17 00:00:00"
                        },
                        {
                            "Requests": 0,
                            "Index": "2020-06-17 10:21:23"
                        }
                    ]
                },
                {
                    "Name": "正常请求量",
                    "Value": [
                        {
                            "Requests": 0,
                            "Index": "2020-06-10 00:00:00"
                        },
                        {
                            "Requests": 0,
                            "Index": "2020-06-11 00:00:00"
                        },
                        {
                            "Requests": 0,
                            "Index": "2020-06-12 00:00:00"
                        },
                        {
                            "Requests": 0,
                            "Index": "2020-06-13 00:00:00"
                        },
                        {
                            "Requests": 0,
                            "Index": "2020-06-14 00:00:00"
                        },
                        {
                            "Requests": 0,
                            "Index": "2020-06-15 00:00:00"
                        },
                        {
                            "Requests": 0,
                            "Index": "2020-06-16 00:00:00"
                        },
                        {
                            "Requests": 0,
                            "Index": "2020-06-17 00:00:00"
                        },
                        {
                            "Requests": 0,
                            "Index": "2020-06-17 10:21:23"
                        }
                    ]
                },
                {
                    "Name": "疑似请求量",
                    "Value": [
                        {
                            "Requests": 0,
                            "Index": "2020-06-10 00:00:00"
                        },
                        {
                            "Requests": 0,
                            "Index": "2020-06-11 00:00:00"
                        },
                        {
                            "Requests": 0,
                            "Index": "2020-06-12 00:00:00"
                        },
                        {
                            "Requests": 0,
                            "Index": "2020-06-13 00:00:00"
                        },
                        {
                            "Requests": 0,
                            "Index": "2020-06-14 00:00:00"
                        },
                        {
                            "Requests": 0,
                            "Index": "2020-06-15 00:00:00"
                        },
                        {
                            "Requests": 0,
                            "Index": "2020-06-16 00:00:00"
                        },
                        {
                            "Requests": 0,
                            "Index": "2020-06-17 00:00:00"
                        },
                        {
                            "Requests": 0,
                            "Index": "2020-06-17 10:21:23"
                        }
                    ]
                },
                {
                    "Name": "风险请求量",
                    "Value": [
                        {
                            "Requests": 0,
                            "Index": "2020-06-10 00:00:00"
                        },
                        {
                            "Requests": 0,
                            "Index": "2020-06-11 00:00:00"
                        },
                        {
                            "Requests": 0,
                            "Index": "2020-06-12 00:00:00"
                        },
                        {
                            "Requests": 0,
                            "Index": "2020-06-13 00:00:00"
                        },
                        {
                            "Requests": 0,
                            "Index": "2020-06-14 00:00:00"
                        },
                        {
                            "Requests": 0,
                            "Index": "2020-06-15 00:00:00"
                        },
                        {
                            "Requests": 0,
                            "Index": "2020-06-16 00:00:00"
                        },
                        {
                            "Requests": 0,
                            "Index": "2020-06-17 00:00:00"
                        },
                        {
                            "Requests": 0,
                            "Index": "2020-06-17 10:21:23"
                        }
                    ]
                }
            ]
        },
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

