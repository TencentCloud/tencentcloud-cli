**Example 1: 查询起草任务结果**



Input: 

```
tccli ess DescribeDraftContractByPromptsTask --cli-unfold-argument  \
    --Operator.UserId yDCZcUUpn********ZGci8dkgk03ZIow \
    --TaskId yD3a5UUs1b********Hu4sn4VpzPXtIy
```

Output: 
```
{
    "Response": {
        "ContractName": "软件开发服务合同",
        "Message": "需求校验未通过: 该需求意图为“**买卖合同”*******，属于严重违法犯罪行为，内容违法违规，无法用于生成任何合同。",
        "ResourceId": "yD3a5UUs1i****UEMs3KDC7ewKOitKTm",
        "Status": 2,
        "RequestId": "47c5c8a5-e32d-4ba1-bbd2-25cc41ea96f9",
        "ContractUrl": "https://file.test.ess.tencent.cn/bresource/resource/resource/0/0.DOCX?hkey=483e25687aa346406a47bb85ebd2a3c344ccd82e8f1bdcd0b*****c619366746dd65aa9b2877d**e**a1c73802075f7d71d2c8471**79c**c6ea5761c943d3181de0a**dd0bd**b4137abc57b33fe151d6*519399f0***570f12cfc97e07314*"
    }
}
```

