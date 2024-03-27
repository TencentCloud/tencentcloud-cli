**Example 1: 创建公司资质申请示例**



Input: 

```
tccli ccc CreateCompanyApply --cli-unfold-argument  \
    --CompanyInfo.ApplicantType 1 \
    --CompanyInfo.CompanyName 北京XXXXX有限责任公司 \
    --CompanyInfo.BusinessId 977111111111111 \
    --CompanyInfo.BusinessIdPicUrl https://xxxx.com/xxxxx.jpg \
    --CompanyInfo.CorporationName 王某某 \
    --CompanyInfo.CorporationId 6108888888888888 \
    --CompanyInfo.CorporationIdPicUrl https://xxxx.com/xxxxx.jpg \
    --CompanyInfo.BusinessScope 软件开发咨询 \
    --CompanyInfo.AcceptPicUrl https://xxxx.com/xxxxx.jpg \
    --CompanyInfo.NetworkCommitmentPicUrl https://xxxx.com/xxxxx.jpg \
    --CompanyInfo.CorporationHoldingOnIdPicUrl https://xxxx.com/xxxxx.jpg \
    --CompanyInfo.OperatorName 李某某 \
    --CompanyInfo.OperatorId 610000000000000 \
    --CompanyInfo.OperatorIdPicUrl https://xxxx.com/xxxxx.jpg \
    --CompanyInfo.OperatorHoldingOnIdPicUrl https://xxxx.com/xxxxx.jpg \
    --CompanyInfo.CommissionPicUrl https://xxxx.com/xxxxx.jpg
```

Output: 
```
{
    "Response": {
        "Id": 0,
        "RequestId": "abc"
    }
}
```

