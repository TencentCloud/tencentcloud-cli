**Example 1: 查询构件属性示例-prod**

查询构件属性示例-prod

Input: 

```
tccli weilingwith DescribePropertyList --cli-unfold-argument  \
    --BuildingId 377e4f9d-d20e-4209-b1e8-0ddb32e888c8 \
    --ElementId b66aece1-62e9-49d3-872e-6e66156a853b \
    --WorkspaceId 1124 \
    --ApplicationToken Sl5ZDmVuHzhN52o8n1KWagl7sLdrLfN7
```

Output: 
```
{
    "Response": {
        "RequestId": "da778098-4425-4519-bd0b-589e9e83ef6f",
        "Result": {
            "BuildingId": "377e4f9d-d20e-4209-b1e8-0ddb32e888c8",
            "Coordinates": {
                "Altitude": 0,
                "Latitude": 39.12852507853361,
                "Longitude": 117.25139600000003
            },
            "ElementId": "b66aece1-62e9-49d3-872e-6e66156a853b",
            "ElementName": "Level : F4",
            "EntityTypeCode": "TBIM_BUILDINGSTOREY",
            "EntityTypeName": "楼层",
            "PropertySet": [
                {
                    "Content": "{Elevation=9500, Story Above=None}",
                    "Description": "",
                    "Name": "Constraints"
                },
                {
                    "Content": "{Computation Height=0}",
                    "Description": "",
                    "Name": "Dimensions"
                },
                {
                    "Content": "{Is ground plane=0}",
                    "Description": "",
                    "Name": "Display"
                },
                {
                    "Content": "{storeyType=TOP_FLOOR, floorHeight=3000, bottomHeight=9500}",
                    "Description": "",
                    "Name": "EDITOR_BUILDING_STOREY_EXTEND"
                },
                {
                    "Content": "{Scope Box=None}",
                    "Description": "",
                    "Name": "Extents"
                },
                {
                    "Content": "{IfcGUID=1LvAmy3$j18hHP$GEcP3rk, Export to IFC=0}",
                    "Description": "",
                    "Name": "IFC Parameters"
                },
                {
                    "Content": "{Structural=No, Design Option=None, Building Story=Yes}",
                    "Description": "",
                    "Name": "Identity Data"
                },
                {
                    "Content": "{Name=Level : F4, Type=C_上标高+层标, Childs=[Roofs], Family=Level, Type Id=87266, Category=OST_Levels, ClassName=OdBmCDANode, ODAUniqueID=214592, LocalizedName=, Family and Type=Level : C_上标高+层标}",
                    "Description": "",
                    "Name": "Invalid group"
                },
                {
                    "Content": "{Material=None}",
                    "Description": "",
                    "Name": "Materials and Finishes"
                }
            ],
            "Translate": {
                "X": 0,
                "Y": 0,
                "Z": 0
            }
        }
    }
}
```

**Example 2: 查询构件属性（详情）**

查询构件属性（详情）成功响应示例

Input: 

```
tccli weilingwith DescribePropertyList --cli-unfold-argument  \
    --BuildingId 2e374df6-7ba7-45d2-a44d-2a92bb2a6668 \
    --ElementId 2e374df6-7ba7-45d2-a44d-2a92bb2a6668 \
    --WorkspaceId 1016 \
    --ApplicationToken fquCgDi2QfNDMlNyQ5YPoMR2Zw4tQs2B
```

Output: 
```
{
    "Response": {
        "RequestId": "37ff2cfc-5c07-4c14-9f4f-82e52b155754",
        "Result": {
            "BuildingId": "2e374df6-7ba7-45d2-a44d-2a92bb2a6668",
            "Coordinates": {
                "Altitude": 0,
                "Latitude": 22.533192029618775,
                "Longitude": 113.93048000000002
            },
            "ElementId": "2e374df6-7ba7-45d2-a44d-2a92bb2a6668",
            "ElementName": "测试建筑",
            "EntityTypeCode": "TBIM_BUILDING",
            "EntityTypeName": "建筑",
            "PropertySet": [
                {
                    "Content": "{overground_floor=0, underground_floor=0, overground_floor_height=0, underground_floor_height=0}",
                    "Description": "editor building extend",
                    "Name": "EDITOR_BUILDING_EXTEND"
                },
                {
                    "Content": "{name=bh1.ifc, size=7384171, type=IFC, pinyin=bh1.ifc, fileKey=/bim/6ced4b4a-e34c-49fb-b8fc-15b63d6fd682.ifc, uploadTS=1685446303474, relTaskId=4058f87f-2bc1-4f28-9c05-25426987dafb}",
                    "Description": "building file",
                    "Name": "TBIM_BUILDING_FILE"
                },
                {
                    "Content": "{NumberOfStoreys=5}",
                    "Description": "",
                    "Name": "Pset_BuildingCommon"
                },
                {
                    "Content": "",
                    "Description": "element extend attributes",
                    "Name": "TBIM_PROPERTY_EXTEND_ATTR"
                },
                {
                    "Content": "{MODEL_HULL=00e79829-d8d1-468b-a497-1a6172be051c.glb, MODEL_ORIGIN=b92563fe-c61f-45df-a9e5-c01ecddb4c77.glb, MODEL_STOREY={30eZ3ov6r4ygu6QtqZ6IN$=5149f7ea-d3ab-470e-9d50-06f190bf2e5a.glb, 30eZ3ov6r4ygu6QtqZ6INI=23268a8e-c01d-4f92-b6ef-a3f5b3740765.glb, 30eZ3ov6r4ygu6QtqZ6INW=955e5c87-dbd5-4197-9eb5-f3216265f36f.glb, 30eZ3ov6r4ygu6QtqZ6INf=8b8fdeda-22d0-44b0-bd09-2dd0592d4713.glb, 30eZ3ov6r4ygu6QtqZ6INs=e72910c7-9d8b-464f-912d-f21fe2b87f2b.glb}}",
                    "Description": "",
                    "Name": "TBIM_BUILDING_GLB_MODEL"
                }
            ],
            "Translate": {
                "X": 0,
                "Y": 0,
                "Z": 0
            }
        }
    }
}
```

