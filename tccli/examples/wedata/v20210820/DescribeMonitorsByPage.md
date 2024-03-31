**Example 1: 分页查询质量监控组**

分页查询质量监控组

Input: 

```
tccli wedata DescribeMonitorsByPage --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 1,
            "Items": [
                {
                    "RuleGroupId": 1,
                    "TableId": "9y78ughi79tg79tgy",
                    "DatasourceId": 1,
                    "DatabaseId": "789uhi8jb789uib",
                    "MonitorType": 1,
                    "MonitorStatus": 1,
                    "CreateUserId": 1,
                    "CreateUserName": "zhangsan",
                    "CreateTime": "2023-10-01"
                }
            ]
        },
        "RequestId": "0ff4e8ae-ebea-4a41-8aa2-1f6bc4b68e69"
    }
}
```

