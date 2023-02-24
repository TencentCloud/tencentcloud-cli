**Example 1: 拉取配置绑定的server或location**

拉取配置绑定的server或location

Input: 

```
tccli clb DescribeCustomizedConfigAssociateList --cli-unfold-argument  \
    --UconfigId pz-fi018waq \
    --Offset 0 \
    --Limit 3
```

Output: 
```
{
    "Response": {
        "BindList": [
            {
                "LoadBalancerId": "lb-az5a9oyo",
                "ListenerId": "lbl-nppnktey",
                "Domain": "www.aaa.com",
                "LocationId": "loc-nppnktey",
                "ListenerName": "test",
                "Protocol": "http",
                "Vport": 80,
                "Url": "",
                "UconfigId": "pz-n651fsue"
            }
        ],
        "TotalCount": 1,
        "RequestId": "83129908-a282-4f9f-8ab-131a3025ba11"
    }
}
```

