**Example 1: 查询慢查询日志**



Input: 

```
tccli cdb DescribeSlowLogs --cli-unfold-argument  \
    --InstanceId cdb-c1nl9rpv
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "TotalCount": 3,
        "Items": [
            {
                "Name": "ivansqwutestdr_slowlog_20170425.log",
                "IntranetUrl": "",
                "Date": "2017-04-26 00:00:08",
                "InternetUrl": "",
                "Type": "slowlog",
                "Size": 0
            },
            {
                "Name": "ivansqwutestdr_slowlog_20170426.log",
                "IntranetUrl": "http://gz.xxxxxxxxxx",
                "Date": "2017-04-27 00:00:07",
                "InternetUrl": "http://gz.xxxxxxxxxx",
                "Type": "slowlog",
                "Size": 212
            },
            {
                "Name": "ivansqwutestdr_slowlog_20170427.log",
                "IntranetUrl": "",
                "Date": "2017-04-28 00:00:09",
                "InternetUrl": "",
                "Type": "slowlog",
                "Size": 0
            }
        ]
    }
}
```

