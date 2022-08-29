**Example 1: 创建并返回出证报告**

获取全部签署完成得合同得出征报告，返回报告 URL

Input: 

```
tccli essbasic CreateChannelFlowEvidenceReport --cli-unfold-argument  \
    --FlowId yDR0PUUhw8ahh****KyK18G1h3FK5ccC \
    --Agent.ProxyOrganizationOpenId test1_clara_open_organization1 \
    --Agent.AppId 7f349*********984a9657b0ec \
    --Agent.ProxyOperator.OpenId channel-super-*****-openId0001
```

Output: 
```
{
    "Response": {
        "ReportUrl": "https://file.ess.tencent.cn/bresource/****",
        "RequestId": "s166141****028448367"
    }
}
```

