**Example 1: 使用 NextToken 续查**

续查只回传 NextToken；调用方不要解析或构造 token。

Input: 

```
tccli cfw DescribeCfwLogs --cli-unfold-argument  \
    --NextToken opaque-token
```

Output: 
```
{
    "Response": {
        "Data": "{\"Items\":[],\"TotalCount\":0,\"Limit\":100,\"HasMore\":false}",
        "RequestId": "4266525E-10C4-41E1-8A28-5CCE1FBF6A58"
    }
}
```

**Example 2: 首次查询防火墙日志**

首次查询传入 LogType；如果 Data.HasMore 为 true，保存 Data.NextToken 用于续查。

Input: 

```
tccli cfw DescribeCfwLogs --cli-unfold-argument  \
    --LogType cfw_netflow_border \
    --Query src_ip:1.1.1.1 \
    --TimeRange 1h \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "Data": "{\"Items\":[{\"src_ip\":\"1.1.1.1\"}],\"TotalCount\":1,\"Limit\":100,\"HasMore\":true,\"NextToken\":\"opaque-token\"}",
        "RequestId": "4266525E-10C4-41E1-8A28-5CCE1FBF6A58"
    }
}
```

