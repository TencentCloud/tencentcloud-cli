**Example 1: 查询二进制日志**



Input: 

```
tccli cdb DescribeBinlogs --cli-unfold-argument  \
    --InstanceId cdb-c1nl9rpv
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "TotalCount": 1,
        "Items": [
            {
                "Name": "ivansqwutestdr_binmysqlbin.000006",
                "IntranetUrl": "http://gz.xxxxxx",
                "Date": "2017-04-26 20:46:32",
                "InternetUrl": "http://gz.xxxxxx",
                "Type": "binlog",
                "Size": 187
            }
        ]
    }
}
```

