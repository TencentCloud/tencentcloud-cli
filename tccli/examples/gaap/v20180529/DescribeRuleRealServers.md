**Example 1: 查询转发规则相关源站信息**

查询转发规则相关源站信息

Input: 

```
tccli gaap DescribeRuleRealServers --cli-unfold-argument  \
    --RuleId rule-gsy1amjd
```

Output: 
```
{
    "Response": {
        "RequestId": "dc73988c-7888-4b9a-b9a4-a0f36a495f3c",
        "TotalCount": 2,
        "RealServerSet": [
            {
                "RealServerIP": "2.5.73.1",
                "RealServerId": "rs-5y1674pn",
                "RealServerName": "pocnetwork_gaap_test_rs_ip",
                "ProjectId": 1321988,
                "InBanBlacklist": 0
            },
            {
                "RealServerIP": "43.132.182.170",
                "RealServerId": "rs-cz4ipit1",
                "RealServerName": "pocnetwork_gaap_test_rs_ip",
                "ProjectId": 1321988,
                "InBanBlacklist": 0
            }
        ],
        "BindRealServerSet": [],
        "BindRealServerTotalCount": 0
    }
}
```

