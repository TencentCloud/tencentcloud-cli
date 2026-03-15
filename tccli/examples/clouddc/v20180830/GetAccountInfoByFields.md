**Example 1: 示例**



Input: 

```
tccli clouddc GetAccountInfoByFields --cli-unfold-argument  \
    --Fields channelmark account_info \
    --Id 12334556
```

Output: 
```
{
    "Response": {
        "JsonString": "{\"account_info\":{\"uin\":\"12334556\",\"cid\":\"xxxxxx\",\"name\":\"JOSHUA\\u5f00\\u53d1\\u4e13\\u7528\",\"auth_name\":\"joshua\\u5f00\\u53d1\\u4e13\\u7528\",\"reg_time\":\"2016-05-14 15:32:05\",\"create_time\":\"2019-05-08 16:29:25\",\"country\":\"US\",\"auth_state\":3}}",
        "RequestId": "16066096-46cf-4db0-971a-9a5a29cd4b9a"
    }
}
```

