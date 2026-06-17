**Example 1: DescribeSSOAccount**

列出当前grafana实例的所有授权账号

Input: 

```
tccli monitor DescribeSSOAccount --cli-unfold-argument  \
    --InstanceId grafana-abcdefgh
```

Output: 
```
{
    "Response": {
        "AccountSet": [
            {
                "UserId": "1000001",
                "Role": [
                    {
                        "Organization": "1",
                        "Role": "Admin"
                    }
                ],
                "Notes": "账号备注",
                "CreateAt": "2020-09-22T00:00:00+00:00",
                "InstanceId": "grafana-abcdxxxx",
                "Uin": "1000002"
            }
        ],
        "RequestId": "xxxxxxxx"
    }
}
```

