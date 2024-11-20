**Example 1: 查看协议端口模板集合**

查看协议端口模板集合

Input: 

```
tccli vpc DescribeServiceTemplateGroups --cli-unfold-argument  \
    --Filters.0.Name service-template-group-name \
    --Filters.0.Values demo \
    --Limit 2
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ServiceTemplateGroupSet": [
            {
                "ServiceTemplateGroupName": "demo",
                "ServiceTemplateGroupId": "ppmg-2klmrefu",
                "ServiceTemplateIdSet": [
                    "ppm-529nwwj8"
                ],
                "ServiceTemplateSet": [
                    {
                        "ServiceTemplateId": "ppm-529nwwj8",
                        "ServiceTemplateName": "demo",
                        "CreatedTime": "2018-04-03 22:05:32",
                        "ServiceSet": [
                            "tcp:80"
                        ],
                        "ServiceExtraSet": [
                            {
                                "Service": "tcp:80",
                                "Description": "web service"
                            }
                        ]
                    }
                ],
                "CreatedTime": "2018-04-03 22:05:32"
            }
        ],
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239"
    }
}
```

