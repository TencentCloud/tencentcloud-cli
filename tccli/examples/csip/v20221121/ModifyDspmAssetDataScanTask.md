**Example 1: 修改Dspm资产数据扫描任务**



Input: 

```
tccli csip ModifyDspmAssetDataScanTask --cli-unfold-argument  \
    --AssetIds cdb-8pwcu099 \
    --IsScheduled False \
    --IsAgreeAuth True \
    --IsRunAtOnce True
```

Output: 
```
{
    "Response": {
        "RequestId": "cf839eee-b651-4ff3-9b49-173f9f55733f",
        "TaskIdSet": [
            1
        ]
    }
}
```

