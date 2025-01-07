**Example 1: 创建协议端口模板集合**

创建协议端口模板集合

Input: 

```
tccli vpc CreateServiceTemplateGroup --cli-unfold-argument  \
    --ServiceTemplateGroupName demo \
    --ServiceTemplateIds ppm-529nwwj8 ppm-4dw6agho
```

Output: 
```
{
    "Response": {
        "ServiceTemplateGroup": {
            "ServiceTemplateGroupName": "demo",
            "ServiceTemplateGroupId": "ppmg-2klmrefu",
            "ServiceTemplateIdSet": [
                "ppm-529nwwj8",
                "ppm-4dw6agho"
            ],
            "ServiceTemplateSet": [
                {
                    "ServiceTemplateId": "demo",
                    "ServiceTemplateName": "demo",
                    "ServiceSet": [],
                    "ServiceExtraSet": [],
                    "CreatedTime": "2018-04-03 22:05:32"
                }
            ],
            "CreatedTime": "2018-04-03 22:05:32"
        },
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239"
    }
}
```

