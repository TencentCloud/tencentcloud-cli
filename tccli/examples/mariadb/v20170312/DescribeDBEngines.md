**Example 1: 获取DB引擎版本列表**



Input: 

```
tccli mariadb DescribeDBEngines --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "Description": "高度兼容MySQL 5.5",
                "Name": "MariaDB 10.0.10",
                "Type": "MariaDB",
                "Version": "10.0.10"
            },
            {
                "Description": "高度兼容MySQL 5.6",
                "Name": "MariaDB 10.1.9",
                "Type": "MariaDB",
                "Version": "10.1.9"
            },
            {
                "Description": "完全兼容MySQL 5.7",
                "Name": "MySQL 5.7.17",
                "Type": "Percona",
                "Version": "5.7.17"
            }
        ],
        "RequestId": "a613aed0-7fb5-11ea-a6fe-525400542aa6",
        "TotalCount": 3
    }
}
```

