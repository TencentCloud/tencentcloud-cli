**Example 1: 创建一个有2份子合同的合同组签署流程（B2B、B2C）,并通过FlowGroupOptions控制签署人通知方式**

1.子合同1是B2B合同 （Approvers中有两个ApproverInfo元素）
2.子合同2是B2C合同 （Approvers中有两个ApproverInfo元素，C端签署人ApproverType是1）
3.此合同组下所有子合同，C端签署人使用手机号验证校验方式 （FlowGroupOptions.ApproverVerifyType 设置为MobileCheck）
4.此合同组下所有子合同，发起方企业经办人不通知，需要发起方自行通知（FlowGroupOptions.SelfOrganizationApproverNotifyType 设置为none）
5.此合同组下所有子合同，他方企业经办人通过短信通知（FlowGroupOptions.OtherApproverNotifyType 设置为sms）


Input: 

```
tccli ess CreateFlowGroupByFiles --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --FlowGroupName 示例合同组-有3份子合同 \
    --FlowGroupInfos.0.FileIds yDwgAUUckp1tbkbgUukJIiCyj7014en1 \
    --FlowGroupInfos.0.FlowName 子合同1-B2B(发起方企业自动签署) \
    --FlowGroupInfos.0.FlowDescription 子合同1 \
    --FlowGroupInfos.0.FlowType 示例合同 \
    --FlowGroupInfos.0.Approvers.0.ApproverType 0 \
    --FlowGroupInfos.0.Approvers.0.OrganizationName 典子谦示例企业 \
    --FlowGroupInfos.0.Approvers.0.ApproverName 典子谦 \
    --FlowGroupInfos.0.Approvers.0.ApproverMobile 18251952320 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentWidth 100 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.FileIndex 0 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentType SIGN_SEAL \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentPage 1 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentRequired True \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentPosX 100 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentPosY 100 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentHeight 100 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentValue yDxMjUyKQDN7EkUuO4zjEBpGXvHEACSA \
    --FlowGroupInfos.0.Approvers.1.ApproverName 张三 \
    --FlowGroupInfos.0.Approvers.1.ApproverType 0 \
    --FlowGroupInfos.0.Approvers.1.OrganizationName 张三示例企业 \
    --FlowGroupInfos.0.Approvers.1.ApproverMobile 18888888888 \
    --FlowGroupInfos.0.Approvers.1.SignComponents.0.ComponentWidth 100 \
    --FlowGroupInfos.0.Approvers.1.SignComponents.0.FileIndex 0 \
    --FlowGroupInfos.0.Approvers.1.SignComponents.0.ComponentType SIGN_SEAL \
    --FlowGroupInfos.0.Approvers.1.SignComponents.0.ComponentPage 1 \
    --FlowGroupInfos.0.Approvers.1.SignComponents.0.ComponentRequired True \
    --FlowGroupInfos.0.Approvers.1.SignComponents.0.ComponentPosX 100 \
    --FlowGroupInfos.0.Approvers.1.SignComponents.0.ComponentPosY 200 \
    --FlowGroupInfos.0.Approvers.1.SignComponents.0.ComponentHeight 100 \
    --FlowGroupInfos.0.Unordered True \
    --FlowGroupInfos.1.FileIds yDwgAUUckp1tbkbgUukJIiCyj7014en2 \
    --FlowGroupInfos.1.FlowName 子合同2-普通B2C \
    --FlowGroupInfos.1.Deadline 0 \
    --FlowGroupInfos.1.FlowDescription 子合同2 \
    --FlowGroupInfos.1.FlowType 示例合同 \
    --FlowGroupInfos.1.Approvers.0.ApproverType 0 \
    --FlowGroupInfos.1.Approvers.0.OrganizationName 王五示例企业 \
    --FlowGroupInfos.1.Approvers.0.ApproverName 王五 \
    --FlowGroupInfos.1.Approvers.0.ApproverMobile 13700000000 \
    --FlowGroupInfos.1.Approvers.0.SignComponents.0.ComponentWidth 100 \
    --FlowGroupInfos.1.Approvers.0.SignComponents.0.FileIndex 0 \
    --FlowGroupInfos.1.Approvers.0.SignComponents.0.ComponentType SIGN_SEAL \
    --FlowGroupInfos.1.Approvers.0.SignComponents.0.ComponentPage 1 \
    --FlowGroupInfos.1.Approvers.0.SignComponents.0.ComponentRequired True \
    --FlowGroupInfos.1.Approvers.0.SignComponents.0.ComponentPosX 100 \
    --FlowGroupInfos.1.Approvers.0.SignComponents.0.ComponentPosY 100 \
    --FlowGroupInfos.1.Approvers.0.SignComponents.0.ComponentHeight 100 \
    --FlowGroupInfos.1.Approvers.0.SignComponents.0.ComponentValue  \
    --FlowGroupInfos.1.Approvers.1.ApproverType 1 \
    --FlowGroupInfos.1.Approvers.1.ApproverName 典子谦 \
    --FlowGroupInfos.1.Approvers.1.ApproverMobile 13200000000 \
    --FlowGroupInfos.1.Approvers.1.SignComponents.0.ComponentWidth 100 \
    --FlowGroupInfos.1.Approvers.1.SignComponents.0.FileIndex 0 \
    --FlowGroupInfos.1.Approvers.1.SignComponents.0.ComponentType SIGN_SIGNATURE \
    --FlowGroupInfos.1.Approvers.1.SignComponents.0.ComponentPage 1 \
    --FlowGroupInfos.1.Approvers.1.SignComponents.0.ComponentRequired True \
    --FlowGroupInfos.1.Approvers.1.SignComponents.0.ComponentPosX 100 \
    --FlowGroupInfos.1.Approvers.1.SignComponents.0.ComponentPosY 200 \
    --FlowGroupInfos.1.Approvers.1.SignComponents.0.ComponentHeight 100 \
    --FlowGroupInfos.1.Unordered True \
    --FlowGroupOptions.ApproverVerifyType MobileCheck \
    --FlowGroupOptions.SelfOrganizationApproverNotifyType none \
    --FlowGroupOptions.OtherApproverNotifyType sms
```

