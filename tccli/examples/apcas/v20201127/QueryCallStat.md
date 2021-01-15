**Example 1: 获取调用量统计**



Input: 

```
tccli apcas QueryCallStat --cli-unfold-argument  \
    --Type 1 \
    --StartTime 1602470155000 \
    --EndTime 1602470355000
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "CallSet": [
            {
                "Date": "2020-08-30 00:00:00",
                "Amount": 2400
            },
            {
                "Date": "2020-09-01 00:00:00",
                "Amount": 2400
            }
        ]
    }
}
```

