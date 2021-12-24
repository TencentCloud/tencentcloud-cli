**Example 1: 获取组件市场组件列表**



Input: 

```
tccli iecp GetMarketComponentList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --Filter test \
    --Order DESC
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "ComponentList": [
            {
                "Outline": "xx",
                "Author": "xx",
                "AppName": "xx",
                "Detail": "xx",
                "ReleaseTime": "xx"
            }
        ],
        "TotalCount": 10
    }
}
```

