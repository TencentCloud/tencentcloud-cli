**Example 1: 查询4层监听器源站列表**

查询4层监听器源站列表

Input: 

```
tccli gaap DescribeListenerRealServers --cli-unfold-argument  \
    --ListenerId listener-pbsgn7ej
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "RealServerSet": [
            {
                "RealServerId": "rs-2k5qnys5",
                "RealServerIP": "123.123.123.123",
                "RealServerName": "rs_test",
                "ProjectId": 0
            },
            {
                "RealServerId": "rs-d5y6ei2u",
                "RealServerIP": "118.89.46.86",
                "RealServerName": "rs_test-2",
                "ProjectId": 0
            }
        ],
        "BindRealServerTotalCount": 1,
        "BindRealServerSet": [
            {
                "RealServerId": "rs-d5y6ei2u",
                "RealServerIP": "118.89.46.86",
                "RealServerWeight": 0,
                "RealServerPort": 80,
                "RealBindStatus": 0
            }
        ],
        "RequestId": "38fab584-8d14-4e2c-988c-4acdabbf2dff"
    }
}
```

