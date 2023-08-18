**Example 1: 查询IP地址模板集合**

查询IP地址模板集合

Input: 

```
tccli vpc DescribeAddressTemplateGroups --cli-unfold-argument  \
    --Filters.0.Name address-template-group-name \
    --Filters.0.Values TestName \
    --Filters.1.Name address-template-group-id \
    --Filters.1.Values ipmg-mdunqeb6
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "1111",
        "AddressTemplateGroupSet": [
            {
                "AddressTemplateGroupName": "test",
                "AddressTemplateGroupId": "ipmg-xxxxxxxx",
                "AddressTemplateIdSet": [
                    "ipm-xxxxxxxx",
                    "ipm-yyyyyyyy"
                ],
                "AddressTemplateSet": [
                    {
                        "AddressTemplateId": "ipm-xxxxxxxx",
                        "AddressTemplateName": "xxxxxxxx",
                        "From": "",
                        "To": ""
                    },
                    {
                        "AddressTemplateId": "ipm-yyyyyyyy",
                        "AddressTemplateName": "yyyyyyyy",
                        "From": "",
                        "To": ""
                    }
                ],
                "CreatedTime": "2022-12-06 20:00:00"
            }
        ]
    }
}
```

