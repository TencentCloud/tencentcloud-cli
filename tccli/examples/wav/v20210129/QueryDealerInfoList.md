**Example 1: 查询经销商信息列表接口**



Input: 

```
tccli wav QueryDealerInfoList --cli-unfold-argument  \
    --Cursor sHmJbhJZhCwwMYmSot50dl2Hs9qQvbP+pCUVxlm/oLU \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "NextCursor": "sHmJbhJZhCwwMYmSot50dl2Hs9qQvbP+pCUVxlm/oLU=",
        "HasMore": 1,
        "PageData": [
            {
                "DealerId": 1348080105398452226,
                "DealerName": "经销商名称"
            }
        ],
        "RequestId": "b1a024bf-4d74-4b5d-a5bd-bbec330520e8"
    }
}
```

