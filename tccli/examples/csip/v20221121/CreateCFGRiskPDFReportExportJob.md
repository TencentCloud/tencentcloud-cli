**Example 1: 云资源配置风险PDF报告导出**



Input: 

```
tccli csip CreateCFGRiskPDFReportExportJob --cli-unfold-argument  \
    --StandardID 3 \
    --MemberId mem-xsdf001 \
    --Limit 1 \
    --Offset 0 \
    --Order Desc \
    --By UpdateTime
```

Output: 
```
{
    "Response": {
        "JobId": "edbcbaeb-8ed4-4999-a1e2-74a7f1a96274",
        "RequestId": "e6ac714b-1658-48b8-bc83-798c9d4bdbe7"
    }
}
```

