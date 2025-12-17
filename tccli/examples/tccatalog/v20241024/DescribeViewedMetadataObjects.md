**Example 1: 获取元数据对象浏览记录**



Input: 

```
tccli tccatalog DescribeViewedMetadataObjects --cli-unfold-argument  \
    --Limit 5
```

Output: 
```
{
    "Response": {
        "RequestId": "c450aca6-c0aa-41d0-a530-07d2b74b3623",
        "ViewedMetadataObjects": [
            {
                "FullName": "emr_hive_test_12022131.test.hive_test",
                "LastViewedTime": "2024-12-16 20:17:57",
                "Type": "table"
            },
            {
                "FullName": "test.test",
                "LastViewedTime": "2024-12-16 19:47:24",
                "Type": "schema"
            },
            {
                "FullName": "mysql_test_1.test.tb1",
                "LastViewedTime": "2024-12-12 17:29:24",
                "Type": "table"
            },
            {
                "FullName": "mysql_test_1.test2",
                "LastViewedTime": "2024-12-12 16:53:41",
                "Type": "schema"
            },
            {
                "FullName": "mysql_test_1.test",
                "LastViewedTime": "2024-12-12 16:53:38",
                "Type": "schema"
            }
        ]
    }
}
```

