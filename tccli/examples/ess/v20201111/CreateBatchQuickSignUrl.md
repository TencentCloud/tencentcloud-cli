**Example 1: 为个人用户，创建合同组批量签署链接**

1. 为个人用户生成合同组H5批量签署链接
2. 使用默认的签名类型
3. 使用默认的签署方式
4. 默认跳转到合同列表页

Input: 

```
tccli ess CreateBatchQuickSignUrl --cli-unfold-argument  \
    --Operator.ClientIp 1.2.3.4 \
    --Operator.UserId yDxVwUyKQWho8CUuO4zjEyQOAgwvr4Zy \
    --FlowApproverInfo.ApproverType 1 \
    --FlowApproverInfo.ApproverMobile 13200000000 \
    --FlowApproverInfo.ApproverName 典子谦 \
    --FlowApproverInfo.ApproverIdCardNumber 620000198802020000 \
    --FlowApproverInfo.ApproverIdCardType ID_CARD \
    --FlowGroupId yDSLcUUck****ysv1OQYIe9H
```

Output: 
```
{
    "Response": {
        "FlowApproverUrlInfo": {
            "ApproverMobile": "13200000000",
            "ApproverName": "典子谦",
            "ApproverType": 1,
            "LongUrl": "https://quick.qian.tencent.cn/guide?Code=yDwi0U**xoK&CodeType=QUICK&shortKey=yDw**S2ATh95&token=Y9b**O",
            "SignUrl": "https://essurl.cn/Y9b**O"
        },
        "RequestId": "s169**68"
    }
}
```

**Example 2: 集团主企业代子企业创建H5批量签署链接**

1. 集团主企业有权限代替子企业发起合同
2. 个人用户在批量签署的合同中是待签署的状态
3. 签署的合同中个人用户没有填写控件，只有签名控件
4. 主企业的版本符合专业版及以上企业版本
5. 批量签署链接中指定签名类型为手写签名和OCR楷体签名
6. 批量签署链接中指定意愿确认方式为人脸认证和手机号认证

Input: 

```
tccli ess CreateBatchQuickSignUrl --cli-unfold-argument  \
    --Operator.ClientIp 1.2.3.4 \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --Agent.ProxyOrganizationId yDxbNUyKQDx3oAUuO4zjEBQGidlGe4hP \
    --FlowApproverInfo.ApproverType 1 \
    --FlowApproverInfo.ApproverMobile 13200000000 \
    --FlowApproverInfo.ApproverName 典子谦 \
    --FlowApproverInfo.ApproverIdCardNumber 620000198802020000 \
    --FlowApproverInfo.ApproverIdCardType ID_CARD \
    --SignatureTypes 0 1 \
    --ApproverSignTypes 1 3 \
    --FlowIds yDwFmUUckpstqfvzUE1h3jo1f3cqjkGm yDwFmUUckpst10i3UubBSat8PWOt2iQF
```

Output: 
```
{
    "Response": {
        "FlowApproverUrlInfo": {
            "ApproverMobile": "13200000000",
            "ApproverName": "典子谦",
            "ApproverType": 1,
            "LongUrl": "https://quick.qian.tencent.cn/guide?Code=yDwi0U**xoK&CodeType=QUICK&shortKey=yDw**S2ATh95&token=Y9b**O",
            "SignUrl": "https://essurl.cn/Y9b**O"
        },
        "RequestId": "s169**68"
    }
}
```

**Example 3: 发起合同后，为C端签署人创建H5批量签署链接**

1. 创建批量签署链接的企业与待批量签署的合同属于同一个企业
2. 批量签署的合同数量不少于1份，不超过100份
3. 上述合同均为待该C端签署人签署状态
4. 该C端签署人仅有手写签名控件，不需要填写合同
5. 企业已经购买了专业版或以上版本套餐

Input: 

