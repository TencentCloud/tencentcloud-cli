**Example 1: 资产标签列表**



Input: 

```
tccli csip DescribeAssetTags --cli-unfold-argument  \
    --MemberId mem-6wfo123 \
    --Limit 1 \
    --Offset 0 \
    --Order update_time \
    --By desc
```

Output: 
```
{
    "Response": {
        "AssetTags": [
            {
                "AppID": 0,
                "AssetCount": 0,
                "Color": "blue",
                "CreateTime": "2026-01-29T18:33:58+08:00",
                "Description": "生产环境",
                "ID": 8,
                "TagKey": "环境",
                "TagValue": "生产",
                "TaggingRule": "[{\"rules\": [{\"value\": \"test-\", \"attribute\": \"vpc_name\", \"condition\": \"starts_with\"}, {\"value\": \"cvm_instance\", \"attribute\": \"asset_type\", \"condition\": \"equals\"}]}]",
                "UpdateTime": "2026-02-02T16:58:09+08:00"
            }
        ],
        "AutoTaggingEnabledList": [
            {
                "Text": "开启",
                "Value": "1"
            }
        ],
        "TotalCount": 12,
        "RequestId": "8cb96a97-d8fd-4874-87f0-615c66a9803f"
    }
}
```