Output: 
```
{
    "Response": {
        "FlowGroupId": "yDwJ7UUckpk84plbUyPWcjISvuv6WMJx",
        "FlowIds": [
            "yDwJ7UUckpk84ploUyPWcjIS9KmiX55F",
            "yDwJ7UUckpk84plvUyPWcjIxKfGMJ9fF",
            "yDwJ7UUckpk84plaUyPWcjIvgnAvfS3H"
        ],
        "RequestId": "s1694572486923868447"
    }
}
```

**Example 2: 创建一个有3份子合同的合同组签署流程（B2B（含自动签署）、B2B、B2C）**

1. 子合同1为B2B合同（Approvers中包含两个ApproverInfo元素）；
2. 子合同1的发起方企业自动签署（ApproverType设置为3，SIGN_SEAL对应签署控件的ComponentValue设置为自动签署使用的印章Id）；
3. 子合同2为普通B2B合同（Approvers中包含两个ApproverInfo元素，且ApproverType都是0）；
4. 子合同3为普通B2C合同（Approvers中包含两个ApproverInfo元素，C端签署人的ApproverType为1）。

Input: 

```
tccli ess CreateFlowGroupByFiles --cli-unfold-argument  \
    --Operator.UserId yDwf2UUckps3me1aUuRbyBJvD8CIgM4K \
    --FlowGroupName 示例合同组-有3份子合同 \
    --FlowGroupInfos.0.FileIds yDwgAUUckp1tbkbgUukJIiCyj7014en1 \
    --FlowGroupInfos.0.FlowName 子合同1-B2B(发起方企业自动签署) \
    --FlowGroupInfos.0.FlowDescription 子合同1 \
    --FlowGroupInfos.0.FlowType 示例合同 \
    --FlowGroupInfos.0.Approvers.0.ApproverType 3 \
    --FlowGroupInfos.0.Approvers.0.OrganizationName 典子谦示例企业 \
    --FlowGroupInfos.0.Approvers.0.ApproverName 典子谦 \
    --FlowGroupInfos.0.Approvers.0.ApproverMobile 18251952320 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentWidth 100 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.FileIndex 0 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentType SIGN_SEAL \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentPage 1 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentRequired True \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentPosX 100 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentPosY 100 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentHeight 100 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentValue yDxMjUyKQDN7EkUuO4zjEBpGXvHEACSA \
    --FlowGroupInfos.0.Approvers.1.ApproverName 张三 \
    --FlowGroupInfos.0.Approvers.1.ApproverType 0 \
    --FlowGroupInfos.0.Approvers.1.OrganizationName 张三示例企业 \
    --FlowGroupInfos.0.Approvers.1.ApproverMobile 18888888888 \
    --FlowGroupInfos.0.Approvers.1.SignComponents.0.ComponentWidth 100 \
    --FlowGroupInfos.0.Approvers.1.SignComponents.0.FileIndex 0 \
    --FlowGroupInfos.0.Approvers.1.SignComponents.0.ComponentType SIGN_SEAL \
    --FlowGroupInfos.0.Approvers.1.SignComponents.0.ComponentPage 1 \
    --FlowGroupInfos.0.Approvers.1.SignComponents.0.ComponentRequired True \
    --FlowGroupInfos.0.Approvers.1.SignComponents.0.ComponentPosX 100 \
    --FlowGroupInfos.0.Approvers.1.SignComponents.0.ComponentPosY 200 \
    --FlowGroupInfos.0.Approvers.1.SignComponents.0.ComponentHeight 100 \
    --FlowGroupInfos.0.Unordered True \
    --FlowGroupInfos.1.FileIds yDwgAUUckp1tbkbgUukJIiCyj7014en2 \
    --FlowGroupInfos.1.FlowName 子合同2-普通B2B \
    --FlowGroupInfos.1.FlowDescription 子合同2 \
    --FlowGroupInfos.1.FlowType 示例合同 \
    --FlowGroupInfos.1.CallbackUrl  \
    --FlowGroupInfos.1.Approvers.0.ApproverType 0 \
    --FlowGroupInfos.1.Approvers.0.OrganizationName 典子谦示例企业 \
    --FlowGroupInfos.1.Approvers.0.ApproverName 典子谦 \
    --FlowGroupInfos.1.Approvers.0.ApproverMobile 18251952320 \
    --FlowGroupInfos.1.Approvers.0.SignComponents.0.ComponentWidth 100 \
    --FlowGroupInfos.1.Approvers.0.SignComponents.0.FileIndex 0 \
    --FlowGroupInfos.1.Approvers.0.SignComponents.0.ComponentType SIGN_SEAL \
    --FlowGroupInfos.1.Approvers.0.SignComponents.0.ComponentPage 1 \
    --FlowGroupInfos.1.Approvers.0.SignComponents.0.ComponentRequired True \
    --FlowGroupInfos.1.Approvers.0.SignComponents.0.ComponentPosX 100 \
    --FlowGroupInfos.1.Approvers.0.SignComponents.0.ComponentPosY 100 \
    --FlowGroupInfos.1.Approvers.0.SignComponents.0.ComponentHeight 100 \
    --FlowGroupInfos.1.Approvers.0.SignComponents.0.ComponentValue  \
    --FlowGroupInfos.1.Approvers.1.ApproverType 0 \
    --FlowGroupInfos.1.Approvers.1.OrganizationName 李四示例企业 \
    --FlowGroupInfos.1.Approvers.1.ApproverName 李四 \
    --FlowGroupInfos.1.Approvers.1.ApproverMobile 15100000000 \
    --FlowGroupInfos.1.Approvers.1.SignComponents.0.ComponentWidth 100 \
    --FlowGroupInfos.1.Approvers.1.SignComponents.0.FileIndex 0 \
    --FlowGroupInfos.1.Approvers.1.SignComponents.0.ComponentType SIGN_SEAL \
    --FlowGroupInfos.1.Approvers.1.SignComponents.0.ComponentPage 1 \
    --FlowGroupInfos.1.Approvers.1.SignComponents.0.ComponentRequired True \
    --FlowGroupInfos.1.Approvers.1.SignComponents.0.ComponentPosX 100 \
    --FlowGroupInfos.1.Approvers.1.SignComponents.0.ComponentPosY 200 \
    --FlowGroupInfos.1.Approvers.1.SignComponents.0.ComponentHeight 100 \
    --FlowGroupInfos.1.Unordered True \
    --FlowGroupInfos.2.FileIds yDwgAUUckp1tbkbgUukJIiCyj7014en3 \
    --FlowGroupInfos.2.FlowName 子合同3-普通B2C \
    --FlowGroupInfos.2.Deadline 0 \
    --FlowGroupInfos.2.FlowDescription 子合同3 \
    --FlowGroupInfos.2.FlowType 示例合同 \
    --FlowGroupInfos.2.Approvers.0.ApproverType 0 \
    --FlowGroupInfos.2.Approvers.0.OrganizationName 王五示例企业 \
    --FlowGroupInfos.2.Approvers.0.ApproverName 王五 \
    --FlowGroupInfos.2.Approvers.0.ApproverMobile 13700000000 \
    --FlowGroupInfos.2.Approvers.0.SignComponents.0.ComponentWidth 100 \
    --FlowGroupInfos.2.Approvers.0.SignComponents.0.FileIndex 0 \
    --FlowGroupInfos.2.Approvers.0.SignComponents.0.ComponentType SIGN_SEAL \
    --FlowGroupInfos.2.Approvers.0.SignComponents.0.ComponentPage 1 \
    --FlowGroupInfos.2.Approvers.0.SignComponents.0.ComponentRequired True \
    --FlowGroupInfos.2.Approvers.0.SignComponents.0.ComponentPosX 100 \
    --FlowGroupInfos.2.Approvers.0.SignComponents.0.ComponentPosY 100 \
    --FlowGroupInfos.2.Approvers.0.SignComponents.0.ComponentHeight 100 \
    --FlowGroupInfos.2.Approvers.0.SignComponents.0.ComponentValue  \
    --FlowGroupInfos.2.Approvers.1.ApproverType 1 \
    --FlowGroupInfos.2.Approvers.1.ApproverName 典子谦 \
    --FlowGroupInfos.2.Approvers.1.ApproverMobile 13200000000 \
    --FlowGroupInfos.2.Approvers.1.SignComponents.0.ComponentWidth 100 \
    --FlowGroupInfos.2.Approvers.1.SignComponents.0.FileIndex 0 \
    --FlowGroupInfos.2.Approvers.1.SignComponents.0.ComponentType SIGN_SIGNATURE \
    --FlowGroupInfos.2.Approvers.1.SignComponents.0.ComponentPage 1 \
    --FlowGroupInfos.2.Approvers.1.SignComponents.0.ComponentRequired True \
    --FlowGroupInfos.2.Approvers.1.SignComponents.0.ComponentPosX 100 \
    --FlowGroupInfos.2.Approvers.1.SignComponents.0.ComponentPosY 200 \
    --FlowGroupInfos.2.Approvers.1.SignComponents.0.ComponentHeight 100 \
    --FlowGroupInfos.2.Unordered True
```

