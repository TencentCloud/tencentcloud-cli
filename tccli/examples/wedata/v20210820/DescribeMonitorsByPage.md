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
                    "DatabaseId": "xx",
                    "MonitorStatus": 1,
                    "RuleGroupId": 1,
                    "CreateUserId": 1,
                    "CreateUserName": "xx",
                    "DatasourceId": 1,
                    "TableId": "xx",
                    "MonitorType": 1,
                    "CreateTime": "xx"
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

