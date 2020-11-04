**Example 1: 用于获取服务器舰队列表**

用于获取服务器舰队列表

Input: 

```
tccli gse ListFleets --cli-unfold-argument  \
    --AssetId asset-eugdyx0g
```

Output: 
```
{
    "Response": {
        "FleetIds": [
            "fleet-qp3g3chf-jwoblkv3"
        ],
        "RequestId": "s1582187331291590006",
        "TotalCount": 1
    }
}
```

