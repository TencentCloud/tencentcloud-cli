**Example 1: 查询服务级账号**

查询服务级账号

Input: 

```
tccli tcr DescribeServiceAccounts --cli-unfold-argument  \
    --RegistryId tcr-dg284imq \
    --All True \
    --EmbedPermission True \
    --Filters.0.Name ServiceAccountName \
    --Filters.0.Values tcr$account_test \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "6a0a32d8-3857-45d4-9f8a-e1d39efd8ac6",
        "ServiceAccounts": [
            {
                "CreateTime": "2024-12-30T14:44:31+08:00",
                "Description": "",
                "Disable": false,
                "ExpiresAt": 1738133070653,
                "Name": "tcr$account_test",
                "Permissions": [
                    {
                        "Actions": [
                            "tcr:PullRepository",
                            "tcr:DescribeHelmCharts"
                        ],
                        "Resource": "ns1"
                    },
                    {
                        "Actions": [
                            "tcr:PullRepository",
                            "tcr:PushRepository",
                            "tcr:CreateRepository",
                            "tcr:CreateHelmChart",
                            "tcr:DescribeHelmCharts"
                        ],
                        "Resource": "ns2"
                    }
                ],
                "UpdateTime": "2024-12-30T14:44:31+08:00"
            }
        ],
        "TotalCount": 1
    }
}
```

