**Example 1: 查询构件树**

查询构件树成功响应示例

Input: 

```
tccli weilingwith DescribeElementProfileTree --cli-unfold-argument  \
    --BuildingId 82d5fb5a-52d0-4636-a225-d46245e911ef \
    --ElementId 61049c1b-158d-41bd-9f0b-df30a50401bd \
    --WorkspaceId 1016 \
    --ApplicationToken 0VGYLwQaH4ejNnwSMIfYtl0zlstprsdZ
```

Output: 
```
{
    "Response": {
        "RequestId": "473e2070-39bf-4e12-836b-c821799c9cd9",
        "Result": {
            "BuildingId": "82d5fb5a-52d0-4636-a225-d46245e911ef",
            "ParentElementId": "61049c1b-158d-41bd-9f0b-df30a50401bd",
            "Root": {
                "Children": [
                    {
                        "Children": [],
                        "ElementProfile": {
                            "BottomHeight": 3000,
                            "BuildingId": "82d5fb5a-52d0-4636-a225-d46245e911ef",
                            "ElementDesc": "",
                            "ElementId": "6042d426-6973-47ff-8ce1-3a63ef9f3c2f",
                            "ElementName": "",
                            "EntityType": "TBIM_SLASHWALL",
                            "IsDelete": 0,
                            "Level": 8,
                            "ParentElementId": "61049c1b-158d-41bd-9f0b-df30a50401bd",
                            "Sort": 1,
                            "SpaceCode": "00003000300000001",
                            "SpacePoiId": "",
                            "SpaceTypeCode": "",
                            "SpaceTypeName": ""
                        }
                    },
                    {
                        "Children": [],
                        "ElementProfile": {
                            "BottomHeight": 3000,
                            "BuildingId": "82d5fb5a-52d0-4636-a225-d46245e911ef",
                            "ElementDesc": "",
                            "ElementId": "f408f4c7-6adc-42fd-9485-d3322d5caf77",
                            "ElementName": "",
                            "EntityType": "TBIM_SLASHWALL",
                            "IsDelete": 0,
                            "Level": 8,
                            "ParentElementId": "61049c1b-158d-41bd-9f0b-df30a50401bd",
                            "Sort": 2,
                            "SpaceCode": "00003000300000002",
                            "SpacePoiId": "",
                            "SpaceTypeCode": "",
                            "SpaceTypeName": ""
                        }
                    },
                    {
                        "Children": [
                            {
                                "Children": [
                                    {
                                        "Children": [],
                                        "ElementProfile": {
                                            "BottomHeight": 3000,
                                            "BuildingId": "82d5fb5a-52d0-4636-a225-d46245e911ef",
                                            "ElementDesc": "",
                                            "ElementId": "2fb8f038-d0d1-4c11-b290-30f4f7ccf5e0",
                                            "ElementName": "",
                                            "EntityType": "TBIM_DOOR",
                                            "IsDelete": 0,
                                            "Level": 0,
                                            "ParentElementId": "f95c3dcd-dfe4-4828-aab7-6cee05fe2578",
                                            "Sort": 1,
                                            "SpaceCode": "",
                                            "SpacePoiId": "",
                                            "SpaceTypeCode": "",
                                            "SpaceTypeName": ""
                                        }
                                    }
                                ],
                                "ElementProfile": {
                                    "BottomHeight": 3000,
                                    "BuildingId": "82d5fb5a-52d0-4636-a225-d46245e911ef",
                                    "ElementDesc": "",
                                    "ElementId": "f95c3dcd-dfe4-4828-aab7-6cee05fe2578",
                                    "ElementName": "",
                                    "EntityType": "TBIM_OPENINGELEMENT",
                                    "IsDelete": 0,
                                    "Level": 0,
                                    "ParentElementId": "b46107b5-95f4-4115-9f90-8c72173417d7",
                                    "Sort": 1,
                                    "SpaceCode": "",
                                    "SpacePoiId": "",
                                    "SpaceTypeCode": "",
                                    "SpaceTypeName": ""
                                }
                            }
                        ],
                        "ElementProfile": {
                            "BottomHeight": 3000,
                            "BuildingId": "82d5fb5a-52d0-4636-a225-d46245e911ef",
                            "ElementDesc": "",
                            "ElementId": "b46107b5-95f4-4115-9f90-8c72173417d7",
                            "ElementName": "",
                            "EntityType": "TBIM_SLASHWALL",
                            "IsDelete": 0,
                            "Level": 8,
                            "ParentElementId": "61049c1b-158d-41bd-9f0b-df30a50401bd",
                            "Sort": 3,
                            "SpaceCode": "00003000300000003",
                            "SpacePoiId": "",
                            "SpaceTypeCode": "",
                            "SpaceTypeName": ""
                        }
                    },
                    {
                        "Children": [],
                        "ElementProfile": {
                            "BottomHeight": 3000,
                            "BuildingId": "82d5fb5a-52d0-4636-a225-d46245e911ef",
                            "ElementDesc": "",
                            "ElementId": "96b96d40-0661-4c5f-a71f-ffd0c5d73791",
                            "ElementName": "",
                            "EntityType": "TBIM_SLASHWALL",
                            "IsDelete": 0,
                            "Level": 8,
                            "ParentElementId": "61049c1b-158d-41bd-9f0b-df30a50401bd",
                            "Sort": 4,
                            "SpaceCode": "00003000300000004",
                            "SpacePoiId": "",
                            "SpaceTypeCode": "",
                            "SpaceTypeName": ""
                        }
                    },
                    {
                        "Children": [],
                        "ElementProfile": {
                            "BottomHeight": 3000,
                            "BuildingId": "82d5fb5a-52d0-4636-a225-d46245e911ef",
                            "ElementDesc": "",
                            "ElementId": "b95c73d1-208a-4342-ac54-5627b2021627",
                            "ElementName": "",
                            "EntityType": "TBIM_COMMON_DEVICE",
                            "IsDelete": 0,
                            "Level": 9,
                            "ParentElementId": "61049c1b-158d-41bd-9f0b-df30a50401bd",
                            "Sort": 5,
                            "SpaceCode": "00003000300000005",
                            "SpacePoiId": "",
                            "SpaceTypeCode": "",
                            "SpaceTypeName": ""
                        }
                    },
                    {
                        "Children": [],
                        "ElementProfile": {
                            "BottomHeight": 3000,
                            "BuildingId": "82d5fb5a-52d0-4636-a225-d46245e911ef",
                            "ElementDesc": "",
                            "ElementId": "8ace642a-c45f-401a-890c-6570f08fd97a",
                            "ElementName": "",
                            "EntityType": "TBIM_COMMON_DEVICE",
                            "IsDelete": 0,
                            "Level": 9,
                            "ParentElementId": "61049c1b-158d-41bd-9f0b-df30a50401bd",
                            "Sort": 6,
                            "SpaceCode": "00003000300000006",
                            "SpacePoiId": "",
                            "SpaceTypeCode": "",
                            "SpaceTypeName": ""
                        }
                    },
                    {
                        "Children": [],
                        "ElementProfile": {
                            "BottomHeight": 3000,
                            "BuildingId": "82d5fb5a-52d0-4636-a225-d46245e911ef",
                            "ElementDesc": "",
                            "ElementId": "a1162f6d-e8c4-4bd2-af78-dbbdb2918b6d",
                            "ElementName": "",
                            "EntityType": "TBIM_COMMON_DEVICE",
                            "IsDelete": 0,
                            "Level": 9,
                            "ParentElementId": "61049c1b-158d-41bd-9f0b-df30a50401bd",
                            "Sort": 7,
                            "SpaceCode": "00003000300000007",
                            "SpacePoiId": "",
                            "SpaceTypeCode": "",
                            "SpaceTypeName": ""
                        }
                    },
                    {
                        "Children": [],
                        "ElementProfile": {
                            "BottomHeight": 3000,
                            "BuildingId": "82d5fb5a-52d0-4636-a225-d46245e911ef",
                            "ElementDesc": "",
                            "ElementId": "8a74aba0-46e3-4097-89e6-7adbeb9ccaef",
                            "ElementName": "",
                            "EntityType": "TBIM_CAMERA",
                            "IsDelete": 0,
                            "Level": 9,
                            "ParentElementId": "61049c1b-158d-41bd-9f0b-df30a50401bd",
                            "Sort": 8,
                            "SpaceCode": "00003000300000008",
                            "SpacePoiId": "",
                            "SpaceTypeCode": "",
                            "SpaceTypeName": ""
                        }
                    },
                    {
                        "Children": [],
                        "ElementProfile": {
                            "BottomHeight": 3000,
                            "BuildingId": "82d5fb5a-52d0-4636-a225-d46245e911ef",
                            "ElementDesc": "",
                            "ElementId": "af7f7d83-17f8-4dff-80e2-a5129a39eab0",
                            "ElementName": "",
                            "EntityType": "TBIM_CAMERA",
                            "IsDelete": 0,
                            "Level": 9,
                            "ParentElementId": "61049c1b-158d-41bd-9f0b-df30a50401bd",
                            "Sort": 9,
                            "SpaceCode": "00003000300000009",
                            "SpacePoiId": "",
                            "SpaceTypeCode": "",
                            "SpaceTypeName": ""
                        }
                    },
                    {
                        "Children": [],
                        "ElementProfile": {
                            "BottomHeight": 3000,
                            "BuildingId": "82d5fb5a-52d0-4636-a225-d46245e911ef",
                            "ElementDesc": "",
                            "ElementId": "f596e5e3-68fb-48e6-bd74-845d623e600f",
                            "ElementName": "",
                            "EntityType": "TBIM_CAMERA",
                            "IsDelete": 0,
                            "Level": 9,
                            "ParentElementId": "61049c1b-158d-41bd-9f0b-df30a50401bd",
                            "Sort": 10,
                            "SpaceCode": "00003000300000010",
                            "SpacePoiId": "",
                            "SpaceTypeCode": "",
                            "SpaceTypeName": ""
                        }
                    }
                ],
                "ElementProfile": {
                    "BottomHeight": 3000,
                    "BuildingId": "82d5fb5a-52d0-4636-a225-d46245e911ef",
                    "ElementDesc": "",
                    "ElementId": "61049c1b-158d-41bd-9f0b-df30a50401bd",
                    "ElementName": "RF",
                    "EntityType": "TBIM_BUILDINGSTOREY",
                    "IsDelete": 0,
                    "Level": 7,
                    "ParentElementId": "",
                    "Sort": 1,
                    "SpaceCode": "000030003",
                    "SpacePoiId": "",
                    "SpaceTypeCode": "",
                    "SpaceTypeName": ""
                }
            }
        }
    }
}
```

