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
        "RequestId": "c2bb261c-1476-4190-93ba-b3c9bae51249",
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

