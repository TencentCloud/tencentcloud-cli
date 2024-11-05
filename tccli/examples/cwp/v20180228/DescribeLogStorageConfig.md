**Example 1: 获取日志存储配置**

获取日志存储配置

Input: 

```
tccli cwp DescribeLogStorageConfig --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Type": [
            "malware"
        ],
        "Period": 30,
        "PeriodModifyCount": 0,
        "Granularity": "day",
        "RequestId": "1c26308c-5493-4eaf-a817-112ec25f499e"
    }
}
```

