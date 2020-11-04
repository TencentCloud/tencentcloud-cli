**Example 1: 创建IP地址模版**



Input: 

```
tccli vpc CreateAddressTemplate --cli-unfold-argument  \
    --Version 2017-03-12\
    --AddressTemplateName TestName\
    --Addresses 192.168.1.0/24 192.168.2.0/24
```

Output: 
```
{
    "Response": {
        "AddressTemplate": {
            "AddressTemplateName": "TestName",
            "AddressTemplateId": "ipm-ht1gkq3a",
            "AddressSet": [
                "192.168.1.0/24",
                "192.168.2.0/24"
            ],
            "CreatedTime": "2018-04-03 21:38:01"
        },
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239"
    }
}
```

