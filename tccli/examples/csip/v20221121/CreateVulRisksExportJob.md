**Example 1: 创建漏洞风险导出任务**



Input: 

```
tccli csip CreateVulRisksExportJob --cli-unfold-argument  \
    --CloudAccountID 100010427547 \
    --Provider tencent
```

Output: 
```
{
    "Response": {
        "JobId": "73114db8-dce5-49e8-a13a-820b2b775014",
        "RequestId": "c826cdab-48c2-40c6-be27-f503dd92c141"
    }
}
```

