**Example 1: 查询活动列表**



Input: 

```
tccli wav QueryActivityJoinList --cli-unfold-argument  \
    --Limit 1 \
    --ActivityId 1394233693086657654
```

Output: 
```
{
    "Response": {
        "NextCursor": "E9y1rxkoUxUW4i+Yx7ThkT7p0+bJm6IXDaCfF4etiyI=",
        "PageData": [
            {
                "ActivityData": "{\"cityInfo\":{\"cityCode\":\"420100\",\"cityName\":\"武汉市\",\"provinceCode\":\"420000\",\"provinceName\":\"湖北省\"},\"carInfo\":{\"carId\":\"1334701452344614913\",\"carName\":\"A车型\",\"brandId\":1334701452336226306,\"tenantSeriesId\":1334701452340420610,\"baseBrandName\":\"大迪\",\"tenantSeriesName\":\"测试素材查看-车型\"},\"shopInfo\":{\"shopId\":1392034008271540226,\"shopName\":\"武汉惠通陆华汽车服务有限公司\",\"cityCode\":\"420100\"}}",
                "SalesName": "hc",
                "UserName": "lxc",
                "ActivityName": "测试未开始活动",
                "SalesPhone": "18976547654",
                "ActivityId": 1394233693086657654,
                "CreateTime": 1624242265,
                "LiveCodeId": 0,
                "JoinId": 1406800137191108987,
                "JoinState": 1,
                "DuplicateLeadId": 0,
                "UserPhone": "18045676789",
                "UpdateTime": 1624242265,
                "Duplicate": 0,
                "JoinTime": 1624242264,
                "LeadId": 1406800137394126823
            }
        ],
        "RequestId": "cee4598b-9eea-4e87-8544-7f584beb6235"
    }
}
```

