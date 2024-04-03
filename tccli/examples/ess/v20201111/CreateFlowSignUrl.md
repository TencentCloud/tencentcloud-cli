**Example 1: 创建个人用户H5签署链接**

发起流程后，给其中的C端签署人创建签署链接

Input: 

```
tccli ess CreateFlowSignUrl --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --FlowApproverInfos.0.ApproverType 1 \
    --FlowApproverInfos.0.ApproverMobile 13200000000 \
    --FlowApproverInfos.0.ApproverName 典子谦 \
    --FlowId yDwFmUUckpstqfvzUE1h3jo1f3cqjkGm
```

Output: 
```
{
    "Response": {
        "FlowApproverUrlInfos": [
            {
                "ApproverMobile": "13200000000",
                "ApproverName": "典子谦",
                "ApproverType": 1,
                "LongUrl": "https://quick.test.qian.tencent.cn/home?ApproverIdCardNumber=Mi**Kio2&ApproverMobile=MTk***NjA%3D&ApproverName=%25**A&ApproverType=1&Code=yDwJCUUck****V2R5K&CodeType=QUICK&FlowId=yDwF**1f3cqjkGm&ShowHeader=1&shortKey=yDwq5**M5GlG1c&token=bR8**HA",
                "SignUrl": "https://essurl.cn/bR8**HA"
            }
        ],
        "RequestId": "s1693832180480950012"
    }
}
```

**Example 2: 创建企业用户H5签署链接**

发起流程后，给其中的B端签署人创建签署链接

Input: 

```
tccli ess CreateFlowSignUrl --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --FlowApproverInfos.0.ApproverType 0 \
    --FlowApproverInfos.0.ApproverMobile 13200000000 \
    --FlowApproverInfos.0.ApproverName 典子谦 \
    --FlowApproverInfos.0.OrganizationName ***有限公司 \
    --FlowId yDwFmUUckpstqfvzUE1h3jo1f3cqjkGm
```

Output: 
```
{
    "Response": {
        "FlowApproverUrlInfos": [
            {
                "ApproverMobile": "13200000000",
                "ApproverName": "典子谦",
                "ApproverType": 0,
                "LongUrl": "https://quick.test.qian.tencent.cn/home?ApproverIdCardNumber=Mi**Kio2&ApproverMobile=MTk***NjA%3D&ApproverName=%25**A&ApproverType=0&Code=yDwJCUUck****V2R5K&CodeType=QUICK&FlowId=yDwF**1f3cqjkGm&ShowHeader=1&shortKey=yDwq5**M5GlG1c&token=bR8**HA",
                "SignUrl": "https://essurl.cn/bR8**HA"
            }
        ],
        "RequestId": "s1693832180480950012"
    }
}
```

**Example 3: 创建企业用户H5预览链接**

发起流程后，给其中的B端签署人创建预览链接

Input: 

```
tccli ess CreateFlowSignUrl --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --FlowApproverInfos.0.ApproverType 0 \
    --FlowApproverInfos.0.ApproverMobile 13200000000 \
    --FlowApproverInfos.0.ApproverName 典子谦 \
    --FlowApproverInfos.0.OrganizationName ***有限公司 \
    --UrlType 1 \
    --FlowId yDwFmUUckpstqfvzUE1h3jo1f3cqjkGm
```

Output: 
```
{
    "Response": {
        "FlowApproverUrlInfos": [
            {
                "ApproverMobile": "13200000000",
                "ApproverName": "典子谦",
                "ApproverType": 0,
                "LongUrl": "https://quick.test.qian.tencent.cn/home?ApproverIdCardNumber=Mi**Kio2&ApproverMobile=MTk***NjA%3D&ApproverName=%25**A&ApproverType=0&Code=yDwJCUUck****V2R5K&CodeType=QUICK&FlowId=yDwF**1f3cqjkGm&ShowHeader=1&shortKey=yDwq5**M5GlG1c&token=bR8**HA",
                "SignUrl": "https://essurl.cn/bR8**HA"
            }
        ],
        "RequestId": "s1693832180480950012"
    }
}
```

**Example 4: 创建合同发起方预览链接**

发起流程后，给其中的合同发起方创建预览链接

Input: 

```
tccli ess CreateFlowSignUrl --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --UrlType 1 \
    --FlowId yDwFmUUckpstqfvzUE1h3jo1f3cqjkGm
```

Output: 
```
{
    "Response": {
        "FlowApproverUrlInfos": [
            {
                "ApproverMobile": "",
                "ApproverName": "",
                "ApproverType": 0,
                "LongUrl": "https://quick.test.qian.tencent.cn/home?ApproverIdCardNumber=Mi**Kio2&ApproverMobile=MTk***NjA%3D&ApproverName=%25**A&PreviewType=2&Code=yDwJCUUck****V2R5K&CodeType=QUICK&FlowId=yDwF**1f3cqjkGm&ShowHeader=1&shortKey=yDwq5**M5GlG1c&token=bR8**HA",
                "SignUrl": "https://essurl.cn/bR8**HA"
            }
        ],
        "RequestId": "s1693832180480950012"
    }
}
```

