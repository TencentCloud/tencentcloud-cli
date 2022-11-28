**Example 1: 查询活动ID为10000的非敏感信息**

查询活动ID为10000的非敏感信息

Input: 

```
tccli opc DescribeActivityNonSensitiveInfo --cli-unfold-argument  \
    --ActivityId 10000
```

Output: 
```
{
    "Response": {
        "ActivityNonSensitiveInfo": {
            "ActivityId": 10000,
            "Name": "测试活动",
            "PageUrl": "https://cloud.tencent.com/act/season",
            "StartTime": "2020-09-22 00:00:00",
            "EndTime": "2021-09-22 00:00:00",
            "Status": 1
        },
        "RequestId": "xx"
    }
}
```

