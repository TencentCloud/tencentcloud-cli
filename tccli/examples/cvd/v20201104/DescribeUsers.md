**Example 1: DescribeUsers**



Input: 

```
tccli cvd DescribeUsers --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Users": [
            {
                "Status": "ACTIVE",
                "DisplayName": "tom",
                "Name": "tom",
                "PhoneNum": "1234567890",
                "DepartmentId": "sale",
                "Mail": "123456@qq.com",
                "StrategyId": "str-123456",
                "Id": "us-02a7aa5b2ae94e028d2304f3ecceb614",
                "StrategyName": "管理策略"
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

