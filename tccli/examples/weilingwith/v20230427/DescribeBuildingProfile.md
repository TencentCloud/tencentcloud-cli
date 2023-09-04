**Example 1: 查询建筑信息**

查询建筑信息成功响应

Input: 

```
tccli weilingwith DescribeBuildingProfile --cli-unfold-argument  \
    --BuildingId 2e374df6-7ba7-45d2-a44d-2a92bb2a6668 \
    --WorkspaceId 1016 \
    --ApplicationToken 0VGYLwQaH4ejNnwSMIfYtl0zlstprsdZ
```

Output: 
```
{
    "Response": {
        "RequestId": "9d3442d1-0df1-48ef-beba-872e07b2b1dd",
        "Result": {
            "BuildingProfile": {
                "Address": "广东省,深圳市,南山区测试建筑",
                "BuildingId": "2e374df6-7ba7-45d2-a44d-2a92bb2a6668",
                "BuildingName": "测试建筑",
                "Latitude": 22.533192,
                "Longitude": 113.93048,
                "SpaceCode": "000003"
            }
        }
    }
}
```

**Example 2: 查询建筑信息示例-prod**

查询建筑信息示例-prod

Input: 

```
tccli weilingwith DescribeBuildingProfile --cli-unfold-argument  \
    --BuildingId 9e98dc3920df4230b431404222fefe37 \
    --WorkspaceId 1124 \
    --ApplicationToken Sl5ZDmVuHzhN52o8n1KWagl7sLdrLfN7
```

Output: 
```
{
    "Response": {
        "RequestId": "966d76de-83dc-4d6a-bd17-75505fe0af7e",
        "Result": {
            "BuildingProfile": {
                "Address": "陕西省,西安市,碑林区rvm",
                "BuildingId": "9e98dc3920df4230b431404222fefe37",
                "BuildingName": "rvm",
                "Latitude": 34.212498,
                "Longitude": 108.88995,
                "SpaceCode": "000147"
            }
        }
    }
}
```

