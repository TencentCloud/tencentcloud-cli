**Example 1: 查询经销商信息列表接口**

查询经销商信息列表

Input: 

```
tccli wav QueryDealerInfoList --cli-unfold-argument  \
    --Cursor sHmJbhJZhCwwMYmSot50dl2Hs9qQvbP+pCUVxlm/oLU= \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "NextCursor": "sHmJbhJZhCwwMYmSot50dl2Hs9qQvbP+pCUVxlm/oLU=",
        "HasMore": 1,
        "PageData": [
            {
                "DealerId": 1348080105398452200,
                "DealerName": "经销商名称",
                "ProvinceCode": "110100",
                "CityCodeList": [
                    "110100"
                ],
                "BrandIdList": [
                    "1"
                ]
            }
        ],
        "RequestId": "b1a024bf-4d74-4b5d-a5bd-bbec330520e8"
    }
}
```

