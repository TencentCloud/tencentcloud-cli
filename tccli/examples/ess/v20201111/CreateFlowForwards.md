**Example 1: 将当前合同经办人转为其他员工**

将当前合同经办人转为其他员工

Input: 

```
tccli ess CreateFlowForwards --cli-unfold-argument  \
    --TargetUserId yDCkSUUck******************BQnKvKPVf \
    --FlowForwardInfos.0.FlowId yDtSPUU**********************PHG7JhZM \
    --FlowForwardInfos.0.RecipientId yDtSPUU******************os8flxcvLpj \
    --FlowForwardInfos.1.FlowId yDtSPUU**********************PHG7s8flx \
    --FlowForwardInfos.1.RecipientId yDtSPUU******************oSPUxSP \
    --Operator.UserId yDtSPUU******************p4z5lt9UuY \
    --Operator.ClientIp 116.211.195.11
```

Output: 
```
{
    "Response": {
        "FailedFlows": [
            {
                "ErrorDetail": "转发人状态非待签署或待填写，禁止转发",
                "FlowId": "yDtSPUU**********************PHG7JhZM"
            }
        ],
        "RequestId": "s1740641173120185806",
        "SuccessFlows": [
            "yDtSPUU**********************PHG7s8flx"
        ]
    }
}
```

