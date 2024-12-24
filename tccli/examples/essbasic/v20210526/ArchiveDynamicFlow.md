**Example 1: 结束动态签署合同**

所有签署方都签署完成，并且不再新增签署方时，结束该动态签署合同


Input: 

```
tccli essbasic ArchiveDynamicFlow --cli-unfold-argument  \
    --Agent.ProxyOperator.OpenId openidxxxx \
    --Agent.ProxyOrganizationOpenId testorgopenid \
    --Agent.AppId 15edb41f2ee412f5ff533ac0185ebxxxxx \
    --FlowId yDCmVUUckpufezuiUxQQFiT8Exxxxxxxx
```

Output: 
```
{
    "Response": {
        "Approvers": [
            {
                "SignId": "yDCmDUUckpuf0hsfUuvalvQtaxxxxxxx",
                "RecipientId": "yDCmDUUckpuf0hseUuvalvQRmxxxxxx"
            }
        ],
        "FlowId": "yDCmDUUckpuf0hsmUuvalvQyxxxxxxxxx",
        "RequestId": "34ded0a6-e679-4af7-a07e-ca4573124213"
    }
}
```

**Example 2: 结束动态签署合同失败**

未签署完成前结束

Input: 

```
tccli essbasic ArchiveDynamicFlow --cli-unfold-argument  \
    --Agent.ProxyOperator.OpenId openidxxxx \
    --Agent.ProxyOrganizationOpenId testorgopenid \
    --Agent.AppId 15edb41f2ee412f5ff533ac0185ebxxxxx \
    --FlowId yDCjFUUckp4jkz76UoofpTx3iZ3A3C3x
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "OperationDenied",
            "Message": "当前合同状态不支持归档合同,请检查后重试"
        },
        "RequestId": "34ded0a6-e679-4af7-a07e-ca457e388499"
    }
}
```

