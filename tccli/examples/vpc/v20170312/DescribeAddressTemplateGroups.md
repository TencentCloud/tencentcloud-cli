**Example 1: 查询IP地址模板集合**

查询IP地址模板集合

Input: 

```
tccli vpc DescribeAddressTemplateGroups --cli-unfold-argument  \
    --Filters.0.Name address-template-group-name \
    --Filters.0.Values demo \
    --Filters.1.Name address-template-group-id \
    --Filters.1.Values ipmg-mdunqeb6
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "8ed052ce-dddf-4af9-9cf5-9c150ff75210",
        "AddressTemplateGroupSet": [
            {
                "AddressTemplateGroupName": "demo",
                "AddressTemplateGroupId": "ipmg-mdunqeb6",
                "AddressTemplateIdSet": [
                    "ipm-xxxxxxxx",
                    "ipm-yyyyyyyy"
                ],
                "AddressTemplateSet": [
                    {
                        "AddressTemplateId": "ipm-siqmaox1",
                        "AddressTemplateName": "ipm demo",
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

