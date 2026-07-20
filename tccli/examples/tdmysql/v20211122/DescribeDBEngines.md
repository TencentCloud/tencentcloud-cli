**Example 1: 查询引擎**



Input: 

```
tccli tdmysql DescribeDBEngines --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "Description": "",
                "Name": "",
                "Type": "TDStore",
                "Version": "r110d001"
            },
            {
                "Description": "",
                "Name": "",
                "Type": "TDStore",
                "Version": "r091d001"
            },
            {
                "Description": "",
                "Name": "",
                "Type": "TDStore",
                "Version": "r120d001"
            }
        ],
        "RequestId": "6c72b90f-8ebd-4944-b62b-8107d66b814d",
        "TotalCount": 3
    }
}
```

**Example 2: 查询数据库引擎信息**



Input: 

```
tccli tdmysql DescribeDBEngines --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "a613aed0-7fb5-11ea-a6fe-525400542aa6",
        "Items": [
            {
                "Version": "8.0",
                "Type": "TDStore",
                "Name": "11",
                "Description": "11"
            }
        ]
    }
}
```

