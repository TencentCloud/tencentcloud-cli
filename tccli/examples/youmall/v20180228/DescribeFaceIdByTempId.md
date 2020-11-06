**Example 1: 根据临时ip获取face id**



Input: 

```
tccli youmall DescribeFaceIdByTempId --cli-unfold-argument  \
    --CompanyId tencent \
    --ShopId 10086 \
    --TempId tencent_10086_21_20180722080857_2677813760953992720_306_271_39_39 \
    --CameraId 21 \
    --PosId test
```

Output: 
```
{
    "Response": {
        "RequestId": "4060c99c-47e7-4706-ab51-a00f91baac39",
        "CompanyId": "tencent",
        "ShopId": 10086,
        "CameraId": 21,
        "PosId": "test",
        "TempId": "tencent_10086_21_20180722080857_2677813760953992720_306_271_39_39",
        "FaceId": 120,
        "PersonInfo": {
            "Age": 20,
            "Gender": 0,
            "PersonId": 1,
            "PersonType": 1,
            "PersonSubType": 1,
            "PersonPictureUrl": "xxxx"
        }
    }
}
```

