**Example 1: B2B签署，补充签署流程本企业企业微信签署人信息**

在B2B签署中，双方签署方指定签署人类型为企业微信签署人，但未指定具体签署人时，需要进行企业微信签署人的补充。

Input: 

```
tccli ess CreateFlowApprovers --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --FlowId yDwFmUUckpstqfvzUE1h3jo1f3cqjkGm \
    --Approvers.0.RecipientId yDRS4UUgygqdcj2tUuO4zjEEFuP35Swc \
    --Approvers.0.ApproverSource WEWORKAPP \
    --Approvers.0.CustomUserId Zhangsan \
    --Approvers.1.RecipientId yDRS4UUgygqdcj2tUuO4zjEEFuP35Swc \
    --Approvers.1.ApproverSource WEWORKAPP \
    --Approvers.1.CustomUserId Lisi \
    --Approvers.2.RecipientId yDRS4UUgygqdcj51UuO4zjEyWTmzsIAR \
    --Approvers.2.ApproverSource WEWORKAPP \
    --Approvers.2.CustomUserId Wangwu \
    --Approvers.3.RecipientId yDRS4UUgygqdcj51UuO4zjEyWTmzsIAR \
    --Approvers.3.ApproverSource WEWORKAPP \
    --Approvers.3.CustomUserId ZhaoLiu
```

Output: 
```
{
    "Response": {
        "RequestId": "s1694694766993518983"
    }
}
```

**Example 2: B2B签署，补充签署流程本企业企业签署人信息**

在B2B签署中，双方签署方指定签署人类型为企业签署人，但未指定具体签署人时，需要进行企业签署人的补充。

Input: 

```
tccli ess CreateFlowApprovers --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --FlowId yDwFmUUckpstqfvzUE1h3jo1f3cqjkGm \
    --Approvers.0.RecipientId yDRS4UUgygqdcj51UuO4zjEyWTmzsIAR \
    --Approvers.0.ApproverName 典子谦 \
    --Approvers.0.ApproverMobile 13200000000 \
    --Approvers.1.RecipientId yDRS4UUgygqdcj51UuO4zjEyWTmzsIAR \
    --Approvers.1.ApproverName 张三 \
    --Approvers.1.ApproverMobile 18888888888 \
    --Approvers.2.RecipientId yDRS4UUgygqdcj2tUuO4zjEEFuP35Swc \
    --Approvers.2.ApproverName 李四 \
    --Approvers.2.ApproverMobile 15100000000 \
    --Approvers.3.RecipientId yDRS4UUgygqdcj2tUuO4zjEEFuP35Swc \
    --Approvers.3.ApproverName 王五 \
    --Approvers.3.ApproverMobile 13700000000
```

Output: 
```
{
    "Response": {
        "RequestId": "s1694694766993518983"
    }
}
```

**Example 3: B2B签署，补充签署流程本企业企业签署人和企业微信签署人信息**

在B2B签署中，如果第一方签署方指定企业签署人类型，但未指定具体签署人，需要进行企业签署人的补充指定；同时第二方签署方指定签署人为企业微信，但也未指定具体签署人，此时也需要进行企业微信签署人的补充。

Input: 

```
tccli ess CreateFlowApprovers --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --FlowId yDwFmUUckpstqfvzUE1h3jo1f3cqjkGm \
    --Approvers.0.RecipientId yDRS4UUgygqdcj51UuO4zjEyWTmzsIAR \
    --Approvers.0.ApproverName 典子谦 \
    --Approvers.0.ApproverMobile 13200000000 \
    --Approvers.1.RecipientId yDRS4UUgygqdcj51UuO4zjEyWTmzsIAR \
    --Approvers.1.ApproverName 张三 \
    --Approvers.1.ApproverMobile 18888888888 \
    --Approvers.2.RecipientId yDRS4UUgygqdcj2tUuO4zjEEFuP35Swc \
    --Approvers.2.ApproverSource WEWORKAPP \
    --Approvers.2.CustomUserId Wangwu \
    --Approvers.3.RecipientId yDRS4UUgygqdcj2tUuO4zjEEFuP35Swc \
    --Approvers.3.ApproverSource WEWORKAPP \
    --Approvers.3.CustomUserId ZhaoLiu
```

Output: 
```
{
    "Response": {
        "RequestId": "s1694694766993518983"
    }
}
```

**Example 4: 错误示例， B2B签署，补充签署流程本企业企业签署人使用了姓名和手机号进行补充报错**

错误示例，B2B签署，在B2B签署中，如果双方签署方均指定企业签署人类型为企业微信签署人，但都未指定具体签署人，且使用了姓名和手机号进行补充，这种方式是不被支持的。企业微信签署人的补充需要使用企业微信UserId进行补充。

Input: 

```
tccli ess CreateFlowApprovers --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --FlowId yDwFmUUckpstqfvzUE1h3jo1f3cqjkGm \
    --Approvers.0.RecipientId yDRS4UUgygqdcj51UuO4zjEyWTmzsIAR \
    --Approvers.0.ApproverName 典子谦 \
    --Approvers.0.ApproverMobile 13200000000 \
    --Approvers.1.RecipientId yDRS4UUgygqdcj51UuO4zjEyWTmzsIAR \
    --Approvers.1.ApproverName 张三 \
    --Approvers.1.ApproverMobile 18888888888 \
    --Approvers.2.RecipientId yDRS4UUgygqdcj2tUuO4zjEEFuP35Swc \
    --Approvers.2.ApproverSource WEWORKAPP \
    --Approvers.2.CustomUserId Wangwu \
    --Approvers.3.RecipientId yDRS4UUgygqdcj2tUuO4zjEEFuP35Swc \
    --Approvers.3.ApproverSource WEWORKAPP \
    --Approvers.3.CustomUserId ZhaoLiu
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "OperationDenied",
            "Message": "签署人RecipientId【yDRS4UUgygqdcj51UuO4zjEyWTmzsIAR】对应的签署人，在发起时限制补充企微或签签署人,请通过CustomUserId指定"
        },
        "RequestId": "s1694694766993518983"
    }
}
```

