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
                "UserId": "100000000",
                "Role": [
                    {
                        "Organization": "org",
                        "Role": "Admin"
                    }
                ],
                "Notes": "xx"
            }
        ],
        "RequestId": "qmunlpf51noe13qp5vyvg7mq5t4t4w6u"
    }
}
```

