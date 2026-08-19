**Example 1: 标签管理自动打标策略预览资产数据**



Input: 

```
tccli csip DescribeTagRuleAssets --cli-unfold-argument  \
    --MemberId mem-6wfo123 \
    --Limit 0 \
    --Offset 20 \
    --TaggingRule [{"rules":[{"value":["tencent-lighthouse_instance"],"attribute":"asset_type","condition":"equals"}],"enabled":1}]
```

Output: 
```
{
    "Response": {
        "AssetTypeList": [
            {
                "Text": "腾讯云-CAM 账号",
                "Value": "tencent-cam_user"
            }
        ],
        "Assets": [],
        "TotalCount": 9,
        "RequestId": "41a42083-983a-46f9-a204-e7a350449e7d"
    }
}
```

