**Example 1: 结束动态签署合同**

所有签署方都签署完成，并且不再新增签署方时，结束该动态签署合同

Input: 

```
tccli ess ArchiveDynamicFlow --cli-unfold-argument  \
    --Operator.ClientIp 1.1.1.1 \
    --Operator.UserId yDxZtUyKQD2JuqUuO4zjERYGxxxxxxxx \
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
        "RequestId": "abc"
    }
}
```

**Example 2: 归档失败**

未签署完成前归档

Input: 

```
tccli ess ArchiveDynamicFlow --cli-unfold-argument  \
    --Operator.UserId yDwf3UUckps8dvveUEfH3DjvMmg3ZkjQ \
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

**Example 3: 归档合同**

所有签署方签署完成后，结束动态合同

Input: 

```
tccli ess ArchiveDynamicFlow --cli-unfold-argument  \
    --Operator.UserId yDwf3UUckps8dvveUEfH3DjvMmg3ZkjQ \
    --FlowId yDCjFUUckp48fiwyUyh7ukYEdXdSyJps
```

Output: 
```
{
    "Response": {
        "Approvers": [
            {
                "RecipientId": "yDCjFUUckp48fiwbUyh7ukYE1kRDNNN4",
                "SignId": "yDCjFUUckp48fiwwUyh7ukYvjx5PR1e2"
            }
        ],
        "FlowId": "yDCjFUUckp48fiwyUyh7ukYEdXdSyJps",
        "RequestId": "ca0fd107-4337-4650-8236-aa3e4561f7ef"
    }
}
```

