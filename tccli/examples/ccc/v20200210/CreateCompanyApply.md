**Example 1: 创建公司资质申请示例**



Input: 

```
tccli ccc CreateCompanyApply --cli-unfold-argument  \
    --CompanyInfo.ApplicantType 1 \
    --CompanyInfo.CompanyName 北京XXXXX有限责任公司 \
    --CompanyInfo.BusinessId 977111111111111 \
    --CompanyInfo.BusinessIdPicUrl https://xxxx.com/xxxxx.jpg \
    --CompanyInfo.IsEqualTencentCloud 1 \
    --CompanyInfo.CorporationName 王某某 \
    --CompanyInfo.CorporationId 6108888888888888 \
    --CompanyInfo.CorporationIdPicUrl https://xxxx.com/xxxxx.jpg \
    --CompanyInfo.NetworkCommitmentPicUrl https://xxxx.com/xxxxx.jpg \
    --CompanyInfo.CorporationHoldingOnIdPicUrl https://xxxx.com/xxxxx.jpg \
    --CompanyInfo.CorporationMobile 18092688910 \
    --CompanyInfo.CorporationMobilePicUrl https://www.example.com/corporation_mobile_pic.gif \
    --CompanyInfo.OperatorName 李某某 \
    --CompanyInfo.OperatorId 610000000000000 \
    --CompanyInfo.OperatorIdPicUrl https://xxxx.com/xxxxx.jpg \
    --CompanyInfo.OperatorHoldingOnIdPicUrl https://xxxx.com/xxxxx.jpg \
    --CompanyInfo.OperatorMobile 18192226857 \
    --CompanyInfo.OperatorEmail 222@qq.com \
    --CompanyInfo.OperatorMobilePicUrl https://xxxx.com/xxxxx.jpg \
    --CompanyInfo.CommissionPicUrl https://www.example.com/commission_pic.JPG \
    --CompanyInfo.CompanyAuthLetterPicUrl https://www.example.com/company_auth_pic.JPG \
    --CompanyInfo.UseDescribeFileUrl https://www.example.com/use_describe_file.doc \
    --CompanyInfo.AcceptPicUrl https://xxxxxxxxx.com/file.jpg
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

