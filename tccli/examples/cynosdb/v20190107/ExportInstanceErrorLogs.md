**Example 1: 导出错误日志**

导出错误日志

Input: 

```
tccli cynosdb ExportInstanceErrorLogs --cli-unfold-argument  \
    --InstanceId cynosdbmysql-ins-xxxxxxxx \
    --StartTime 2019-07-04 16:45:32 \
    --EndTime 2019-07-04 16:55:32 \
    --Limit 10 \
    --Offset 0 \
    --LogLevels error \
    --KeyWords abc \
    --FileType csv \
    --OrderBy Timestamp \
    --OrderByType ASC
```

Output: 
```
{
    "Response": {
        "ErrorLogItems": [
            {
                "Timestamp": "2019-07-04 16:45:32",
                "Level": "error",
                "Content": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

