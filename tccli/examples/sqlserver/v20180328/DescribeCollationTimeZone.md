**Example 1: 查询实例支持的字符集和时区**



Input: 

```
tccli sqlserver DescribeCollationTimeZone --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "863b2797-858b-49f3-88e9-50159e564cbc",
        "Collation": [
            "Chinese_PRC_CI_AS"
        ],
        "TimeZone": [
            "China Standard Time"
        ]
    }
}
```

