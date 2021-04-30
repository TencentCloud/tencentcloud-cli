**Example 1: QueryAgentTaxPaymentBatch**



Input: 

```
tccli cpdp QueryAgentTaxPaymentBatch --cli-unfold-argument  \
    --BatchNum 98
```

Output: 
```
{
    "Response": {
        "RequestId": "8aadd86c-1727-40ef-9927-9f87201449af",
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

