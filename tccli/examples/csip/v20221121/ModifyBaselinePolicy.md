**Example 1: 调用示例**



Input: 

```
tccli csip ModifyBaselinePolicy --cli-unfold-argument  \
    --Policy.CycleScanConf.Enable 1 \
    --Policy.CycleScanConf.IntervalType DAY \
    --Policy.CycleScanConf.IntervalValueList 1 \
    --Policy.CycleScanConf.ScanStart 03:00 \
    --Policy.CycleScanConf.ScanEnd 04:00 \
    --Policy.CheckAssetType HOST \
    --Policy.AutoSyncItem False \
    --Policy.Type SELF \
    --Policy.Name 测试策略 \
    --Policy.Description 测试策略 \
    --Policy.ConfHostType ALL \
    --Policy.ConfHostIncludeList ins-include \
    --Policy.ConfHostExcludeList ins-exclude \
    --Policy.Enable True \
    --Policy.ConfClusterType ALL \
    --Policy.ConfClusterIncludeList cls-include \
    --Policy.ConfClusterExcludeList cls-exclude \
    --Policy.CategoryConf.0.CategoryID 4 \
    --Policy.CategoryConf.0.AllSelect False \
    --Policy.CategoryConf.0.SubCategoryConfList.0.CategoryID 206 \
    --Policy.CategoryConf.0.SubCategoryConfList.0.AllSelect False \
    --Policy.CategoryConf.0.SubCategoryConfList.0.ItemIDList 5396 \
    --Policy.CustomItemConf.0.RuleID 120 \
    --Policy.CustomItemConf.0.CustomValueList custom_value \
    --Policy.CustomItemConf.0.CustomItemID 148 \
    --Policy.Appid 200000000 \
    --Policy.ID 450 \
    --Policy.ConfItemCount 0 \
    --Policy.ConfHostCount 0 \
    --Policy.ConfClusterCount 0 \
    --Policy.ScanningTaskID 0 \
    --Policy.LatestScanTime 1970-01-01T00:00:00Z \
    --Policy.LatestCycleScanTime 1970-01-01T00:00:00Z \
    --Policy.TagIDList 12 \
    --Policy.CloudTagList core \
    --MemberId mem-tencent-6*************29
```

Output: 
```
{
    "Response": {
        "RequestId": "fb33355f-f4d4-4a09-81ba-da3c1acb0a6c"
    }
}
```

