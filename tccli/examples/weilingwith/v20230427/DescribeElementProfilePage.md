**Example 1: 查询分页构件信息**

查询分页构件信息成功响应示例

Input: 

```
tccli weilingwith DescribeElementProfilePage --cli-unfold-argument  \
    --BuildingId 956bd069-c802-4bbb-b325-18d30d7bcd3c \
    --PageNumber 1 \
    --PageSize 10 \
    --EntityTypes TBIM_SPACE TBIM_BUILDINGSTOREY \
    --WorkspaceId 1016 \
    --ApplicationToken ZRCJHdnhqEUEqO1vyskCgWimPucHhREV
```

Output: 
```
{
    "Response": {
        "RequestId": "f21ec011-9dde-478f-acd4-6adecb8a1c32",
        "Result": {
            "List": [
                {
                    "BottomHeight": -100,
                    "BuildingId": "956bd069-c802-4bbb-b325-18d30d7bcd3c",
                    "ElementDesc": "",
                    "ElementId": "1Kjh8u2qf4uRSkCPoKigTI",
                    "ElementName": "1F（结） -0.100",
                    "EntityType": "TBIM_BUILDINGSTOREY",
                    "IsDelete": 0,
                    "Level": 7,
                    "ParentElementId": "956bd069-c802-4bbb-b325-18d30d7bcd3c",
                    "Sort": 1,
                    "SpaceCode": "000185004",
                    "SpacePoiId": "",
                    "SpaceTypeCode": "",
                    "SpaceTypeName": ""
                },
                {
                    "BottomHeight": 0,
                    "BuildingId": "956bd069-c802-4bbb-b325-18d30d7bcd3c",
                    "ElementDesc": "",
                    "ElementId": "3Mph_S_ef13f4LIAEQPvzw",
                    "ElementName": "1",
                    "EntityType": "TBIM_SPACE",
                    "IsDelete": 0,
                    "Level": 8,
                    "ParentElementId": "1Kjh8u2qf4uRSkCPoKj36O",
                    "Sort": 2,
                    "SpaceCode": "00018500100000001",
                    "SpacePoiId": "",
                    "SpaceTypeCode": "",
                    "SpaceTypeName": ""
                },
                {
                    "BottomHeight": 0,
                    "BuildingId": "956bd069-c802-4bbb-b325-18d30d7bcd3c",
                    "ElementDesc": "",
                    "ElementId": "1Kjh8u2qf4uRSkCPoKj36O",
                    "ElementName": "1F 0.000",
                    "EntityType": "TBIM_BUILDINGSTOREY",
                    "IsDelete": 0,
                    "Level": 7,
                    "ParentElementId": "956bd069-c802-4bbb-b325-18d30d7bcd3c",
                    "Sort": 3,
                    "SpaceCode": "000185001",
                    "SpacePoiId": "",
                    "SpaceTypeCode": "",
                    "SpaceTypeName": ""
                },
                {
                    "BottomHeight": 5900,
                    "BuildingId": "956bd069-c802-4bbb-b325-18d30d7bcd3c",
                    "ElementDesc": "",
                    "ElementId": "1Kjh8u2qf4uRSkCPoKiWWT",
                    "ElementName": "2F（结）5.900",
                    "EntityType": "TBIM_BUILDINGSTOREY",
                    "IsDelete": 0,
                    "Level": 7,
                    "ParentElementId": "956bd069-c802-4bbb-b325-18d30d7bcd3c",
                    "Sort": 4,
                    "SpaceCode": "000185007",
                    "SpacePoiId": "",
                    "SpaceTypeCode": "",
                    "SpaceTypeName": ""
                },
                {
                    "BottomHeight": 6000,
                    "BuildingId": "956bd069-c802-4bbb-b325-18d30d7bcd3c",
                    "ElementDesc": "",
                    "ElementId": "1Kjh8u2qf4uRSkCPoKj38P",
                    "ElementName": "2F 6.000",
                    "EntityType": "TBIM_BUILDINGSTOREY",
                    "IsDelete": 0,
                    "Level": 7,
                    "ParentElementId": "956bd069-c802-4bbb-b325-18d30d7bcd3c",
                    "Sort": 5,
                    "SpaceCode": "000185002",
                    "SpacePoiId": "",
                    "SpaceTypeCode": "",
                    "SpaceTypeName": ""
                },
                {
                    "BottomHeight": 11000,
                    "BuildingId": "956bd069-c802-4bbb-b325-18d30d7bcd3c",
                    "ElementDesc": "",
                    "ElementId": "1Kjh8u2qf4uRSkCPoKlbkh",
                    "ElementName": "3F(结）",
                    "EntityType": "TBIM_BUILDINGSTOREY",
                    "IsDelete": 0,
                    "Level": 7,
                    "ParentElementId": "956bd069-c802-4bbb-b325-18d30d7bcd3c",
                    "Sort": 6,
                    "SpaceCode": "000185003",
                    "SpacePoiId": "",
                    "SpaceTypeCode": "",
                    "SpaceTypeName": ""
                },
                {
                    "BottomHeight": 11100,
                    "BuildingId": "956bd069-c802-4bbb-b325-18d30d7bcd3c",
                    "ElementDesc": "",
                    "ElementId": "1Kjh8u2qf4uRSkCPoKiVXm",
                    "ElementName": "F3",
                    "EntityType": "TBIM_BUILDINGSTOREY",
                    "IsDelete": 0,
                    "Level": 7,
                    "ParentElementId": "956bd069-c802-4bbb-b325-18d30d7bcd3c",
                    "Sort": 7,
                    "SpaceCode": "000185005",
                    "SpacePoiId": "",
                    "SpaceTypeCode": "",
                    "SpaceTypeName": ""
                },
                {
                    "BottomHeight": 16200,
                    "BuildingId": "956bd069-c802-4bbb-b325-18d30d7bcd3c",
                    "ElementDesc": "",
                    "ElementId": "1Kjh8u2qf4uRSkCPoKiVdy",
                    "ElementName": "F4",
                    "EntityType": "TBIM_BUILDINGSTOREY",
                    "IsDelete": 0,
                    "Level": 7,
                    "ParentElementId": "956bd069-c802-4bbb-b325-18d30d7bcd3c",
                    "Sort": 8,
                    "SpaceCode": "000185006",
                    "SpacePoiId": "",
                    "SpaceTypeCode": "",
                    "SpaceTypeName": ""
                }
            ],
            "TotalCount": 8
        }
    }
}
```

