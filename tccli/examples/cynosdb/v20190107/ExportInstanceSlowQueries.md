**Example 1: 导出实例慢日志**



Input: 

```
tccli cynosdb ExportInstanceSlowQueries --cli-unfold-argument  \
    --InstanceId cynosdbmysql-ins-xxxxxxxx \
    --StartTime 2022-01-01 00:00:00 \
    --EndTime 2022-01-01 23:59:59 \
    --Offset 0 \
    --Limit 100 \
    --Username root \
    --Database db \
    --FileType csv
```

Output: 
```
{
    "Response": {
        "FileContent": "xxxx",
        "RequestId": "9e56617c-c7cc-44e1-a967-6beb418ad5e7"
    }
}
```

