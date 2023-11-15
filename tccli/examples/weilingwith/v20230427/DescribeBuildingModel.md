**Example 1: 查询建筑模型**

查询建筑模型成功响应示例

Input: 

```
tccli weilingwith DescribeBuildingModel --cli-unfold-argument  \
    --BuildingId 82d5fb5a-52d0-4636-a225-d46245e911ef \
    --WorkspaceId 1016 \
    --ApplicationToken ZRCJHdnhqEUEqO1vyskCgWimPucHhREV
```

Output: 
```
{
    "Response": {
        "RequestId": "8f193fa9-506a-421d-afe9-fdde94cc5849",
        "Result": {
            "Models": [
                {
                    "ElementId": "82d5fb5a-52d0-4636-a225-d46245e911ef",
                    "ElementName": "验证专用",
                    "ModelType": "MODEL_ORIGIN",
                    "ModelUrl": "https://bim-1301743406.cos.ap-guangzhou.myqcloud.com/100055/1016/cb6bad63-0855-4dc2-8908-20518627479b.glb?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDsyyqVvLagaL8lBZq5896tTxOfjbL2h8L%26q-sign-time%3D1692758001%3B1787366001%26q-key-time%3D1692758001%3B1787366001%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3Ddbac70b180e5a2d8c343506dae755a01669ffb04"
                },
                {
                    "ElementId": "82d5fb5a-52d0-4636-a225-d46245e911ef",
                    "ElementName": "验证专用-外壳",
                    "ModelType": "MODEL_HULL",
                    "ModelUrl": "https://bim-1301743406.cos.ap-guangzhou.myqcloud.com/100055/1016/ff847c36-89f8-4644-9c1f-d265bd5d5167.glb?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDsyyqVvLagaL8lBZq5896tTxOfjbL2h8L%26q-sign-time%3D1692758001%3B1787366001%26q-key-time%3D1692758001%3B1787366001%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3D7af0ab15cab83314e44026fedc0927467d07b776"
                },
                {
                    "ElementId": "0b00f88f-36f1-4ae3-a7b4-5db12332c005",
                    "ElementName": "-1F",
                    "ModelType": "MODEL_STOREY",
                    "ModelUrl": "https://bim-1301743406.cos.ap-guangzhou.myqcloud.com/100055/1016/2ee86ae4-41a1-4c45-840b-4e9eae1b83a1.glb?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDsyyqVvLagaL8lBZq5896tTxOfjbL2h8L%26q-sign-time%3D1692758001%3B1787366001%26q-key-time%3D1692758001%3B1787366001%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3De9b58a5293201d24c19e2bc28b49404035b569c1"
                },
                {
                    "ElementId": "61049c1b-158d-41bd-9f0b-df30a50401bd",
                    "ElementName": "RF",
                    "ModelType": "MODEL_STOREY",
                    "ModelUrl": "https://bim-1301743406.cos.ap-guangzhou.myqcloud.com/100055/1016/c96a40b9-f5b6-4523-b58d-15c79f4a4d3b.glb?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDsyyqVvLagaL8lBZq5896tTxOfjbL2h8L%26q-sign-time%3D1692758001%3B1787366001%26q-key-time%3D1692758001%3B1787366001%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3D1dfc789fc1770b898e4ffcca61a234449f2c8ff3"
                },
                {
                    "ElementId": "5880efdd-829e-4e3b-a3e2-9e5be4818747",
                    "ElementName": "-2F",
                    "ModelType": "MODEL_STOREY",
                    "ModelUrl": "https://bim-1301743406.cos.ap-guangzhou.myqcloud.com/100055/1016/f7afb966-8df5-416c-9e93-22e323cceca6.glb?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDsyyqVvLagaL8lBZq5896tTxOfjbL2h8L%26q-sign-time%3D1692758001%3B1787366001%26q-key-time%3D1692758001%3B1787366001%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3D12cfa0a9344a3064cdd0a3e75d81a160b44085ce"
                },
                {
                    "ElementId": "d0f4a172-6d8b-4993-b7f3-dec2fe8f0a57",
                    "ElementName": "1F",
                    "ModelType": "MODEL_STOREY",
                    "ModelUrl": "https://bim-1301743406.cos.ap-guangzhou.myqcloud.com/100055/1016/d4f94196-63cc-4075-885b-b73853653d78.glb?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDsyyqVvLagaL8lBZq5896tTxOfjbL2h8L%26q-sign-time%3D1692758001%3B1787366001%26q-key-time%3D1692758001%3B1787366001%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3De901cf3e32c4efe7344924a9c9f5a69b681d8e45"
                }
            ]
        }
    }
}
```

