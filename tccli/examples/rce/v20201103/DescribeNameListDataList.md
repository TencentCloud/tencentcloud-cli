**Example 1: DescribeNameListDataList**



Input: 

```
tccli rce DescribeNameListDataList --cli-unfold-argument  \
    --BusinessSecurityData.NameListId 33 \
    --BusinessSecurityData.Status 1 \
    --BusinessSecurityData.PageNumber 1 \
    --BusinessSecurityData.PageSize 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "Count": 1,
            "List": [
                {
                    "NameListDataId": 72,
                    "NameListId": 33,
                    "DataContent": "xxx.x.0.4",
                    "DataSource": 2,
                    "StartTime": "2020-03-03 04:50:00",
                    "EndTime": "2020-03-03 04:50:00",
                    "Status": 1,
                    "Remark": "ip黑名单5",
                    "CreateTime": "2020-06-19 18:23:25",
                    "UpdateTime": "2020-06-23 16:51:31"
                }
            ]
        },
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

