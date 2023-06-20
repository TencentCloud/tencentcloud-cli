**Example 1: 查询实例postgres-6fego161备份列表**

查询postgres-6fego161数据库实例在2018-06-10 17:06:38至2018-06-11 17:06:38时间内的全量备份列表。

Input: 

```
tccli postgres DescribeDBBackups --cli-unfold-argument  \
    --DBInstanceId postgres-6fego161 \
    --Limit 20 \
    --StartTime 2018-06-10 17:06:38 \
    --Offset 0 \
    --EndTime 2018-06-11 17:06:38 \
    --Type 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "BackupList": [
            {
                "SetId": "f77ecd1a-087c-5c66-8c35-95c835d7ec24",
                "Status": 2,
                "InternalAddr": "http://172.16.16.30:8366/download/20180622015612.tar.gz?giz7Z4LlMjascFkshSSB4+B1gaI0F3HAQIZcFPDbIsdfgfJdfs+89qfhuYQ5wC0ooTcDIdUwB4iJlL1by8xfKkcMAv8nr8g67P6hhg5YOnk=",
                "StartTime": "2018-06-22 01:56:01.181971",
                "ExternalAddr": "https://gz-dl-postgres.cloud.tencent.com/download/20180622015612.tar.gz?giz7Z4LlMjascFkshSSB4+B1gaI0F3HAQIZcFPDbIsdfgfJdfs+89qfhuYQ5wC0ooTcDIdUwB4iJlL1by8xfKkcMAv8nr8g67P6hhg5YOnk=",
                "Strategy": 1,
                "DbList": [
                    "db1"
                ],
                "Way": 1,
                "EndTime": "2018-06-22 01:56:55.071181",
                "Type": 1,
                "Id": 450,
                "Size": 3654968
            },
            {
                "SetId": "f6yecd1a-087c-5c66-cdas-95c835d7ec24",
                "Status": 2,
                "InternalAddr": "http://172.16.16.30:8366/download/20180621015515.tar.gz?giz7Z4LlMjascFkshSSB4+B1gaI0F3HAQIZcFPDbIse2MDEI7vd/CuyMUMMyDXAd4ld69sCMdEKwkpFWIVcfE+PZ0+MYTbsBHzW84KtSGw8=",
                "StartTime": "2018-06-21 01:55:04.199169",
                "ExternalAddr": "https://gz-dl-postgres.cloud.tencent.com/download/20180621015515.tar.gz?giz7Z4LlMjascFkshSSB4+B1gaI0F3HAQIZcFPDbIse2MDEI7vd/CuyMUMMyDXAd4ld69sCMdEKwkpFWIVcfE+PZ0+MYTbsBHzW84KtSGw8=",
                "Strategy": 1,
                "DbList": [
                    "db2"
                ],
                "Way": 1,
                "EndTime": "2018-06-21 01:55:58.477232",
                "Type": 1,
                "Id": 450,
                "Size": 3654991
            }
        ],
        "RequestId": "08fdf411-5d39-44f2-8e1d-a58ee60b237d"
    }
}
```