**Example 2: 查询建筑模型示例-prod**

查询建筑模型示例-prod

Input: 

```
tccli weilingwith DescribeBuildingModel --cli-unfold-argument  \
    --BuildingId 9e98dc3920df4230b431404222fefe37 \
    --WorkspaceId 1124 \
    --ApplicationToken Sl5ZDmVuHzhN52o8n1KWagl7sLdrLfN7
```

Output: 
```
{
    "Response": {
        "RequestId": "02cc707e-e6bf-4b5d-a1c3-0544eadfc3fa",
        "Result": {
            "Models": [
                {
                    "ElementId": "9e98dc3920df4230b431404222fefe37",
                    "ElementName": "rvm",
                    "ModelType": "MODEL_ORIGIN",
                    "ModelUrl": "https://bim-1317915939.cos.ap-guangzhou.myqcloud.com/100001/1124/070b7a50-90ec-4cdb-bd16-ce5073878bc9.glb?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDbGuX8hEh5PbnBXvFhy2rSqztYyA7pa6N%26q-sign-time%3D1693827299%3B1694345699%26q-key-time%3D1693827299%3B1694345699%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3Daa7fea7e00ec0c07ccee5f350fa7e881cfd78035"
                },
                {
                    "ElementId": "9e98dc3920df4230b431404222fefe37",
                    "ElementName": "rvm-外壳",
                    "ModelType": "MODEL_HULL",
                    "ModelUrl": "https://bim-1317915939.cos.ap-guangzhou.myqcloud.com/100001/1124/dbdb4717-6629-4a7e-85a7-b720eae82cdd.glb?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDbGuX8hEh5PbnBXvFhy2rSqztYyA7pa6N%26q-sign-time%3D1693827299%3B1694345699%26q-key-time%3D1693827299%3B1694345699%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3D9ba5a3ed7b71a008fb0e11b194f4c1948bc9c9e9"
                },
                {
                    "ElementId": "679279f4adaa431daf04bab2ea30ad28",
                    "ElementName": "/STABILIZER",
                    "ModelType": "MODEL_STOREY",
                    "ModelUrl": "https://bim-1317915939.cos.ap-guangzhou.myqcloud.com/100001/1124/d0c77567-597e-48fd-9afb-7afddb5d1786.glb?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDbGuX8hEh5PbnBXvFhy2rSqztYyA7pa6N%26q-sign-time%3D1693827299%3B1694345699%26q-key-time%3D1693827299%3B1694345699%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3Ddf00cf2e40bd39a3d26ce10e19f910d6e425c16f"
                },
                {
                    "ElementId": "4cf3865c355048d0be117466b89ff5ae",
                    "ElementName": "/SAMPLE-ADMIN",
                    "ModelType": "MODEL_STOREY",
                    "ModelUrl": "https://bim-1317915939.cos.ap-guangzhou.myqcloud.com/100001/1124/b04791d4-f6ad-43f5-a36d-74eba01b2090.glb?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDbGuX8hEh5PbnBXvFhy2rSqztYyA7pa6N%26q-sign-time%3D1693827299%3B1694345699%26q-key-time%3D1693827299%3B1694345699%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3D8f62e68d47eabbfe029af1d736815aa248691cf2"
                },
                {
                    "ElementId": "42ac80b2834442f89c9c73e723986012",
                    "ElementName": "/PSI-SAMPLE",
                    "ModelType": "MODEL_STOREY",
                    "ModelUrl": "https://bim-1317915939.cos.ap-guangzhou.myqcloud.com/100001/1124/12816356-f38e-4252-a8d0-6222df7d9421.glb?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDbGuX8hEh5PbnBXvFhy2rSqztYyA7pa6N%26q-sign-time%3D1693827299%3B1694345699%26q-key-time%3D1693827299%3B1694345699%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3D39f7013ce9d5e7d2d36532e2b54ab4edfbc605ff"
                }
            ]
        }
    }
}
```

