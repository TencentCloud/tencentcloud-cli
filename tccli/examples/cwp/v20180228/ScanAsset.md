**Example 1: 资产指纹扫描**

启动资产指纹扫描

Input: 

```
tccli cwp ScanAsset --cli-unfold-argument  \
    --AssetTypeIds 1 \
    --Quuids 6cf3c132-aaa-bbbb-b08d-98be9421372a
```

Output: 
```
{
    "Response": {
        "RequestId": "8564b09e-0e04-4516-bb59-db09742503c2",
        "TaskId": 1
    }
}
```

