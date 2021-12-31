**Example 1: 查询车系车型信息列表接口**



Input: 

```
tccli wav QueryVehicleInfoList --cli-unfold-argument  \
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
                "BrandId": 1348081115398452226,
                "BrandName": "品牌名称",
                "SeriesId": 1348080105398452333,
                "SeriesName": "车系名称",
                "ModelId": 1348084565398452121,
                "ModelName": "车型名称"
            }
        ],
        "RequestId": "b1a024bf-4d74-4b5d-a5bd-bbec330520e8"
    }
}
```

