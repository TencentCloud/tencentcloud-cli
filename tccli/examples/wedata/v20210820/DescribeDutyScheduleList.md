**Example 1: 获取值班表列表，携带创建者信息**



Input: 

```
tccli wedata DescribeDutyScheduleList --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "RequestId": "8c721701-0d14-4dbc-9724-4736eccca8e8",
        "Data": {
            "Rows": [
                {
                    "Id": 87,
                    "Name": "mytestdd",
                    "Creator": "100022256608"
                },
                {
                    "Id": 88,
                    "Name": "ss1",
                    "Creator": "100022256608"
                },
                {
                    "Id": 89,
                    "Name": "sss1",
                    "Creator": "100022256608"
                },
                {
                    "Id": 90,
                    "Name": "sss11",
                    "Creator": "100022256608"
                },
                {
                    "Id": 91,
                    "Name": "sss111",
                    "Creator": "100022256608"
                },
                {
                    "Id": 92,
                    "Name": "sss12",
                    "Creator": "100022256608"
                },
                {
                    "Id": 93,
                    "Name": "e22ldd61ydb",
                    "Creator": "100022256608"
                },
                {
                    "Id": 94,
                    "Name": "idtxn1qnvx",
                    "Creator": "100022256608"
                },
                {
                    "Id": 95,
                    "Name": "m263x3gpci",
                    "Creator": "100022256608"
                },
                {
                    "Id": 96,
                    "Name": "fua1dsjja64",
                    "Creator": "100022256608"
                }
            ],
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 45,
            "TotalPageNumber": 5
        }
    }
}
```

