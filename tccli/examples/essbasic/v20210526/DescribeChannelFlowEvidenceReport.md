**Example 1: 创建并返回出证报告**

获取全部签署完成的合同的出证报告，返回报告 URL

Input: 

```
tccli essbasic DescribeChannelFlowEvidenceReport --cli-unfold-argument  \
    --ReportId yDR0PUUhw8ahh****KyK18G1h3FK5ccC \
    --Agent.ProxyOrganizationOpenId test1_claxxxanization1 \
    --Agent.AppId 7f349*********984a9657b0ec \
    --Agent.ProxyOperator.OpenId channel-super-*****-openId0001
```

Output: 
```
{
    "Response": {
        "ReportUrl": "",
        "Status": "EvidenceStatusSuccess",
        "RequestId": "s166141****028448367"
    }
}
```

