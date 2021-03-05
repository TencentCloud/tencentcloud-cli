**Example 1: 获取CC自定义策略**



Input: 

```
tccli dayu DescribeCCSelfDefinePolicy --cli-unfold-argument  \
    --Business bgp \
    --Id bgp-000000xe
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Total": 1,
        "Policys": [
            {
                "SetId": 1262,
                "Name": "12434",
                "Smode": "matching",
                "Frequency": 0,
                "ExeMode": "drop",
                "Switch": 1,
                "CreateTime": "2019-04-24 12:32:12",
                "RuleList": [
                    {
                        "Skey": "host",
                        "Operator": "include",
                        "Value": "24234"
                    }
                ],
                "Protocol": "http",
                "Domain": ""
            }
        ]
    }
}
```