**Example 5: 创建个人用户H5签署链接，使用视频认证方式**

发起流程后，给其中的C端签署人创建签署链接，并且使用视频认证方式

Input: 

```
tccli ess CreateFlowSignUrl --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --FlowApproverInfos.0.ApproverType 1 \
    --FlowApproverInfos.0.ApproverMobile 13200000000 \
    --FlowApproverInfos.0.ApproverName 典子谦 \
    --FlowApproverInfos.0.ApproverSignTypes 1 \
    --FlowApproverInfos.0.Intention.IntentionType 1 \
    --FlowApproverInfos.0.Intention.IntentionQuestions.0.Question 请问，您是否同意签署本协议？可语音回复“同意”或“不同意”。 \
    --FlowApproverInfos.0.Intention.IntentionQuestions.0.Answers 同意 我同意 \
    --FlowId yDwFmUUckpstqfvzUE1h3jo1f3cqjkGm
```

Output: 
```
{
    "Response": {
        "FlowApproverUrlInfos": [
            {
                "ApproverMobile": "13200000000",
                "ApproverName": "典子谦",
                "ApproverType": 1,
                "LongUrl": "https://quick.test.qian.tencent.cn/home?ApproverIdCardNumber=Mi**Kio2&ApproverMobile=MTk***NjA%3D&ApproverName=%25**A&ApproverType=1&Code=yDwJCUUck****V2R5K&CodeType=QUICK&FlowId=yDwF**1f3cqjkGm&ShowHeader=1&shortKey=yDwq5**M5GlG1c&token=bR8**HA",
                "SignUrl": "https://essurl.cn/bR8**HA"
            }
        ],
        "RequestId": "s1693832180480950012"
    }
}
```

**Example 6: 错误示例-创建个人用户签署链接，传错签署人姓名**

1. 给个人用户创建签署链接
2. 用户姓名不是合同的参与人

Input: 

```
tccli ess CreateFlowSignUrl --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --FlowApproverInfos.0.ApproverType 1 \
    --FlowApproverInfos.0.ApproverMobile 13200000000 \
    --FlowApproverInfos.0.ApproverName 张三 \
    --FlowId yDwFmUUckpstqfvzUE1h3jo1f3cqjkGm
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "ResourceNotFound",
            "Message": "无法找到参与人"
        },
        "RequestId": "s1693832578941223891"
    }
}
```

**Example 7: 创建个人用户H5签署链接(签署完成后跳转到指定地址)**

1. 给个人用户创建签署链接
2. 签署完成后跳转到指定页面地址(设置跳转地址JumpUrl)

Input: 

```
tccli ess CreateFlowSignUrl --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --FlowApproverInfos.0.ApproverType 1 \
    --FlowApproverInfos.0.ApproverMobile 13200000000 \
    --FlowApproverInfos.0.ApproverName 典子谦 \
    --JumpUrl https://www.example.com \
    --FlowId yDwFmUUckpstqfvzUE1h3jo1f3cqjkGm
```

Output: 
```
{
    "Response": {
        "FlowApproverUrlInfos": [
            {
                "ApproverMobile": "13200000000",
                "ApproverName": "典子谦",
                "ApproverType": 1,
                "LongUrl": "https://quick.test.qian.tencent.cn/home?ApproverIdCardNumber=MioqKi**Kio2&ApproverMobile=MTk***NjA%3D&ApproverName=%25**A&ApproverType=1&Code=yDwJCUUck****V2R5K&CodeType=QUICK&FlowId=yDwF**1f3cqjkGm&ShowHeader=1&shortKey=yDwq5**M5GlG1c&token=bR8**HA",
                "SignUrl": "https://essurl.cn/bR8**HA"
            }
        ],
        "RequestId": "s1693832180480950012"
    }
}
```

**Example 8: 错误示例-创建个人用户签署链接，该用户还有些控件需要填写**

1. 给个人用户创建签署链接
2. 该个人用户除了签署控件，还有填写控件需要补充

Input: 

```
tccli ess CreateFlowSignUrl --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --FlowApproverInfos.0.ApproverType 1 \
    --FlowApproverInfos.0.ApproverMobile 13200000000 \
    --FlowApproverInfos.0.ApproverName 典子谦 \
    --FlowId yDwFmUUckpstqfvzUE1h3jo1f3cqjkGm
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation",
            "Message": "该用户有暂不支持H5端的控件，请删除后重新发起流程"
        },
        "RequestId": "s1693901602090298421"
    }
}
```

