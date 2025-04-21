**Example 1: 查询账号安全策略示例**

查询已配置的账号安全策略

Input: 

```
tccli ioa DescribeAccountSecurityPolicy --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "Description": "",
                    "Detail": "{\"AutoLoginSwitch\":2,\"TicketValidTime\":24}",
                    "ExpireTime": 0,
                    "Id": 29,
                    "Itime": "2022-11-17 16:39:05",
                    "Name": "基础策略",
                    "PolicyId": 29,
                    "PolicyName": "基础策略",
                    "PolicyType": 1,
                    "ScopeItems": [
                        {
                            "List": [],
                            "ScopeType": 1
                        },
                        {
                            "List": [
                                {
                                    "Id": 95,
                                    "IdPathArr": [
                                        95
                                    ],
                                    "Name": "全网账户"
                                }
                            ],
                            "ScopeType": 2
                        },
                        {
                            "List": [],
                            "ScopeType": 3
                        }
                    ],
                    "Status": 2,
                    "Utime": "2022-11-17 16:39:05"
                }
            ],
            "Page": {
                "PageCount": 1,
                "PageNum": 1,
                "PageSize": 100,
                "Total": 1
            }
        },
        "RequestId": "0c48aa3d-b95e-4e2d-a4a5-81e61ae5b3fa"
    }
}
```

