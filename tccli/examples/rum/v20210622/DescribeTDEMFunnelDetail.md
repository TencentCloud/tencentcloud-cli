**Example 1: 示例**



Input: 

```
tccli rum DescribeTDEMFunnelDetail --cli-unfold-argument  \
    --AppId 1****7 \
    --FunnelId 11ca34ce-2747-41b4-b52d-e18310e45d43
```

Output: 
```
{
    "Response": {
        "Result": "{\"CreatedBy\":\"\",\"Description\":\"\",\"FunnelId\":\"11ca34ce-2747-41b4-b52d-e18310e45d43\",\"FunnelName\":\"进入购物车\",\"Source\":\"manual\",\"Status\":\"active\",\"StepCount\":3,\"Steps\":[{\"ActionType\":\"\",\"PageMatchMode\":\"exact\",\"PagePattern\":\"商城首页\",\"Selector\":\"\",\"StepName\":\"进入首页\",\"VisualName\":\"\"},{\"ActionType\":\"\",\"PageMatchMode\":\"exact\",\"PagePattern\":\"商品列表页\",\"Selector\":\"\",\"StepName\":\"进入列表页\",\"VisualName\":\"\"},{\"ActionType\":\"\",\"PageMatchMode\":\"exact\",\"PagePattern\":\"购物车页\",\"Selector\":\"\",\"StepName\":\"进入购物车\",\"VisualName\":\"\"}],\"UpdatedAt\":\"2026-05-12 07:12:03\"}",
        "RequestId": "c3ede0ff-9a91-4312-ac09-b2d8f7c597c7"
    }
}
```

