**Example 1: 导出公网资产**



Input: 

```
tccli csip CreatePublicAssetsExportJob --cli-unfold-argument  \
    --MemberId mem-0a**1*f****4*aee \
    --Limit 1 \
    --Offset 0 \
    --Order UpdateTime \
    --By Desc
```

Output: 
```
{
    "Response": {
        "JobId": "9559745b-12a1-406a-baab-1ae1a6eb1a0f",
        "RequestId": "1abdf1ea-e4e3-4fa0-9220-bb5e13e03543"
    }
}
```

