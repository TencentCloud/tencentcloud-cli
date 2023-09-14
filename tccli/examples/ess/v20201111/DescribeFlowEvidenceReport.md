**Example 1: 查询正在处理中的签署报告**

查询正在处理中的签署报告，正在处理中

Input: 

```
tccli ess DescribeFlowEvidenceReport --cli-unfold-argument  \
    --ReportId yDR0PUUhw8ahh****KyK18G1h3FK5ccC \
    --Operator.UserId de71c67592974c****20572d44ec0b6d
```

Output: 
```
{
    "Response": {
        "ReportUrl": "",
        "RequestId": "3129718393196",
        "Status": "EvidenceStatusExecuting"
    }
}
```

**Example 2: 查询签署报告**

查询签署报告，返回报告 URL

Input: 

```
tccli ess DescribeFlowEvidenceReport --cli-unfold-argument  \
    --ReportId yDR0PUUhw8ahh****KyK18G1h3FK5ccC \
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

