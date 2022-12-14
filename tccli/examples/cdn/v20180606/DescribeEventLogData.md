**Example 1: DescribeEventLogData 用于查询事件日志统计曲线**



Input: 

```
tccli cdn DescribeEventLogData --cli-unfold-argument  \
    --StartTime 2020-09-22 00:00:00 \
    --EndTime 2020-09-22 00:10:00 \
    --Domain www.test.com \
    --Url /1.jpg \
    --Mode cc \
    --ActionName intercept
```

Output: 
```
{
    "Response": {
        "RequestId": "1abbe623-4b0e-4727-ab51-7624902d47f4",
        "Results": []
    }
}
```

