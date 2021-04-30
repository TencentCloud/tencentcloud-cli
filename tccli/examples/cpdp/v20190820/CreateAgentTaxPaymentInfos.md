**Example 1: CreateAgentTaxPaymentInfos**



Input: 

```
tccli cpdp CreateAgentTaxPaymentInfos --cli-unfold-argument  \
    --AgentId test \
    --Channel 1 \
    --Type 0 \
    --RawElectronicCertUrl https://cloud.tencent.com/document/product/1122/40638 \
    --FileName paxos.pdf \
    --AgentTaxPaymentInfos.0.AnchorId 1234567890 \
    --AgentTaxPaymentInfos.0.AnchorName 张三 \
    --AgentTaxPaymentInfos.0.AnchorIDCard 1234567890 \
    --AgentTaxPaymentInfos.0.StartTime 2020-01-01 \
    --AgentTaxPaymentInfos.0.EndTime 2020-01-01 \
    --AgentTaxPaymentInfos.0.Amount 10000 \
    --AgentTaxPaymentInfos.0.Tax 600
```

Output: 
```
{
    "Response": {
        "RequestId": "0888a907-aad3-4b53-ad10-b07117d1816d",
        "AgentTaxPaymentBatch": {
            "StatusMsg": "下载&上传成功",
            "Type": 0,
            "BatchNum": 98,
            "InfoNum": 1,
            "Channel": 1,
            "FileName": "paxos.pdf",
            "RawElectronicCertUrl": "https://cloud.tencent.com/document/product/1122/40638",
            "AgentId": "test",
            "StatusCode": 0
        }
    }
}
```

