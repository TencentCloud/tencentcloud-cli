**Example 1: 查询IP地址模板集合**



Input: 

```
tccli vpc DescribeAddressTemplateGroups --cli-unfold-argument  \
    --Version 2017-03-12 \
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
        "AddressTemplateGroupSet": [
            {
                "AddressTemplateGroupName": "TestName",
                "AddressTemplateGroupId": "ipmg-2uw6ujo6",
                "AddressTemplateIdSet": [
                    "ipm-mdunqeb6"
                ],
                "AddressTemplateSet": [
                    {
                        "AddressTemplateId": "ipm-mdunqeb6",
                        "AddressTemplateName": "test"
                    }
                ],
                "CreatedTime": "2017-12-31 14:09:13"
            }
        ],
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239"
    }
}
```

