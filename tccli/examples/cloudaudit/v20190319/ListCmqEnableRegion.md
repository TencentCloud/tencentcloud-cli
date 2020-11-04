**Example 1: 查询云审计支持的cmq的可用区**

查询云审计支持的cmq的可用区

Input: 

```
tccli cloudaudit ListCmqEnableRegion --cli-unfold-argument  \
    --WebsiteType zh
```

Output: 
```
{
    "Response": {
        "RequestId": "b69a7b60-e58f-4d27-a2b7-722fe01109c1",
        "EnableRegions": [
            {
                "CmqRegion": "sh",
                "CmqRegionName": "上海"
            },
            {
                "CmqRegion": "hk",
                "CmqRegionName": "香港"
            }
        ]
    }
}
```

