**Example 1: 创建并返回出证报告**

通过已完成签署的流程FlowId，发起出证请求，获取出证报告的ID。

Input: 

```
tccli essbasic CreateChannelFlowEvidenceReport --cli-unfold-argument  \
    --FlowId yDR0PUUhw8ahh****KyK18G1h3FK5ccC \
    --Agent.ProxyOrganizationOpenId test1_clara_xxxxxrganization1 \
    --Agent.AppId 7f349*********984a9657b0ec \
    --Agent.ProxyOperator.OpenId channel-super-*****-openId0001
```

Output: 
```
{
    "Response": {
        "ReportUrl": "",
        "Status": "EvidenceStatusSuccess",
        "ReportId": "yDRspUUgyxxxxxUur7PA0xEQpJXh2b",
        "RequestId": "s166141****028448367"
    }
}
```

**Example 2: 错误示例：流程未签署完，请求出证失败**

流程FlowId必须处于全部签署完成的状态，否则请求将无法成功。

Input: 

```
tccli essbasic CreateChannelFlowEvidenceReport --cli-unfold-argument  \
    --FlowId yDR0PUUhw8ahh****KyK18G1h3FK5ccd \
    --Agent.ProxyOrganizationOpenId test1_clara_xxxxxrganization1 \
    --Agent.AppId 7f349*********984a9657b0ec \
    --Agent.ProxyOperator.OpenId channel-super-*****-openId0001
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "OperationDenied.FlowStatusForbid",
            "Message": "当前流程状态不支持出证"
        },
        "RequestId": "s1692***********72"
    }
}
```

