**Example 1: 创建协议端口模板**

创建协议端口模板

Input: 

```
tccli vpc CreateServiceTemplate --cli-unfold-argument  \
    --ServiceTemplateName TestName \
    --Services TCP:8080 UDP:99
```

Output: 
```
{
    "Response": {
        "ServiceTemplate": {
            "ServiceTemplateName": "TestName",
            "ServiceTemplateId": "ppm-bu8cir16",
            "ServiceSet": [
                "tcp: 8080",
                "udp: 99"
            ],
            "CreatedTime": "2018-04-03 21:19:31",
            "ServiceExtraSet": [
                {
                    "Description": "xx",
                    "Service": "xx"
                }
            ]
        },
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239"
    }
}
```

