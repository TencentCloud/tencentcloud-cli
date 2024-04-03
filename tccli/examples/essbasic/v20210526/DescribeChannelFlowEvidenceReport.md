**Example 1: 查询签署报告**

获取全部签署完成的合同的出证报告，返回报告 URL

Input: 

```
tccli essbasic DescribeChannelFlowEvidenceReport --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --ReportId yDSLVUUckpo3nva8UEnf33kvzHQ19GcL \
    --ReportType 0
```

Output: 
```
{
    "Response": {
        "ReportUrl": "https://file.test.ess.tencent.cn/bresource/resource/resource/0/0.PDF?hkey=5c123fea2686b****6283",
        "Status": "EvidenceStatusSuccess",
        "RequestId": "d9040af5-eda9-47cf-b37c-b0c5b34a6319"
    }
}
```

**Example 2: 查询公证处核验报告**

获取全部签署完成的合同的公证处核验报告，返回报告 URL

Input: 

```
tccli essbasic DescribeChannelFlowEvidenceReport --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --ReportId yDSLVUUckpo3nva8UEnf33kvzHQ19GcL \
    --ReportType 1
```

Output: 
```
{
    "Response": {
        "ReportUrl": "https://file.test.ess.tencent.cn/bresource/resource/resource/0/0.PDF?hkey=5c123fea2686b****6283",
        "Status": "EvidenceStatusSuccess",
        "RequestId": "d9040af5-eda9-47cf-b37c-b0c5b34a6319"
    }
}
```

