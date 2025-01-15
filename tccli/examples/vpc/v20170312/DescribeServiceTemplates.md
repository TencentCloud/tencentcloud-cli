**Example 1: 查看协议端口模板**

查看协议端口模板

Input: 

```
tccli vpc DescribeServiceTemplates --cli-unfold-argument  \
    --Filters.0.Name service-template-name \
    --Filters.0.Values demo \
    --Limit 2
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ServiceTemplateSet": [
            {
                "ServiceTemplateName": "demo",
                "ServiceTemplateId": "ppm-bu8cir16",
                "ServiceSet": [
                    "tcp:8080",
                    "udp:99"
                ],
                "ServiceExtraSet": [
                    {
                        "Service": "tcp:8080",
                        "Description": ""
                    },
                    {
                        "Service": "udp:99",
                        "Description": ""
                    }
                ],
                "CreatedTime": "2018-04-03 21:19:31"
            }
        ],
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239"
    }
}
```

