**Example 1: 查询出证报告**

查询出证报告，返回报告 URL

Input: 

```
tccli ess DescribeFlowEvidenceReport --cli-unfold-argument  \
    --ReportId yDR0PUUhw8ahh****KyK18G1h3FK5ccC \
    --Operator.OpenId  \
    --Operator.ClientIp 113.***.**.65 \
    --Operator.ProxyIp  \
    --Operator.Channel  \
    --Operator.UserId de71c67592974c****20572d44ec0b6d
```

Output: 
```
{
    "Response": {
        "ReportUrl": "",
        "RequestId": "s16679771xxxx693616",
        "Status": "EvidenceStatusSuccess"
    }
}
```

