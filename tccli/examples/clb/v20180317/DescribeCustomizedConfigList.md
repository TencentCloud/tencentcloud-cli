**Example 1: 拉取配置列表**



Input: 

```
tccli clb DescribeCustomizedConfigList --cli-unfold-argument  \
    --ConfigType CLB \
    --Offset 0 \
    --Limit 3
```

Output: 
```
{
    "Response": {
        "ConfigList": [
            {
                "UconfigId": "pz-go2gs3d6",
                "ConfigType": "CLB",
                "ConfigContent": "client_max_body_size 1m;",
                "ConfigName": "122222",
                "CreateTimestamp": "2019-11-28 20:44:24",
                "UpdateTimestamp": "2020-03-01 11:11:27"
            }
        ],
        "TotalCount": 1,
        "RequestId": "d6f74bc7-2b26-4f5f-9dd8-6f0c8e8e2cc2"
    }
}
```

