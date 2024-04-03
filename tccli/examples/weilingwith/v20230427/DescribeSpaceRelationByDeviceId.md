**Example 1: 查询设备绑定的空间层级关系示例-prod**

查询设备绑定的空间层级关系示例-prod

Input: 

```
tccli weilingwith DescribeSpaceRelationByDeviceId --cli-unfold-argument  \
    --DeviceId 3049938c-3048-4fef-a2e8-2843ede35edb \
    --WorkspaceId 1133 \
    --ApplicationToken Sl5ZDmVuHzhN52o8n1KWagl7sLdrLfN7
```

Output: 
```
{
    "Response": {
        "RequestId": "9565acba-fb0e-4ec7-be20-ab274b105fd9",
        "Result": {
            "SpaceRelation": {
                "Children": [
                    {
                        "Children": [
                            {
                                "Children": [],
                                "ElementId": "3425fbe2-3d6c-471f-9527-b878f35d1f03",
                                "ElementName": "",
                                "Level": 8,
                                "ParentSpaceCode": "000218048",
                                "SpaceCode": "00021804800000470"
                            }
                        ],
                        "ElementId": "57e7c90c-e3e2-46e0-b9ee-8084c1889620",
                        "ElementName": "7F",
                        "Level": 7,
                        "ParentSpaceCode": "000218",
                        "SpaceCode": "000218048"
                    }
                ],
                "ElementId": "306fc545-fc98-4513-ae6e-751f990ae61a",
                "ElementName": "BHDA-1",
                "Level": 6,
                "ParentSpaceCode": "",
                "SpaceCode": "000218"
            }
        }
    }
}
```

**Example 2: 查询指定空间下设备与构件绑定关系列表**

查询指定空间下设备与构件绑定关系列表成功响应示例

Input: 

```
tccli weilingwith DescribeSpaceRelationByDeviceId --cli-unfold-argument  \
    --DeviceId ad655ba1-975a-4238-94d7-5d2015d1cf1f \
    --WorkspaceId 1016 \
    --ApplicationToken GUsHDOIP614sDxEIiliCx7GIKTqyONoX
```

Output: 
```
{
    "Response": {
        "RequestId": "30b9a52a-1ed8-4d97-b17d-2459b938ca3a",
        "Result": {
            "SpaceRelation": {
                "Children": [
                    {
                        "Children": [
                            {
                                "Children": [],
                                "ElementId": "bdbbf537-d6c4-4b1e-80ae-e0bcaab8b06f",
                                "ElementName": "test_no_100",
                                "Level": 9,
                                "ParentSpaceCode": "000162002",
                                "SpaceCode": "00016200200000003"
                            }
                        ],
                        "ElementId": "f3c5ffa5-05e3-4c26-a447-0edf71aa9783",
                        "ElementName": "1F",
                        "Level": 7,
                        "ParentSpaceCode": "000162",
                        "SpaceCode": "000162002"
                    }
                ],
                "ElementId": "377a53a6-c5a7-445d-a3b7-c2d721f95408",
                "ElementName": "小智新设备挂接0628",
                "Level": 6,
                "ParentSpaceCode": "",
                "SpaceCode": "000162"
            }
        }
    }
}
```

