**Example 1: 漏洞管理 - 一键检测**

漏洞管理 - 一键检测

Input: 

```
tccli cwp ScanAsset --cli-unfold-argument  \
    --AssetTypeIds 1 \
    --Quuids xx
```

Output: 
```
{
    "Response": {
        "RequestId": "4234234",
        "TaskId": 1
    }
}
```

