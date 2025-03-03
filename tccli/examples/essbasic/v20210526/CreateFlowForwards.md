**Example 1: 将当前合同经办人转为其他员工**

将当前合同经办人转为其他员工

Input: 

```
tccli essbasic CreateFlowForwards --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --TargetOpenId open_id_1 \
    --FlowForwardInfos.0.FlowId yDtSPUU**********************PHG7JhZM \
    --FlowForwardInfos.0.RecipientId yDtSPUU******************os8flxcvLpj \
    --FlowForwardInfos.1.FlowId yDtSPUU**********************PHG7s8flx \
    --FlowForwardInfos.1.RecipientId yDtSPUU******************oSPUxSP
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

