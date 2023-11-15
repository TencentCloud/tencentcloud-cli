**Example 1: 查询设备绑定的空间信息**

查询设备绑定的空间信息成功响应示例

Input: 

```
tccli weilingwith DescribeSpaceInfoByDeviceId --cli-unfold-argument  \
    --DeviceId 1c902558-d360-4a93-9b6f-1b49970534f7 \
    --WorkspaceId 1016 \
    --ApplicationToken 0VGYLwQaH4ejNnwSMIfYtl0zlstprsdZ
```

Output: 
```
{
    "Response": {
        "RequestId": "901e3a31-d49c-4570-b96c-dcddee09c22d",
        "Result": {
            "BottomHeight": 3000,
            "BuildingId": "82d5fb5a-52d0-4636-a225-d46245e911ef",
            "ElementId": "8a74aba0-46e3-4097-89e6-7adbeb9ccaef",
            "ElementName": "",
            "EntityType": "TBIM_CAMERA",
            "Level": 9,
            "SpaceCode": "00003000300000008"
        }
    }
}
```

**Example 2: 查询设备绑定的空间信息示例-prod**

查询设备绑定的空间信息示例-prod

Input: 

```
tccli weilingwith DescribeSpaceInfoByDeviceId --cli-unfold-argument  \
    --DeviceId 3049938c-3048-4fef-a2e8-2843ede35edb \
    --WorkspaceId 1133 \
    --ApplicationToken Sl5ZDmVuHzhN52o8n1KWagl7sLdrLfN7
```

Output: 
```
{
    "Response": {
        "RequestId": "750095c6-29f0-4598-b1d7-16e15d43e774",
        "Result": {
            "BottomHeight": 24750,
            "BuildingId": "306fc545-fc98-4513-ae6e-751f990ae61a",
            "ElementId": "3425fbe2-3d6c-471f-9527-b878f35d1f03",
            "ElementName": "",
            "EntityType": "TBIM_CUSTOMCOLUMN",
            "Level": 8,
            "SpaceCode": "00021804800000470"
        }
    }
}
```