```
tccli ess CreateBatchQuickSignUrl --cli-unfold-argument  \
    --ApproverSignTypes 1 3 \
    --FlowApproverInfo.ApproverIdCardNumber 620000198802020000 \
    --FlowApproverInfo.ApproverIdCardType ID_CARD \
    --FlowApproverInfo.ApproverMobile 13200000000 \
    --FlowApproverInfo.ApproverName 典子谦 \
    --FlowApproverInfo.ApproverType 1 \
    --FlowIds yDwFmUUckpstqfvzUE1h3jo1f3cqjkGm yDwFmUUckpst10i3UubBSat8PWOt2iQF \
    --JumpUrl https://abc.com \
    --SignatureTypes 0 1
```

Output: 
```
{
    "Response": {
        "FlowApproverUrlInfo": {
            "ApproverMobile": "13200000000",
            "ApproverName": "典子谦",
            "ApproverType": 1,
            "LongUrl": "https://quick.qian.tencent.cn/guide?Code=yDwiB**FOE&CodeType=QUICK&shortKey=yDwiB**1e5&token=Rg0**Q",
            "SignUrl": "https://essurl.cn/Rg0**Q"
        },
        "RequestId": "s1698**9686"
    }
}
```

**Example 4: 创建H5批量签署链接，签署完成后跳转到指定地址**

1. 个人用户在批量签署的合同中是待签署的状态
2. 签署的合同中个人用户没有填写控件，只有签名控件
3. 企业的版本符合专业版及以上企业版本
4. 批量签署链接中指定签名类型为手写签名和OCR楷体签名
5. 批量签署链接中指定意愿确认方式为人脸认证和手机号认证
6. 批量签署链接中指定签署完成后的跳转地址为https://abc.com

Input: 

```
tccli ess CreateBatchQuickSignUrl --cli-unfold-argument  \
    --Operator.ClientIp 1.2.3.4 \
    --Operator.UserId yDxVwUyKQWho8CUuO4zjEyQOAgwvr4Zy \
    --FlowApproverInfo.ApproverType 1 \
    --FlowApproverInfo.ApproverMobile 13200000000 \
    --FlowApproverInfo.ApproverName 典子谦 \
    --FlowApproverInfo.ApproverIdCardNumber 620000198802020000 \
    --FlowApproverInfo.ApproverIdCardType ID_CARD \
    --JumpUrl https://abc.com \
    --SignatureTypes 0 1 \
    --ApproverSignTypes 1 3 \
    --FlowIds yDwFmUUckpstqfvzUE1h3jo1f3cqjkGm yDwFmUUckpst10i3UubBSat8PWOt2iQF
```

Output: 
```
{
    "Response": {
        "FlowApproverUrlInfo": {
            "ApproverMobile": "13200000000",
            "ApproverName": "典子谦",
            "ApproverType": 1,
            "LongUrl": "https://quick.qian.tencent.cn/guide?Code=yDwi0U**xoK&CodeType=QUICK&shortKey=yDw**S2ATh95&token=Y9b**O",
            "SignUrl": "https://essurl.cn/Y9b**O"
        },
        "RequestId": "s169**68"
    }
}
```

**Example 5: 错误示例-创建签署链接的企业不是待批量签署合同的发起方**

1. 企业A创建了一些合同
2. 企业B用上述合同编号创建批量签署链接

Input: 

```
tccli ess CreateBatchQuickSignUrl --cli-unfold-argument  \
    --Operator.ClientIp 1.2.3.4 \
    --Operator.UserId yDxVwUyKQWho8CUuO4zjEyQOAgwvr4Zy \
    --FlowApproverInfo.ApproverType 1 \
    --FlowApproverInfo.ApproverMobile 13200000000 \
    --FlowApproverInfo.ApproverName 典子谦 \
    --FlowApproverInfo.ApproverIdCardNumber 620000198802020000 \
    --FlowApproverInfo.ApproverIdCardType ID_CARD \
    --SignatureTypes 0 1 \
    --ApproverSignTypes 1 3 \
    --FlowIds yDwFkUUckpstzjhfUugNAWf1KibXqS26
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation",
            "Message": "不支持非当前企业发起的合同，生成批量签署链接。不满足合同:[\"yDwFkUUckpstzjhfUugNAWf1KibXqS26\"]"
        },
        "RequestId": "s1698**02"
    }
}
```

