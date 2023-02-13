**Example 1: 查询IP地址模板**

查询IP地址模板

Input: 

```
tccli vpc DescribeAddressTemplates --cli-unfold-argument  \
    --Filters.0.Name address-template-name \
    --Filters.0.Values TestName \
    --Filters.1.Name address-template-id \
    --Filters.1.Values ipm-mdunqeb6
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AddressTemplateSet": [
            {
                "AddressTemplateName": "TestName",
                "AddressTemplateId": "ipm-mdunqeb6",
                "AddressSet": [
                    "192.168.0.0/16",
                    "192.128.8.8/17"
                ],
                "AddressExtraSet": [
                    {
                        "Description": "desc",
                        "Address": "192.168.0.0/16"
                    },
                    {
                        "Description": "desc",
                        "Address": "192.128.8.8/17"
                    }
                ],
                "CreatedTime": "2017-12-31 10:06:05"
            }
        ],
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239"
    }
}
```

