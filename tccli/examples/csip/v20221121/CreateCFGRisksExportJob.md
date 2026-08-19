**Example 1: 创建云资源配置检测报告导出任务**



Input: 

```
tccli csip CreateCFGRisksExportJob --cli-unfold-argument  \
    --MemberId mem-68*8**7*65*6*00* \
    --Limit 1 \
    --Offset 0 \
    --Order UpdateTime \
    --By DESC \
    --StandardIDs 3
```

Output: 
```
{
    "Response": {
        "JobId": "89d61637-9917-4e19-b000-58c2a8e1b358",
        "RequestId": "59277b4f-3473-4b3d-b4ca-283a53448e61"
    }
}
```

