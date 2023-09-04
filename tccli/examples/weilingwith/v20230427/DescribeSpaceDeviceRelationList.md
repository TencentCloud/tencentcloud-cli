**Example 1: 查询指定空间下设备与构件绑定关系列表**

查询指定空间下设备与构件绑定关系列表成功响应示例

Input: 

```
tccli weilingwith DescribeSpaceDeviceRelationList --cli-unfold-argument  \
    --ElementIds 82d5fb5a-52d0-4636-a225-d46245e911ef \
    --IsCascade True \
    --WorkspaceId 1016 \
    --PageNumber 1 \
    --PageSize 10 \
    --ApplicationToken 0VGYLwQaH4ejNnwSMIfYtl0zlstprsdZ
```

Output: 
```
{
    "Response": {
        "RequestId": "6923a12d-747c-4cf2-99d5-6c74af01cb39",
        "Result": {
            "SpaceDeviceRelationList": [
                {
                    "DeviceId": "1c902558-d360-4a93-9b6f-1b49970534f7",
                    "ElementId": "8a74aba0-46e3-4097-89e6-7adbeb9ccaef"
                },
                {
                    "DeviceId": "b66603af-7f8c-46c0-8712-1353a08d5806",
                    "ElementId": "af7f7d83-17f8-4dff-80e2-a5129a39eab0"
                },
                {
                    "DeviceId": "282e3b5f-5a08-45cf-ab86-fb5d3ca6ceea",
                    "ElementId": "f596e5e3-68fb-48e6-bd74-845d623e600f"
                },
                {
                    "DeviceId": "0826a816-e153-4448-873d-b284f9cf6f22",
                    "ElementId": "b95c73d1-208a-4342-ac54-5627b2021627"
                },
                {
                    "DeviceId": "5f089c7e-0530-44c9-9435-c6aaf92f6a29",
                    "ElementId": "8ace642a-c45f-401a-890c-6570f08fd97a"
                },
                {
                    "DeviceId": "c0e3f641-6ec6-444e-8ac9-3cfecc755cb0",
                    "ElementId": "a1162f6d-e8c4-4bd2-af78-dbbdb2918b6d"
                },
                {
                    "DeviceId": "e9e0fe2e-b188-4f42-9a4c-acd63c1d3ac5",
                    "ElementId": "14d0e599-396d-4d64-8843-bf4ea10e7f75"
                },
                {
                    "DeviceId": "90ad0dc7-2f59-4af3-98db-6d43d5602ff2",
                    "ElementId": "36d2a1dc-5aaf-49d3-8151-3327d83a062b"
                },
                {
                    "DeviceId": "d80db7ed-0efc-4456-9694-f8292cae7163",
                    "ElementId": "05159066-26b4-4f40-9810-04b54227ab8a"
                },
                {
                    "DeviceId": "f7b7ec55-f2b3-45a0-8010-8d2d4cd9d58d",
                    "ElementId": "6afd8e84-97e5-4df9-8788-ca2551ea3f96"
                }
            ]
        }
    }
}
```

**Example 2: 查询指定空间下设备与构件绑定关系列表示例-prod**

查询指定空间下设备与构件绑定关系列表示例-prod

Input: 

```
tccli weilingwith DescribeSpaceDeviceRelationList --cli-unfold-argument  \
    --ElementIds 306fc545-fc98-4513-ae6e-751f990ae61a \
    --IsCascade True \
    --WorkspaceId 1133 \
    --PageNumber 1 \
    --PageSize 10 \
    --ApplicationToken Sl5ZDmVuHzhN52o8n1KWagl7sLdrLfN7
```

Output: 
```
{
    "Response": {
        "RequestId": "d2f8170b-0ef2-4b7a-aee4-6946a6028e59",
        "Result": {
            "SpaceDeviceRelationList": [
                {
                    "DeviceId": "675a9490-dd66-4ac7-b39b-c74977899a1a",
                    "ElementId": "be78cede-0c33-4771-80ec-2959fd5ecd3b"
                },
                {
                    "DeviceId": "14dfa61a-762b-4785-bd39-cd709c6cf3d9",
                    "ElementId": "9e03687f-727f-472e-8722-39eacd069a6c"
                },
                {
                    "DeviceId": "840e3fe7-4eb4-4a64-9036-02ba94956e06",
                    "ElementId": "e80dd0b5-1123-4c81-b8f4-5fbc09f16957"
                },
                {
                    "DeviceId": "3247728f-15d2-48a2-a0fc-d07a6a6023f0",
                    "ElementId": "b3ca676b-389e-4bb9-a549-22e6a34b06e9"
                },
                {
                    "DeviceId": "90f965da-5ed9-469c-bace-7ecd09e2693c",
                    "ElementId": "8c06cb9e-ed92-4b26-9491-eb7a615ef3d0"
                },
                {
                    "DeviceId": "1635422d-5de3-4e38-9f68-94b43fd78185",
                    "ElementId": "308adda6-5121-437f-b9d7-a60484cd4f78"
                },
                {
                    "DeviceId": "35bc7027-567a-48d2-a3ee-63c57be9ae9f",
                    "ElementId": "83068b31-ecf0-4e1f-8e21-08588830bb37"
                },
                {
                    "DeviceId": "749287c4-c48f-42f4-b083-838c1b2fef09",
                    "ElementId": "572d813d-64fa-4b50-b2c9-cc1a729f7b90"
                },
                {
                    "DeviceId": "50a294f4-9289-43d0-aa27-efc31c7405ac",
                    "ElementId": "238c7691-0472-468c-9c66-4cc3dbdff880"
                },
                {
                    "DeviceId": "3049938c-3048-4fef-a2e8-2843ede35edb",
                    "ElementId": "3425fbe2-3d6c-471f-9527-b878f35d1f03"
                }
            ]
        }
    }
}
```

