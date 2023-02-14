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
        "RequestId": "xx",
        "AddressTemplateGroupSet": [
            {
                "CreatedTime": "2020-12-03 16:12:15",
                "AddressTemplateGroupName": "测试1",
                "AddressTemplateIdSet": [
                    "ipm-mdunqeb6"
                ],
                "AddressTemplateSet": [
                    {
                        "To": "10.1.1.2/22",
                        "From": "10.1.1.3/22"
                    }
                ],
                "AddressTemplateGroupId": "ipmg-ivrc58q8"
            }
        ]
    }
}
```

