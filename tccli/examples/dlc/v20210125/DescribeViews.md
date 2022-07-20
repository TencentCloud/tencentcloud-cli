**Example 1: 查询视图列表**



Input: 

```
tccli dlc DescribeViews --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0 \
    --DatabaseName testdb \
    --Sort name \
    --Asc True \
    --StartTime 2021-11-11 00:00:00 \
    --EndTime 2021-11-18 00:00:00
```

Output: 
```
{
    "Response": {
        "RequestId": "c1d840f1-2df8-4ef4-9e44-02db58f24475",
        "TotalCount": 1,
        "ViewList": [
            {
                "ViewBaseInfo": {
                    "DatabaseName": "testdb",
                    "ViewName": "v1",
                    "UserAlias": "testUser",
                    "UserSubUin": "100019878767"
                },
                "Columns": [],
                "Properties": [
                    {
                        "Key": "presto_view",
                        "Value": "true"
                    },
                    {
                        "Key": "presto_query_id",
                        "Value": "20210901_123510_00000_9jg5j"
                    },
                    {
                        "Key": "transient_lastDdlTime",
                        "Value": "1630499714051"
                    },
                    {
                        "Key": "comment",
                        "Value": "Presto View"
                    },
                    {
                        "Key": "presto_version",
                        "Value": "0.242.1-DLC-rc11-6fe2f42"
                    }
                ],
                "CreateTime": "1630499714000",
                "ModifiedTime": "1630499714000"
            }
        ]
    }
}
```

