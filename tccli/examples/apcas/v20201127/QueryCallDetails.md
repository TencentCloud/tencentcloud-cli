**Example 1: 查询调用统计**



Input: 

```
tccli apcas QueryCallDetails --cli-unfold-argument  \
    --Type 1 \
    --StartTime 1602470155000 \
    --EndTime 1602470355000 \
    --PageNumber 1 \
    --PageSize 100
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "CallDetails": {
            "TotalCount": 2,
            "CallDetailSet": [
                {
                    "DataType": 1,
                    "ValidAmount": 3000,
                    "Date": "2020-09-04 18:00:00"
                },
                {
                    "DataType": 3,
                    "ValidAmount": 6380,
                    "Date": "2020-09-05 17:00:00"
                }
            ]
        }
    }
}
```

