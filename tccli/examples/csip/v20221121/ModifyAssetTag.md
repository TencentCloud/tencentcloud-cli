**Example 1: 标签管理编辑标签**



Input: 

```
tccli csip ModifyAssetTag --cli-unfold-argument  \
    --Key 业务q \
    --Value 业务q \
    --TagID 95 \
    --MemberId mem-6wfo123 \
    --Color blue \
    --Description 测试标签 \
    --TaggingRule [{"rules":[{"value":["tencent-lighthouse_instance"],"attribute":"asset_type","condition":"equals"}],"enabled":1}]
```

Output: 
```
{
    "Response": {
        "Code": "0",
        "Message": "Asset tag updated successfully",
        "RequestId": "20b5dc29-f5e2-4bbb-afa9-ab024124dbb4"
    }
}
```

