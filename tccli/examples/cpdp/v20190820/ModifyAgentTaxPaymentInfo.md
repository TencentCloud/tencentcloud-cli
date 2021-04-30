**Example 1: ModifyAgentTaxPaymentInfo**



Input: 

```
tccli cpdp ModifyAgentTaxPaymentInfo --cli-unfold-argument  \
    --BatchNum 98 \
    --RawElectronicCertUrl https://cloud.tencent.com/document/product/1122/40639
```

Output: 
```
{
    "Response": {
        "RequestId": "c8ee3913-aa2a-4ea0-840f-9a77247bcabb",
        "AgentTaxPaymentBatch": {
            "StatusMsg": "下载&上传成功",
            "Type": 0,
            "BatchNum": 98,
            "InfoNum": 1,
            "Channel": 1,
            "FileName": "paxos.pdf",
            "RawElectronicCertUrl": "https://cloud.tencent.com/document/product/1122/40639",
            "AgentId": "test",
            "StatusCode": 0
        }
    }
}
```

