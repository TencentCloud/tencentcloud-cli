**Example 1: 查询续购配置**

指定产品和包分组，查询当前用户的续购配置

Input: 

```
tccli billing DescribeMeasureResourceAutoPurchaseConfig --cli-unfold-argument  \
    --ProductCode p_clb \
    --GroupIdList p_clb_lcu_domestic p_clb_lcu_international
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AutoRePurchaseFlag": 1,
                "GroupId": "p_clb_lcu_domestic",
                "ProductCode": "p_clb",
                "RemainThreshold": "0",
                "ResourceId": "clblcu-jfm000fwAPUz1np"
            }
        ],
        "RequestId": "b35a6eb0-f3dd-4dad-9bf3-d2e42488eeac"
    }
}
```