**Example 6: 错误示例-创建签署链接中指定的C端个人用户不在合同参与人列表中**

1. 合同已经创建完成，其中个人用户为A
2. 创建个人H5批量签署链接中的ApproverType指定了个人类型(ApproverType=1)
3. 创建个人H5批量签署链接中的姓名、手机号、证件信息指定为用户B

Input: 

```
tccli ess CreateBatchQuickSignUrl --cli-unfold-argument  \
    --Operator.ClientIp 1.2.3.4 \
    --Operator.UserId yDxVwUyKQWho8CUuO4zjEyQOAgwvr4Zy \
    --FlowApproverInfo.ApproverType 1 \
    --FlowApproverInfo.ApproverMobile 13200000000 \
    --FlowApproverInfo.ApproverName 典子谦 \
    --FlowApproverInfo.ApproverIdCardNumber 620000198802020000 \
    --FlowApproverInfo.ApproverIdCardType ID_CARD \
    --SignatureTypes 0 1 \
    --ApproverSignTypes 1 3 \
    --FlowIds yDwFkUUckpstzjhfUugNAWf1KibXqS26
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation",
            "Message": "在合同[yDwFkUUckpstzjhfUugNAWf1KibXqS26]中无法找到参与人[姓名：典子谦,手机号：13200000000,证件号：620000198802020000,证件类型：ID_CARD,参与人类型：1]"
        },
        "RequestId": "s1698**53"
    }
}
```

**Example 7: 错误示例，为个人用户生成H5批量签署链接，没有指定合同流程ID信息，也没有指定合同组ID信息**

1. 没有指定合同流程ID信息
2. 没有指定合同组ID信息

Input: 

```
tccli ess CreateBatchQuickSignUrl --cli-unfold-argument  \
    --Operator.ClientIp 1.2.3.4 \
    --Operator.UserId yDxVwUyKQWho8CUuO4zjEyQOAgwvr4Zy \
    --FlowApproverInfo.ApproverType 1 \
    --FlowApproverInfo.ApproverMobile 13200000000 \
    --FlowApproverInfo.ApproverName 典子谦 \
    --FlowApproverInfo.ApproverIdCardNumber 620000198802020000 \
    --FlowApproverInfo.ApproverIdCardType ID_CARD
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation",
            "Message": "流程ID和合同组ID不能同时为空，请检查参数后再试"
        },
        "RequestId": "s17007***76147"
    }
}
```

**Example 8: 发起合同后，获取C端签署人的H5批量领取链接**

1. 创建批量签署链接的合同签署方，必须都是动态签署人且未补充。
2. 批量签署的合同数量不少于1份，不超过100份
3. 上述合同签署方类型必须一致，均为待C端签署人签署状态
4. 企业已经购买了专业版或以上版本套餐

Input: 

```
tccli ess CreateBatchQuickSignUrl --cli-unfold-argument  \
    --ApproverSignTypes 1 3 \
    --FlowApproverInfo.ApproverType 1 \
    --FlowIds yDwFmUUckpstqfvzUE1h3jo1f3cqjkGm yDwFmUUckpst10i3UubBSat8PWOt2iQF \
    --JumpUrl https://abc.com \
    --SignatureTypes 0 1 \
    --FlowBatchUrlInfo.FlowBatchApproverInfos.0.FlowId yDwFmUUckpstqfvzUE1h3jo1f3cqjkGm \
    --FlowBatchUrlInfo.FlowBatchApproverInfos.0.RecipientId yDCmvUUckpup6xhwUxKRs1rIRejg254i \
    --FlowBatchUrlInfo.FlowBatchApproverInfos.1.FlowId yDwFmUUckpst10i3UubBSat8PWOt2iQF \
    --FlowBatchUrlInfo.FlowBatchApproverInfos.1.RecipientId yDCmvUUckpup6xh1UxKRs1rwHjT5QyHH
```

