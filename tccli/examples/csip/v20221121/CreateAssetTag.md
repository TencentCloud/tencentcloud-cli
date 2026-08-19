**Example 1: 标签管理创建资产标签**



Input: 

```
tccli csip CreateAssetTag --cli-unfold-argument  \
    --Key 业务q \
    --Value 测试标签 \
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
        "Message": "Asset tag created successfully",
        "RequestId": "17657036-4d99-4294-9dfa-24117fa82689"
    }
}
```

