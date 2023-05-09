**Example 1: 创建协议端口模板**

创建协议端口模板

Input: 

```
tccli vpc CreateServiceTemplate --cli-unfold-argument  \
    --ServiceTemplateName TestName \
    --Services TCP:8080
```

Output: 
```
{
    "Response": {
        "ServiceTemplate": {
            "ServiceTemplateName": "TestName",
            "ServiceTemplateId": "ppm-xxxxxxxx",
            "ServiceSet": [
                "tcp: 8080"
            ],
            "CreatedTime": "2018-04-03 21:19:31",
            "ServiceExtraSet": [
                {
                    "Description": "test",
                    "Service": "tcp:8080"
                }
            ]
        },
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239"
    }
}
```

