**Example 1: 创建健康报告浏览地址**



Input: 

```
tccli dbbrain CreateDBDiagReportUrl --cli-unfold-argument  \
    --Product mysql \
    --InstanceId cdb-c1nl9rpv \
    --AsyncRequestId 63452
```

Output: 
```
{
    "Response": {
        "ReportUrl": "https://dbbrain-sh-1256569818.cos.ap-guangzhou.myqcloud.com/report_cdb-c1nl9rpv_10947711_1618851196690.pdf?sign=q-sign-algorithm",
        "ExpireTime": 1618890295,
        "RequestId": "24665720-8c93-11eb-bee6-e98cea0e6794"
    }
}
```