Output: 
```
{
    "Response": {
        "FlowApproverUrlInfo": {
            "ApproverMobile": "",
            "ApproverName": "",
            "ApproverType": 1,
            "LongUrl": "https://quick.qian.tencent.cn/guide?Code=yDwiB**FOE&CodeType=QUICK&shortKey=yDwiB**1e5&token=Rg0**Q",
            "SignUrl": "https://essurl.cn/Rg0**Q"
        },
        "RequestId": "s1698**9686"
    }
}
```

**Example 9: 为个人用户，创建合同组批量签署链接,并且指定视频问答模式的认证方式**

1. 为个人用户生成合同组H5批量签署链接
2. 使用默认的签名类型
3. 使用默认的签署方式
4. 默认跳转到合同列表页
5.指定视频问答模式的认证方式

Input: 

```
tccli ess CreateBatchQuickSignUrl --cli-unfold-argument  \
    --Operator.ClientIp 1.2.3.4 \
    --Operator.UserId yDxVwUyKQWho8CUuO4zjEyQOAgwvr4Zy \
    --FlowApproverInfo.ApproverType 1 \
    --FlowApproverInfo.ApproverMobile 13200000000 \
    --FlowApproverInfo.ApproverName 典子谦 \
    --FlowApproverInfo.ApproverIdCardNumber 620000198802020000 \
    --FlowApproverInfo.ApproverIdCardType ID_CARD \
    --FlowGroupId yDSLcUUck****ysv1OQYIe9H \
    --ApproverSignTypes 1 \
    --Intention.IntentionType 1 \
    --Intention.IntentionQuestions.0.Question 请问，您是否同意签署本协议？可语音回复“同意”或“不同意”。 \
    --Intention.IntentionQuestions.0.Answers 同意 我同意
```

Output: 
```
{
    "Response": {
        "FlowApproverUrlInfo": {
            "ApproverMobile": "13200000000",
            "ApproverName": "典子谦",
            "ApproverType": 1,
            "LongUrl": "https://quick.qian.tencent.cn/guide?Code=yDwi0U**xoK&CodeType=QUICK&shortKey=yDw**S2ATh95&token=Y9b**O",
            "SignUrl": "https://essurl.cn/Y9b**O"
        },
        "RequestId": "s169**68"
    }
}
```

**Example 10: 为企业用户，创建合同批量签署链接**

1. 为企业员工生成合同组H5批量签署链接
2. 使用默认的签署方式


Input: 

```
tccli ess CreateBatchQuickSignUrl --cli-unfold-argument  \
    --Operator.ClientIp 1.2.3.4 \
    --Operator.UserId yDxVwUyKQWho8CUuO4zjEyQOAgwvr4Zy \
    --FlowApproverInfo.ApproverType 1 \
    --FlowApproverInfo.ApproverMobile 13200000000 \
    --FlowApproverInfo.ApproverName 典员工 \
    --FlowApproverInfo.ApproverIdCardNumber 620000198802020000 \
    --FlowApproverInfo.ApproverIdCardType ID_CARD \
    --FlowApproverInfo.OrganizationName xxxx公司 \
    --FlowIds yDSLcUUck****ysv1OQYIe9H ysv1OQYIe9H****yDSLcUUck
```

Output: 
```
{
    "Response": {
        "FlowApproverUrlInfo": {
            "ApproverMobile": "13200000000",
            "ApproverName": "典员工",
            "ApproverType": 0,
            "LongUrl": "https://quick.qian.tencent.cn/guide?Code=yDwi0U**xoK&CodeType=QUICK&shortKey=yDw**S2ATh95&token=Y9b**O",
            "SignUrl": "https://essurl.cn/Y9b**O"
        },
        "RequestId": "s169**68"
    }
}
```

