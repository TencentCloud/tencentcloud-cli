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
        "ReportUrl": "https://file.ess.tencent.cn/file/yDwhIU*****kvSEnAV3Qyl2B/0/1.PDF?hkey=58cce665fd939d77e5895e16e05e893c***ccff7e5f2c81027b190f9ef3bf4e7cb06f02a5b6fea82b7b211d1f85204b11bd66fb28ab960b2b966215ec624b11c422291f68554b8e0f",
        "RequestId": "s16679771xxxx693616",
        "Status": "EvidenceStatusSuccess"
    }
}
```