**Example 2: 查询构件树示例-prod**

查询构件树示例-prod

Input: 

```
tccli weilingwith DescribeElementProfileTree --cli-unfold-argument  \
    --BuildingId 377e4f9d-d20e-4209-b1e8-0ddb32e888c8 \
    --Level 7 \
    --WorkspaceId 1124 \
    --ApplicationToken Sl5ZDmVuHzhN52o8n1KWagl7sLdrLfN7
```

Output: 
```
{
    "Response": {
        "RequestId": "30078117-d5fa-41a2-b837-bb747aede417",
        "Result": {
            "BuildingId": "377e4f9d-d20e-4209-b1e8-0ddb32e888c8",
            "ParentElementId": "377e4f9d-d20e-4209-b1e8-0ddb32e888c8",
            "Root": {
                "Children": [
                    {
                        "Children": [],
                        "ElementProfile": {
                            "BottomHeight": 0,
                            "BuildingId": "377e4f9d-d20e-4209-b1e8-0ddb32e888c8",
                            "ElementDesc": "from Rvt",
                            "ElementId": "f96fc337-019a-4f91-a73e-169f7e0cd91c",
                            "ElementName": "Level : F1",
                            "EntityType": "TBIM_BUILDINGSTOREY",
                            "IsDelete": 0,
                            "Level": 7,
                            "ParentElementId": "377e4f9d-d20e-4209-b1e8-0ddb32e888c8",
                            "Sort": 1,
                            "SpaceCode": "000290001",
                            "SpacePoiId": "",
                            "SpaceTypeCode": "",
                            "SpaceTypeName": ""
                        }
                    },
                    {
                        "Children": [],
                        "ElementProfile": {
                            "BottomHeight": 0,
                            "BuildingId": "377e4f9d-d20e-4209-b1e8-0ddb32e888c8",
                            "ElementDesc": "from Rvt",
                            "ElementId": "28ddb220-3d6e-4464-8099-4be964d9cb87",
                            "ElementName": "Level : F2",
                            "EntityType": "TBIM_BUILDINGSTOREY",
                            "IsDelete": 0,
                            "Level": 7,
                            "ParentElementId": "377e4f9d-d20e-4209-b1e8-0ddb32e888c8",
                            "Sort": 2,
                            "SpaceCode": "000290002",
                            "SpacePoiId": "",
                            "SpaceTypeCode": "",
                            "SpaceTypeName": ""
                        }
                    },
                    {
                        "Children": [],
                        "ElementProfile": {
                            "BottomHeight": 0,
                            "BuildingId": "377e4f9d-d20e-4209-b1e8-0ddb32e888c8",
                            "ElementDesc": "from Rvt",
                            "ElementId": "985e2202-2fc9-490c-a80a-587b750c3496",
                            "ElementName": "Level : 室外地坪",
                            "EntityType": "TBIM_BUILDINGSTOREY",
                            "IsDelete": 0,
                            "Level": 7,
                            "ParentElementId": "377e4f9d-d20e-4209-b1e8-0ddb32e888c8",
                            "Sort": 3,
                            "SpaceCode": "000290003",
                            "SpacePoiId": "",
                            "SpaceTypeCode": "",
                            "SpaceTypeName": ""
                        }
                    },
                    {
                        "Children": [],
                        "ElementProfile": {
                            "BottomHeight": 0,
                            "BuildingId": "377e4f9d-d20e-4209-b1e8-0ddb32e888c8",
                            "ElementDesc": "from Rvt",
                            "ElementId": "e7cda0c3-5b0c-49e7-b2a6-4a654ca4b07b",
                            "ElementName": "Level : F3",
                            "EntityType": "TBIM_BUILDINGSTOREY",
                            "IsDelete": 0,
                            "Level": 7,
                            "ParentElementId": "377e4f9d-d20e-4209-b1e8-0ddb32e888c8",
                            "Sort": 4,
                            "SpaceCode": "000290004",
                            "SpacePoiId": "",
                            "SpaceTypeCode": "",
                            "SpaceTypeName": ""
                        }
                    },
                    {
                        "Children": [],
                        "ElementProfile": {
                            "BottomHeight": 0,
                            "BuildingId": "377e4f9d-d20e-4209-b1e8-0ddb32e888c8",
                            "ElementDesc": "from Rvt",
                            "ElementId": "b66aece1-62e9-49d3-872e-6e66156a853b",
                            "ElementName": "Level : F4",
                            "EntityType": "TBIM_BUILDINGSTOREY",
                            "IsDelete": 0,
                            "Level": 7,
                            "ParentElementId": "377e4f9d-d20e-4209-b1e8-0ddb32e888c8",
                            "Sort": 5,
                            "SpaceCode": "000290005",
                            "SpacePoiId": "",
                            "SpaceTypeCode": "",
                            "SpaceTypeName": ""
                        }
                    },
                    {
                        "Children": [],
                        "ElementProfile": {
                            "BottomHeight": 0,
                            "BuildingId": "377e4f9d-d20e-4209-b1e8-0ddb32e888c8",
                            "ElementDesc": "from Rvt",
                            "ElementId": "073b2c5f-8f62-4dfe-8fe6-bb24679b9803",
                            "ElementName": "未指定标高",
                            "EntityType": "TBIM_BUILDINGSTOREY",
                            "IsDelete": 0,
                            "Level": 7,
                            "ParentElementId": "377e4f9d-d20e-4209-b1e8-0ddb32e888c8",
                            "Sort": 6,
                            "SpaceCode": "000290001",
                            "SpacePoiId": "",
                            "SpaceTypeCode": "",
                            "SpaceTypeName": ""
                        }
                    }
                ],
                "ElementProfile": {
                    "BottomHeight": 0,
                    "BuildingId": "377e4f9d-d20e-4209-b1e8-0ddb32e888c8",
                    "ElementDesc": "",
                    "ElementId": "377e4f9d-d20e-4209-b1e8-0ddb32e888c8",
                    "ElementName": "三层小别墅",
                    "EntityType": "TBIM_BUILDING",
                    "IsDelete": 0,
                    "Level": 6,
                    "ParentElementId": "",
                    "Sort": 1,
                    "SpaceCode": "000290",
                    "SpacePoiId": "",
                    "SpaceTypeCode": "",
                    "SpaceTypeName": ""
                }
            }
        }
    }
}
```

