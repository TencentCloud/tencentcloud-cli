**Example 1: 修改 DB Custom 置放群组的标签**



Input: 

```
tccli dbdc ModifyDBCustomDisasterRecoverGroupTags --cli-unfold-argument  \
    --DisasterRecoverGroupId dbps-xjelypsq \
    --AddTags.0.Key 部门 \
    --AddTags.0.Value 数据库 \
    --DeleteTagKeys DBCustom_置放群组
```

Output: 
```
{
    "Response": {
        "RequestId": "577aae7d-f0f8-48fa-83a1-d93efd1e1a5c"
    }
}
```

