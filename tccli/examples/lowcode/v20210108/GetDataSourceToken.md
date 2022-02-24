**Example 1: 获取数据源授权token示例**



Input: 

```
tccli lowcode GetDataSourceToken --cli-unfold-argument  \
    --DataSourceId xx
```

Output: 
```
{
    "Response": {
        "Data": {
            "QQDocsToken": {
                "OpenId": "xx",
                "ClientId": "xx",
                "AccessToken": "xx",
                "TokenType": "xx",
                "Scope": "xx"
            },
            "MeetingToken": {
                "OpenId": "xx",
                "AccessToken": "xx"
            }
        },
        "RequestId": "xx"
    }
}
```

