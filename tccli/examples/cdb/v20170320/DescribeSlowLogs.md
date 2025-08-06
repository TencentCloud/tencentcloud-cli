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
                "IntranetUrl": "http://gz.tencent.com***",
                "Date": "2017-04-26",
                "InternetUrl": "http://gz.tencent.com***",
                "Type": "slowlog",
                "Size": 0
            },
            {
                "Name": "ivansqwutestdr_slowlog_20170426.log",
                "IntranetUrl": "http://gz.tencent.com***",
                "Date": "2017-04-27",
                "InternetUrl": "http://gz.tencent.com***",
                "Type": "slowlog",
                "Size": 212
            },
            {
                "Name": "ivansqwutestdr_slowlog_20170427.log",
                "IntranetUrl": "http://gz.tencent.com***",
                "Date": "2017-04-28",
                "InternetUrl": "http://gz.tencent.com***",
                "Type": "slowlog",
                "Size": 0
            }
        ]
    }
}
```

