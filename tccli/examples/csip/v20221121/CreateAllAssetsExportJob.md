**Example 1: 导出全部资产**



Input: 

```
tccli csip CreateAllAssetsExportJob --cli-unfold-argument  \
    --MemberId mem-0acb10f*f**4da*e \
    --Limit 1 \
    --Offset 0 \
    --Order UpdateTime \
    --By Desc \
    --IsCloudHost True
```

Output: 
```
{
    "Response": {
        "JobId": "679f0712-8d72-4525-b6ff-e7b081815ee9",
        "RequestId": "dc9b60d6-d853-4e29-8058-22b67d8b8bd3"
    }
}
```