Output: 
```
{
    "Response": {
        "FlowGroupId": "yDwJ7UUckpk84praUyPWcjISDLsIVxyo",
        "FlowIds": [
            "yDwJ7UUckpk84prkUyPWcjIufyhLeqjP",
            "yDwJ7UUckpk84prtUyPWcjIwX73sJYGC",
            "yDwJ7UUckpk84pryUyPWcjI11TGDLwGO"
        ],
        "RequestId": "s1694570527888078574"
    }
}
```

**Example 3: 通过主代子方式创建一个有3份子合同的合同组签署流程（B2B（含自动签署）、B2B、B2C）**

1. 通过主代子方式发起合同（Agent.ProxyOrganizationId设置为子企业的电子签企业Id）；
2. 子合同1为B2B合同（Approvers中包含两个ApproverInfo元素，且ApproverType都是0）；
3. 子合同1的发起方企业自动签署（ApproverType设置为3，SIGN_SEAL对应签署控件的ComponentValue设置为自动签署使用的印章Id）；
4. 子合同2为普通B2B合同（Approvers中包含两个ApproverInfo元素，且ApproverType都是0）；
5. 子合同3为普通B2C合同（Approvers中包含两个ApproverInfo元素，C端签署人的ApproverType为1）。

Input: 

```
tccli ess CreateFlowGroupByFiles --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --Agent.ProxyOrganizationId yDRSRUUgygj6qnwfUuO4zjEwc193c2hH \
    --FlowGroupName 示例合同组-3份子合同 \
    --FlowGroupInfos.0.FileIds yDwgAUUckp1tbkbgUukJIiCyj7014en1 \
    --FlowGroupInfos.0.FlowName 子合同1-B2B(发起方企业自动签署) \
    --FlowGroupInfos.0.FlowDescription 子合同1 \
    --FlowGroupInfos.0.FlowType 示例合同 \
    --FlowGroupInfos.0.Approvers.0.ApproverType 3 \
    --FlowGroupInfos.0.Approvers.0.OrganizationName 典子谦示例企业 \
    --FlowGroupInfos.0.Approvers.0.ApproverName 典子谦 \
    --FlowGroupInfos.0.Approvers.0.ApproverMobile 18251952320 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentWidth 100 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.FileIndex 0 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentType SIGN_SEAL \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentPage 1 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentRequired True \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentPosX 100 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentPosY 100 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentHeight 100 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentValue yDxMjUyKQDN7EkUuO4zjEBpGXvHEACSA \
    --FlowGroupInfos.0.Approvers.1.ApproverName 张三 \
    --FlowGroupInfos.0.Approvers.1.ApproverType 0 \
    --FlowGroupInfos.0.Approvers.1.OrganizationName 张三示例企业 \
    --FlowGroupInfos.0.Approvers.1.ApproverMobile 18888888888 \
    --FlowGroupInfos.0.Approvers.1.SignComponents.0.ComponentWidth 100 \
    --FlowGroupInfos.0.Approvers.1.SignComponents.0.FileIndex 0 \
    --FlowGroupInfos.0.Approvers.1.SignComponents.0.ComponentType SIGN_SEAL \
    --FlowGroupInfos.0.Approvers.1.SignComponents.0.ComponentPage 1 \
    --FlowGroupInfos.0.Approvers.1.SignComponents.0.ComponentRequired True \
    --FlowGroupInfos.0.Approvers.1.SignComponents.0.ComponentPosX 100 \
    --FlowGroupInfos.0.Approvers.1.SignComponents.0.ComponentPosY 200 \
    --FlowGroupInfos.0.Approvers.1.SignComponents.0.ComponentHeight 100 \
    --FlowGroupInfos.0.Unordered True \
    --FlowGroupInfos.1.FileIds yDwgAUUckp1tbkbgUukJIiCyj7014en2 \
    --FlowGroupInfos.1.FlowName 子合同2-普通B2B \
    --FlowGroupInfos.1.FlowDescription 子合同2 \
    --FlowGroupInfos.1.FlowType 示例合同 \
    --FlowGroupInfos.1.CallbackUrl  \
    --FlowGroupInfos.1.Approvers.0.ApproverType 0 \
    --FlowGroupInfos.1.Approvers.0.OrganizationName 典子谦示例企业 \
    --FlowGroupInfos.1.Approvers.0.ApproverName 典子谦 \
    --FlowGroupInfos.1.Approvers.0.ApproverMobile 18251952320 \
    --FlowGroupInfos.1.Approvers.0.SignComponents.0.ComponentWidth 100 \
    --FlowGroupInfos.1.Approvers.0.SignComponents.0.FileIndex 0 \
    --FlowGroupInfos.1.Approvers.0.SignComponents.0.ComponentType SIGN_SEAL \
    --FlowGroupInfos.1.Approvers.0.SignComponents.0.ComponentPage 1 \
    --FlowGroupInfos.1.Approvers.0.SignComponents.0.ComponentRequired True \
    --FlowGroupInfos.1.Approvers.0.SignComponents.0.ComponentPosX 100 \
    --FlowGroupInfos.1.Approvers.0.SignComponents.0.ComponentPosY 100 \
    --FlowGroupInfos.1.Approvers.0.SignComponents.0.ComponentHeight 100 \
    --FlowGroupInfos.1.Approvers.0.SignComponents.0.ComponentValue  \
    --FlowGroupInfos.1.Approvers.1.ApproverType 0 \
    --FlowGroupInfos.1.Approvers.1.OrganizationName 李四示例企业 \
    --FlowGroupInfos.1.Approvers.1.ApproverName 李四 \
    --FlowGroupInfos.1.Approvers.1.ApproverMobile 15100000000 \
    --FlowGroupInfos.1.Approvers.1.SignComponents.0.ComponentWidth 100 \
    --FlowGroupInfos.1.Approvers.1.SignComponents.0.FileIndex 0 \
    --FlowGroupInfos.1.Approvers.1.SignComponents.0.ComponentType SIGN_SEAL \
    --FlowGroupInfos.1.Approvers.1.SignComponents.0.ComponentPage 1 \
    --FlowGroupInfos.1.Approvers.1.SignComponents.0.ComponentRequired True \
    --FlowGroupInfos.1.Approvers.1.SignComponents.0.ComponentPosX 100 \
    --FlowGroupInfos.1.Approvers.1.SignComponents.0.ComponentPosY 200 \
    --FlowGroupInfos.1.Approvers.1.SignComponents.0.ComponentHeight 100 \
    --FlowGroupInfos.1.Unordered True \
    --FlowGroupInfos.2.FileIds yDwgAUUckp1tbkbgUukJIiCyj7014en3 \
    --FlowGroupInfos.2.FlowName 子合同3-普通B2C \
    --FlowGroupInfos.2.Deadline 0 \
    --FlowGroupInfos.2.FlowDescription 子合同3 \
    --FlowGroupInfos.2.FlowType 示例合同 \
    --FlowGroupInfos.2.Approvers.0.ApproverType 0 \
    --FlowGroupInfos.2.Approvers.0.OrganizationName 王五示例企业 \
    --FlowGroupInfos.2.Approvers.0.ApproverName 王五 \
    --FlowGroupInfos.2.Approvers.0.ApproverMobile 13700000000 \
    --FlowGroupInfos.2.Approvers.0.SignComponents.0.ComponentWidth 100 \
    --FlowGroupInfos.2.Approvers.0.SignComponents.0.FileIndex 0 \
    --FlowGroupInfos.2.Approvers.0.SignComponents.0.ComponentType SIGN_SEAL \
    --FlowGroupInfos.2.Approvers.0.SignComponents.0.ComponentPage 1 \
    --FlowGroupInfos.2.Approvers.0.SignComponents.0.ComponentRequired True \
    --FlowGroupInfos.2.Approvers.0.SignComponents.0.ComponentPosX 100 \
    --FlowGroupInfos.2.Approvers.0.SignComponents.0.ComponentPosY 100 \
    --FlowGroupInfos.2.Approvers.0.SignComponents.0.ComponentHeight 100 \
    --FlowGroupInfos.2.Approvers.0.SignComponents.0.ComponentValue  \
    --FlowGroupInfos.2.Approvers.1.ApproverType 1 \
    --FlowGroupInfos.2.Approvers.1.ApproverName 典子谦 \
    --FlowGroupInfos.2.Approvers.1.ApproverMobile 13200000000 \
    --FlowGroupInfos.2.Approvers.1.SignComponents.0.ComponentWidth 100 \
    --FlowGroupInfos.2.Approvers.1.SignComponents.0.FileIndex 0 \
    --FlowGroupInfos.2.Approvers.1.SignComponents.0.ComponentType SIGN_SIGNATURE \
    --FlowGroupInfos.2.Approvers.1.SignComponents.0.ComponentPage 1 \
    --FlowGroupInfos.2.Approvers.1.SignComponents.0.ComponentRequired True \
    --FlowGroupInfos.2.Approvers.1.SignComponents.0.ComponentPosX 100 \
    --FlowGroupInfos.2.Approvers.1.SignComponents.0.ComponentPosY 200 \
    --FlowGroupInfos.2.Approvers.1.SignComponents.0.ComponentHeight 100 \
    --FlowGroupInfos.2.Unordered True
```

Output: 
```
{
    "Response": {
        "FlowGroupId": "yDwJ8UUckpk84plbUyPWcjISvuv6WMJx",
        "FlowIds": [
            "yDwJ8UUckpk84ploUyPWcjIS9KmiX55F",
            "yDwJ8UUckpk84plvUyPWcjIxKfGMJ9fF",
            "yDwJ8UUckpk84plaUyPWcjIvgnAvfS3H"
        ],
        "RequestId": "s1694572486923868447"
    }
}
```

