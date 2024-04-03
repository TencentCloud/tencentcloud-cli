**Example 1: 延期签署方的签署截止时间**

1.将签署流程yDCNtUUckpvrezq3UudRJ1LEXDLa8Lga 中 签署人角色编号 yDwhyUUckp2cmuh4Uu2bfpvRH48OvSw7 对应的签署人设置的签署截止时间延长到1705976964

Input: 

```
tccli ess ModifyFlowDeadline --cli-unfold-argument  \
    --Operator.UserId yDRt2UUgygqxyp7yUuO5zjEwqXwsIljA \
    --FlowId yDCNtUUckpvrezq3UudRJ1LEXDLa8Lga \
    --Deadline 1705976964 \
    --RecipientId yDwhyUUckp2cmuh4Uu2bfpvRH48OvSw7
```

Output: 
```
{
    "Response": {
        "RequestId": "s1705924585583461780"
    }
}
```

**Example 2: 延期签署方的签署截止时间失败-签署流程已过期**

1.将签署流程yDCNtUUckpvrezq3UudRJ1LEXDLa9Lga中 签署人角色编号yDwhyUUckp2cmuh4Uu2bfpvRH48OvSw8 对应的签署人设置的签署截止时间延长到1705976980
2.此时合同已经过期，无法操作

Input: 

```
tccli ess ModifyFlowDeadline --cli-unfold-argument  \
    --Operator.UserId yDRt2UUgygqxyp7yUuO5zjEwqXwsIljA \
    --FlowId yDCNtUUckpvrezq3UudRJ1LEXDLa9Lga \
    --Deadline 1705976980 \
    --RecipientId yDwhyUUckp2cmuh4Uu2bfpvRH48OvSw8
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation",
            "Message": "此签署流程已经终止，当前处于流程已经过期状态，无法进行延期操作，请确认后重试"
        },
        "RequestId": "s1705991274996790452"
    }
}
```

**Example 3: 延期整个合同-合同发起时有签署人单独设置了签署截止时间**

1.合同发起时设置合同截止时间为1704988032，该合同有3个签署人A，B，C
2.合同发起时A签署人设置签署截止时间为1704978032，B，C签署人未单独设置签署人截止时间（默认和合同保持一致）
3.通过接口对整个合同延期后，A签署人截止时间不变（还是1704978032），B，C签署人的签署截止时间和合同截止时间延期为1705977064

Input: 

```
tccli ess ModifyFlowDeadline --cli-unfold-argument  \
    --Operator.UserId yDRt2UUgygqxyp7yUuO5zjEwqXwsIljA \
    --FlowId yDCNtUUckpvrcvf4UELZnZDvMStFgT7K \
    --Deadline 1705977064
```

Output: 
```
{
    "Response": {
        "RequestId": "s1705924585583461781"
    }
}
```

**Example 4: 延期整个合同-合同发起时没有签署人设置签署人签署截止时间**

1.合同发起时设置合同截止时间为1704988032，该合同有3个签署人A，B，C
2.合同发起时并未为签署人未单独设置签署人截止时间（默认和合同保持一致）
3.通过接口对整个合同延期后，A，B，C签署人的签署截止时间和合同截止时间延期为1705977064

Input: 

```
tccli ess ModifyFlowDeadline --cli-unfold-argument  \
    --Operator.UserId yDRt2UUgygqxyp7yUuO5zjEwqXwsIljA \
    --FlowId yDCNtUUckpvrcvf4UELZnZDvMStFgT7K \
    --Deadline 1705977064
```

Output: 
```
{
    "Response": {
        "RequestId": "s1705924585583461781"
    }
}
```

