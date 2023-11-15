**Example 1: 设备列表**

成功响应

Input: 

```
tccli weilingwith DescribeDeviceList --cli-unfold-argument  \
    --WorkspaceId 1016 \
    --DeviceTypeSet w0701005 \
    --PageNumber 1 \
    --PageSize 1 \
    --ApplicationToken wA9bELuI4oulQCBK876UDBxe00dNcxQW
```

Output: 
```
{
    "Response": {
        "RequestId": "dd0b4025-2db7-4da3-998a-dda6cfc19441",
        "Result": {
            "DeviceDataSet": [
                {
                    "ActiveTime": "2023-04-13T14:11:24+08:00",
                    "DeviceName": "5f089c7e-0530-44c9-9435-c6aaf92f6a29",
                    "DeviceTagSet": [
                        "西安",
                        "真实"
                    ],
                    "DeviceTypeCode": "5f089c7e-0530-44c9-9435-c6aaf92f6a29",
                    "DeviceTypeName": "5f089c7e-0530-44c9-9435-c6aaf92f6a29",
                    "FieldList": [
                        {
                            "Id": 1,
                            "Key": "color",
                            "Name": "颜色",
                            "Val": ""
                        },
                        {
                            "Id": 3,
                            "Key": "height",
                            "Name": "高度",
                            "Val": ""
                        },
                        {
                            "Id": 64,
                            "Key": "size",
                            "Name": "尺寸",
                            "Val": ""
                        },
                        {
                            "Id": 65,
                            "Key": "weight",
                            "Name": "重量",
                            "Val": ""
                        },
                        {
                            "Id": 66,
                            "Key": "width",
                            "Name": "宽度",
                            "Val": ""
                        },
                        {
                            "Id": 67,
                            "Key": "long",
                            "Name": "长度",
                            "Val": ""
                        },
                        {
                            "Id": 68,
                            "Key": "volume",
                            "Name": "体积",
                            "Val": ""
                        }
                    ],
                    "IsActive": 1,
                    "IsLive": false,
                    "Location": {
                        "X": 30769.744140625,
                        "Y": 10080.6162109375,
                        "Z": 24750
                    },
                    "ModelId": "2000056",
                    "ModelName": "边缘摄像头",
                    "ParentWID": "",
                    "ParentWIDName": "",
                    "ProductAbility": 3,
                    "ProductId": 2000056,
                    "ProductName": "边缘摄像头",
                    "SN": "DS-2DE7530IW-A20190315AACHD00715442W",
                    "SpaceInfoSet": [
                        {
                            "Code": "000137",
                            "Id": "85dc534a-4f69-4553-aad0-368cda0f1e92",
                            "Level": 6,
                            "Name": "滨海大厦"
                        },
                        {
                            "Code": "000137048",
                            "Id": "bf0fb1b4-493c-458f-bf8c-7279963b4928",
                            "Level": 7,
                            "Name": "7F"
                        },
                        {
                            "Code": "00013704800003110",
                            "Id": "472ee223-5caf-46c1-beca-d7238a937733",
                            "Level": 9,
                            "Name": ""
                        }
                    ],
                    "WID": "5f089c7e-0530-44c9-9435-c6aaf92f6a29"
                }
            ],
            "PageNumber": 1,
            "PageSize": 1,
            "TotalPage": 16,
            "TotalRow": 16
        }
    }
}
```

