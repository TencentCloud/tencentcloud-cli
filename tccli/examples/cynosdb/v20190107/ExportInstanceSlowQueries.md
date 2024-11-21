**Example 1: 导出实例慢日志**



Input: 

```
tccli cynosdb ExportInstanceSlowQueries --cli-unfold-argument  \
    --InstanceId cynosdbmysql-ins-93sj6l7d \
    --StartTime 2024-10-11 16:36:18 \
    --EndTime 2024-10-12 16:36:18 \
    --Offset 0 \
    --Limit 1 \
    --Username root \
    --Database db \
    --FileType csv
```

Output: 
```
{
    "Response": {
        "FileContent": "执行时间,SQL语句,客户端地址,用户名,数据库名,执行时长(秒),加锁时长(秒),解析行数,返回行数,远程读取次数,远程读取的字节数,远程读取所花费的时间（微秒）,远程写入次数,远程写入的字节数,远程写入所花费的时间（微秒）,事务提交延迟（微秒）\n2024-10-11 16:36:18,\"INSERT IGNORE INTO sbtest14(id, k, c, pad) VALUES(NULL, 779102\",1.1.1.1,root,db,1.227114,0.000003,0,0,0,0,0,0,0,0,0",
        "RequestId": "9e56617c-c7cc-44e1-a967-6beb418ad5e7"
    }
}
```

