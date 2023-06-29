**Example 1: 查询下线工单列表**



Input: 

```
tccli bma DescribeBPOfflineTickets --cli-unfold-argument  \
    --Filters.0.Name Status \
    --Filters.0.Value xxx \
    --Filters.1.Name StartTime \
    --Filters.1.Value 2020-06-01 00:00:00 \
    --Filters.2.Name EndTime \
    --Filters.2.Value 2020-12-01 00:00:00 \
    --PageSize 10 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {
        "Tickets": [
            {
                "Status": 1,
                "DetectTime": "xx",
                "FakeURL": "xx",
                "FakeURLId": 1,
                "OfflineTime": "xx",
                "SUin": "xx",
                "AppealNumber": "xx",
                "ProtectWeb": "xx",
                "Note": "xx",
                "IP": "xx",
                "CreateTime": "xx",
                "IPLoc": "xx"
            }
        ],
        "TotalCount": 1,
        "RequestId": "xx"
    }
}
```

