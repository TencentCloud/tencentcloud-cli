**Example 1: 编辑策略**

编辑策略

Input: 

```
tccli csip BatchModifyBaselinePolicy --cli-unfold-argument  \
    --PolicyIDList 2 \
    --CycleScanConf.Enable 1 \
    --CycleScanConf.IntervalType DAY \
    --CycleScanConf.IntervalValueList 3 \
    --CycleScanConf.ScanStart 00:00 \
    --CycleScanConf.ScanEnd 00:20 \
    --CategoryConf.0.CategoryID 8 \
    --CategoryConf.0.AllSelect True \
    --CategoryConf.0.SubCategoryConfList.0.CategoryID 161 \
    --CategoryConf.0.SubCategoryConfList.0.AllSelect True \
    --CategoryConf.0.SubCategoryConfList.0.ItemIDList 12838 \
    --AutoSyncItem True \
    --MemberId mem-***********795752f66e429 \
    --CustomItemConf.0.RuleID 12837 \
    --CustomItemConf.0.CustomValueList 90 \
    --CustomItemConf.0.CustomItemID 2
```

Output: 
```
{
    "Response": {
        "RequestId": "4782df10-ce57-447d-a037-d53e231a7b85"
    }
}
```

