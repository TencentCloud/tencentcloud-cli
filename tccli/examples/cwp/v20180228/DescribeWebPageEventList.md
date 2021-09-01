**Example 1: 示例**



Input: 

```
tccli cwp DescribeWebPageEventList --cli-unfold-argument  \
    --By CreateTime \
    --Order 1 \
    --Filters.0.Name IpOrAlias \
    --Filters.0.Values 'HostName or HostIp'
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Id": 1,
                "CreateTime": "2020-06-10 00:00:04",
                "EventDir": "/tmp",
                "EventStatus": 1,
                "EventType": 1,
                "HostIp": "10.0.0.1",
                "HostName": "服务器名称1",
                "RestoreTime": "2020-06-11 00:00:04",
                "FileType": 1
            }
        ],
        "RequestId": "d9506441-52bc-4d14-a767-7e1251ed3ced",
        "TotalCount": 1
    }
}
```

