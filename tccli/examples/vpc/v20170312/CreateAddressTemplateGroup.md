**Example 1: 创建IP地址模版集合**



Input: 

```
tccli vpc CreateAddressTemplateGroup --cli-unfold-argument  \
    --Version 2017-03-12\
    --AddressTemplateGroupName TestName\
    --AddressTemplateIds ipm-88t6207k ipm-mdunqeb6
```

Output: 
```
{
    "Response": {
        "AddressTemplateGroup": {
            "AddressTemplateGroupName": "TestName",
            "AddressTemplateGroupId": "ipmg-dih8xdbq",
            "AddressTemplateIdSet": [
                "ipm-88t6207k",
                "ipm-mdunqeb6"
            ],
            "CreatedTime": "2018-04-03 21:51:02"
        },
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239"
    }
}
```

