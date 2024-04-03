**Example 1: 撤销合同部分成功**

撤销4个合同，并且自定义撤销理由，使用只保留身份信息的方式(CancelMessageFormat 设置为2) </br>
假设发起方是典子谦示例企业的经办人张三，这批合同撤销后，签署方看到的撤销理由是：发起方-典子谦示例企业以"合同内容错误，需要修正"的理由撤销当前合同</br>
其中合同yDmFdUUckpsvi8mpUEn0aFR1tWzReolk 已经签署完成，无法撤销。

Input: 

```
tccli essbasic ChannelBatchCancelFlows --cli-unfold-argument  \
    --Agent.AppId yDRSRUUgygj6qnwfUuO4zjEwc193c2hH \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --CancelMessage 合同内容错误，需要修正 \
    --CancelMessageFormat 1 \
    --FlowIds yDmFmUUckpstqfvzUE1h3jo1f3cqjkGa yDmFmUUckpst10i3UubBSat8PWOt2iQc yDmFdUUckpsvi8mpUEn0aFR1tWzReolk yDmFmUUckpst10i3UubBAat8PSOt2iJc
```

Output: 
```
{
    "Response": {
        "FailMessages": [
            "",
            "",
            "合同流程Id:yDmFdUUckpsvi8mpUEn0aFR1tWzReolk,无法撤回，错误信息：合同当前状态不支持撤销",
            ""
        ],
        "RequestId": "s1698669052286290493",
        "TaskId": "yDCVWUUckpwk3b05UyEZnO0xOn4snWWY"
    }
}
```

**Example 2: 自定义撤销理由，使用只保留身份信息的方式撤销合同**

撤销3个合同，并且自定义撤销理由，使用只保留身份信息的方式(CancelMessageFormat 设置为1) </br>
假设发起方是典子谦示例企业的经办人张三，这批合同撤销后，签署方看到的撤销理由是：发起方以"合同内容错误，需要修正"的理由撤销当前合同

Input: 

```
tccli essbasic ChannelBatchCancelFlows --cli-unfold-argument  \
    --Agent.AppId yDRSRUUgygj6qnwfUuO4zjEwc193c2hH \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --CancelMessage 合同内容错误，需要修正 \
    --CancelMessageFormat 1 \
    --FlowIds yDwFmUUckpstqfvzUE1h3jo1f3cqjkGa yDwFmUUckpst10i3UubBSat8PWOt2iQc yDwFdUUckpsvi8mpUEn0aFR1tWzReolk
```

Output: 
```
{
    "Response": {
        "FailMessages": [],
        "RequestId": "s1698667230378832487",
        "TaskId": "yDCVWUUckpwk3b05UyEZnO0xOn4snWWY"
    }
}
```

**Example 3: 自定义撤销理由，使用保留身份信息+企业名称的方式撤销合同**

撤销3个合同，并且自定义撤销理由，使用只保留身份信息的方式(CancelMessageFormat 设置为2) </br>
假设发起方是典子谦示例企业的经办人张三，这批合同撤销后，签署方看到的撤销理由是：发起方-典子谦示例企业以"合同内容错误，需要修正"的理由撤销当前合同

Input: 

```
tccli essbasic ChannelBatchCancelFlows --cli-unfold-argument  \
    --Agent.AppId yDRSRUUgygj6qnwfUuO4zjEwc193c2hH \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --CancelMessage 合同内容错误，需要修正 \
    --CancelMessageFormat 1 \
    --FlowIds yDmFmUUckpstqfvzUE1h3jo1f3cqjkGa yDmFmUUckpst10i3UubBSat8PWOt2iQc yDmFdUUckpsvi8mpUEn0aFR1tWzReolk
```

Output: 
```
{
    "Response": {
        "FailMessages": [],
        "RequestId": "s1698667230378832497",
        "TaskId": "yDCVWUUckpwk3b05UyEZnO0xOn4snWWY"
    }
}
```

**Example 4: 自定义撤销理由，保留身份信息+企业名称+经办人名称撤销合同**

撤销3个合同，并且自定义撤销理由，使用默认格式(CancelMessageFormat 设置为3) </br>
假设发起方是典子谦示例企业的经办人张三，这批合同撤销后，签署方看到的撤销理由是：发起方-典子谦示例企业-张三以"合同内容错误，需要修正"的理由撤销当前合同

Input: 

```
tccli essbasic ChannelBatchCancelFlows --cli-unfold-argument  \
    --Agent.AppId yDRSRUUgygj6qnwfUuO4zjEwc193c2hH \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --CancelMessage 合同内容错误，需要修正 \
    --CancelMessageFormat 3 \
    --FlowIds yDwFmUUckpstqfvzUE1h3jo1f3cqjkGm yDwFmUUckpst10i3UubBSat8PWOt2iQF yDwFdUUckpsvi8mpUEn0aFR1tWzReoTk
```

Output: 
```
{
    "Response": {
        "FailMessages": [],
        "RequestId": "s1698667230378832486",
        "TaskId": "yDCVWUUckpwk3b05UyEZnO0xOn4snWWY"
    }
}
```

