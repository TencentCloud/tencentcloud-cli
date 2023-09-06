**Example 1: 撤销签署流程样例**

撤销单个签署流程

Input: 

```
tccli ess CancelFlow --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --FlowId yDwFmUUckpstqfvzUE1h3jo1f3cqjkGm \
    --CancelMessage 这个合同里边的付款金额写错了
```

Output: 
```
{
    "Response": {
        "RequestId": "85651ecc8"
    }
}
```

**Example 2: 错误示例-撤销一个已经签署完成的流程合同**

1. 合同已经签署完成
2. 撤销该合同

Input: 

```
tccli ess CancelFlow --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --FlowId yDwFkUUckpstzjhfUugNAWf1KibXqS26 \
    --CancelMessage 这个合同里边的付款金额写错了
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "OperationDenied.FlowHasTerminated",
            "Message": "此流程已经终止，当前所有参与者签署"
        },
        "RequestId": "s1693***537224"
    }
}
```

