**Example 1: 获取实例慢查询日志**



Input: 

```
tccli postgres DescribeDBSlowlogs --cli-unfold-argument  \
    --DBInstanceId postgres-apzvwncr\
    --StartTime '2018-06-10 17:06:38'\
    --EndTime '2018-06-11 17:06:38'
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Detail": [],
        "RequestId": "08fdf411-5d39-44f2-8e1d-a58ee60b237d"
    }
}
```

