**Example 1: 请求示例**

查询指定实例的慢日志记录

Input: 

```
tccli redis DescribeProxySlowLog --cli-unfold-argument  \
    --InstanceId crs-asda**** \
    --BeginTime '2019-09-08 12:12:41' \
    --EndTime '2019-09-09 12:12:41'
```

Output: 
```
{
    "Response": {
        "TotalCount": 106980,
        "InstanceProxySlowLogDetail": [
            {
                "Duration": 45,
                "ExecuteTime": "2019-09-08 12:13:08",
                "CommandLine": "hget hash_key classify_scope::default",
                "Client": "172.16.21.78",
                "Command": "hget"
            }
        ],
        "RequestId": "121d5b40-d2b8-11e9-8c40-ef686158cbd6"
    }
}
```

**Example 2: 请求示例2**

TotalCount大于1W，即慢日志超过1万条，不支持返回日志详情，返回数据为空。

Input: 

```
tccli redis DescribeProxySlowLog --cli-unfold-argument  \
    --InstanceId crs-asda**** \
    --BeginTime '2019-09-08 12:12:41' \
    --EndTime '2019-09-09 12:12:41' \
    --Limit 10 \
    --Offset 10000
```

Output: 
```
{
    "Response": {
        "TotalCount": 10001,
        "InstanceProxySlowLogDetail": [],
        "RequestId": "121d5b40-d2b8-11e9-8c40-ef686158cbd6"
    }
}
```

