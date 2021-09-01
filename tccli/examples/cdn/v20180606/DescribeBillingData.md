**Example 1: 计费数据查询**



Input: 

```
tccli cdn DescribeBillingData --cli-unfold-argument  \
    --StartTime '2018-09-04 00:00:00' \
    --EndTime '2018-09-04 12:00:00'
```

Output: 
```
{
    "Response": {
        "RequestId": "123",
        "Data": [
            {
                "Resource": "all",
                "BillingData": [
                    {
                        "Metric": "flux",
                        "DetailData": [
                            {
                                "Time": "2018-09-03 00:00:00",
                                "Value": 10
                            },
                            {
                                "Time": "2018-09-03 00:05:00",
                                "Value": 20
                            }
                        ],
                        "SummarizedData": {
                            "Name": "sum",
                            "Value": 30
                        }
                    }
                ]
            }
        ],
        "Interval": "5min"
    }
}
```

