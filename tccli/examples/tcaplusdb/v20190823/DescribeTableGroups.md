**Example 1: 查询表格组列表**

查询表格组列表

Input: 

```
tccli tcaplusdb DescribeTableGroups --cli-unfold-argument  \
    --ClusterId 6179109757
```

Output: 
```
{
    "Response": {
        "RequestId": "dbaf73f4-3d1d-4f7b-b3b3-259d53e546be",
        "TotalCount": 2,
        "TableGroups": [
            {
                "CreatedTime": "2019-08-30 18:57:02",
                "TableGroupId": "1",
                "TableCount": 0,
                "TotalSize": 0,
                "TableGroupName": "tdr测试区1"
            },
            {
                "CreatedTime": "2019-08-30 18:58:03",
                "TableGroupId": "1001",
                "TableCount": 0,
                "TotalSize": 0,
                "TableGroupName": "tdr正式区1"
            }
        ]
    }
}
```