**Example 2: 查询分页构件信息示例-prod**

查询分页构件信息示例-prod

Input: 

```
tccli weilingwith DescribeElementProfilePage --cli-unfold-argument  \
    --BuildingId 9e98dc3920df4230b431404222fefe37 \
    --PageNumber 1 \
    --PageSize 5 \
    --WorkspaceId 1124 \
    --ApplicationToken Sl5ZDmVuHzhN52o8n1KWagl7sLdrLfN7
```

Output: 
```
{
    "Response": {
        "RequestId": "aa86cd58-027d-46b4-8d59-a7e15c733f18",
        "Result": {
            "List": [
                {
                    "BottomHeight": 0,
                    "BuildingId": "9e98dc3920df4230b431404222fefe37",
                    "ElementDesc": "",
                    "ElementId": "9e98dc3920df4230b431404222fefe37",
                    "ElementName": "rvm",
                    "EntityType": "TBIM_BUILDING",
                    "IsDelete": 0,
                    "Level": 6,
                    "ParentElementId": "",
                    "Sort": 1,
                    "SpaceCode": "000147",
                    "SpacePoiId": "86162",
                    "SpaceTypeCode": "",
                    "SpaceTypeName": ""
                },
                {
                    "BottomHeight": 0,
                    "BuildingId": "9e98dc3920df4230b431404222fefe37",
                    "ElementDesc": "/SAMPLE-ADMIN built by rvm",
                    "ElementId": "4cf3865c355048d0be117466b89ff5ae",
                    "ElementName": "/SAMPLE-ADMIN",
                    "EntityType": "TBIM_BUILDINGSTOREY",
                    "IsDelete": 0,
                    "Level": 0,
                    "ParentElementId": "9e98dc3920df4230b431404222fefe37",
                    "Sort": 2,
                    "SpaceCode": "",
                    "SpacePoiId": "861620006",
                    "SpaceTypeCode": "",
                    "SpaceTypeName": ""
                },
                {
                    "BottomHeight": 0,
                    "BuildingId": "9e98dc3920df4230b431404222fefe37",
                    "ElementDesc": "/HS-ADMIN/ADMIN built by rvm",
                    "ElementId": "f5dfeea83847436a98dd02957b283d0d",
                    "ElementName": "/HS-ADMIN/ADMIN",
                    "EntityType": "TBIM_BUILDINGELEMENTPROXY",
                    "IsDelete": 0,
                    "Level": 0,
                    "ParentElementId": "4cf3865c355048d0be117466b89ff5ae",
                    "Sort": 3,
                    "SpaceCode": "",
                    "SpacePoiId": "8616200060004",
                    "SpaceTypeCode": "",
                    "SpaceTypeName": ""
                },
                {
                    "BottomHeight": 0,
                    "BuildingId": "9e98dc3920df4230b431404222fefe37",
                    "ElementDesc": "/GRID-STABILIZER/1 built by rvm",
                    "ElementId": "b3f9777344214077a65d3673b17578bc",
                    "ElementName": "/GRID-STABILIZER/1",
                    "EntityType": "TBIM_BUILDINGELEMENTPROXY",
                    "IsDelete": 0,
                    "Level": 0,
                    "ParentElementId": "6ab5d7d6f6264824a1318435a0a09b4c",
                    "Sort": 4,
                    "SpaceCode": "",
                    "SpacePoiId": "",
                    "SpaceTypeCode": "",
                    "SpaceTypeName": ""
                },
                {
                    "BottomHeight": 0,
                    "BuildingId": "9e98dc3920df4230b431404222fefe37",
                    "ElementDesc": "CYLINDER 2 of EQUIPMENT /P1502B built by rvm",
                    "ElementId": "fc1a114cf16d4f999f4825294a6b378f",
                    "ElementName": "CYLINDER 2 of EQUIPMENT /P1502B",
                    "EntityType": "TBIM_BUILDINGELEMENTPROXY",
                    "IsDelete": 0,
                    "Level": 0,
                    "ParentElementId": "2fa2c48f06ee40a5a8a24f296925e532",
                    "Sort": 5,
                    "SpaceCode": "",
                    "SpacePoiId": "",
                    "SpaceTypeCode": "",
                    "SpaceTypeName": ""
                }
            ],
            "TotalCount": 2501
        }
    }
}
```

