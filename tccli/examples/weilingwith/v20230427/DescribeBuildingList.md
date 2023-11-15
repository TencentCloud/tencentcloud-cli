**Example 1: 查询建筑列表**

查询建筑列表成功响应示例

Input: 

```
tccli weilingwith DescribeBuildingList --cli-unfold-argument  \
    --WorkspaceId 1016 \
    --HasModel True \
    --ApplicationToken ZRCJHdnhqEUEqO1vyskCgWimPucHhREV
```

Output: 
```
{
    "Response": {
        "RequestId": "6fb5c58b-975c-40a0-ae17-437ddfa0d234",
        "Result": {
            "BuildingProfileList": [
                {
                    "Address": "北京市,东城区forest-12",
                    "BuildingId": "f207b473-3eb7-4b7c-873b-9e2549354234",
                    "BuildingName": "forest-12",
                    "Latitude": 39.92836,
                    "Longitude": 116.416336,
                    "SpaceCode": "000144"
                },
                {
                    "Address": "天津市,河东区test-1111",
                    "BuildingId": "112acca6-c448-413c-90cf-9da1ea880274",
                    "BuildingName": "test-1111",
                    "Latitude": 39.128525,
                    "Longitude": 117.251396,
                    "SpaceCode": "000141"
                },
                {
                    "Address": "北京市,东城区forest-11",
                    "BuildingId": "c5f12d6b-485f-4c31-82e9-e7d9a6053859",
                    "BuildingName": "forest-11",
                    "Latitude": 39.92836,
                    "Longitude": 116.416336,
                    "SpaceCode": "000140"
                },
                {
                    "Address": "北京市,东城区forest-10",
                    "BuildingId": "44ebb092-8a3e-46c2-a887-803d2e94aee9",
                    "BuildingName": "forest-10",
                    "Latitude": 39.92836,
                    "Longitude": 116.416336,
                    "SpaceCode": "000139"
                },
                {
                    "Address": "河北省,秦皇岛市,山海关区testdsds",
                    "BuildingId": "e89d3f4f-9f0e-4e34-9c94-18589870caa4",
                    "BuildingName": "testdsds",
                    "Latitude": 39.97888,
                    "Longitude": 119.775185,
                    "SpaceCode": "000102"
                },
                {
                    "Address": "北京市,东城区国际医疗保健中心V1",
                    "BuildingId": "5826a9ca-b14c-40de-95da-be635cfe846e",
                    "BuildingName": "国际医疗保健中心V1",
                    "Latitude": 39.92836,
                    "Longitude": 116.416336,
                    "SpaceCode": "000096"
                },
                {
                    "Address": "北京市,东城区天健一号楼",
                    "BuildingId": "d04de59d-3bf1-42a8-a894-74ffe6a2dd25",
                    "BuildingName": "天健一号楼",
                    "Latitude": 39.92836,
                    "Longitude": 116.416336,
                    "SpaceCode": "000094"
                },
                {
                    "Address": "北京市,东城区测试建筑数据0818",
                    "BuildingId": "00110b6b-2d67-4cf5-ae08-de0fe5118a4d",
                    "BuildingName": "测试建筑数据0818",
                    "Latitude": 39.92836,
                    "Longitude": 116.416336,
                    "SpaceCode": "000092"
                },
                {
                    "Address": "广东省,深圳市,南山区前海大厦",
                    "BuildingId": "956bd069-c802-4bbb-b325-18d30d7bcd3c",
                    "BuildingName": "前海test",
                    "Latitude": 22.527027,
                    "Longitude": 113.899185,
                    "SpaceCode": "000185"
                },
                {
                    "Address": "河北省,邯郸市,峰峰矿区小别墅",
                    "BuildingId": "044b1384-f965-440a-875b-0a64b61c2388",
                    "BuildingName": "小别墅",
                    "Latitude": 36.419296,
                    "Longitude": 114.21257,
                    "SpaceCode": "000183"
                },
                {
                    "Address": "河北省,秦皇岛市,北戴河区成大中心",
                    "BuildingId": "41151071-5230-422b-9ff3-dff735172823",
                    "BuildingName": "成大中心",
                    "Latitude": 39.83491,
                    "Longitude": 119.48449,
                    "SpaceCode": "000176"
                },
                {
                    "Address": "天津市,河西区gzip",
                    "BuildingId": "ec4a49d9-e710-4bd9-a694-f3a99dd4796a",
                    "BuildingName": "gzip",
                    "Latitude": 39.10968,
                    "Longitude": 117.22338,
                    "SpaceCode": "000175"
                },
                {
                    "Address": "广东省,深圳市,南山区腾讯滨海大厦",
                    "BuildingId": "5fe9a07f-a632-4da9-abb7-9133a18e9505",
                    "BuildingName": "滨海3层",
                    "Latitude": 22.522806,
                    "Longitude": 113.93534,
                    "SpaceCode": "000174"
                },
                {
                    "Address": "北京市,西城区江森",
                    "BuildingId": "988f3768-933b-4fe7-81ef-174a62e4aa0c",
                    "BuildingName": "江森",
                    "Latitude": 39.9126,
                    "Longitude": 116.36585,
                    "SpaceCode": "000173"
                },
                {
                    "Address": "山西省,长治市,上党区DDDD",
                    "BuildingId": "1f8315b1-16f1-4c1f-b6e7-e35eb735d802",
                    "BuildingName": "DDDD",
                    "Latitude": 36.05315,
                    "Longitude": 113.051346,
                    "SpaceCode": "000171"
                },
                {
                    "Address": "天津市,河东区小智新设备挂接0628",
                    "BuildingId": "377a53a6-c5a7-445d-a3b7-c2d721f95408",
                    "BuildingName": "小智新设备挂接0628",
                    "Latitude": 39.128525,
                    "Longitude": 117.251396,
                    "SpaceCode": "000162"
                },
                {
                    "Address": "北京市,东城区测试IFC数据13",
                    "BuildingId": "d61c36cd-cb38-4909-9348-679ef2693f38",
                    "BuildingName": "测试IFC数据13",
                    "Latitude": 39.92836,
                    "Longitude": 116.416336,
                    "SpaceCode": "000078"
                },
                {
                    "Address": "北京市,东城区测试IFC数据11",
                    "BuildingId": "8e3afa64-834f-41b7-8539-1e5a7a38dac4",
                    "BuildingName": "测试IFC数据11",
                    "Latitude": 39.92836,
                    "Longitude": 116.416336,
                    "SpaceCode": "000074"
                },
                {
                    "Address": "北京市,东城区测试IFC数据10",
                    "BuildingId": "decd96a8-b312-4b10-a609-95e681f2356d",
                    "BuildingName": "测试IFC数据10",
                    "Latitude": 39.92836,
                    "Longitude": 116.416336,
                    "SpaceCode": "000073"
                },
                {
                    "Address": "北京市,西城区测试IFC数据07",
                    "BuildingId": "f25d2dbd-f31c-47bb-8ac7-8208864312f1",
                    "BuildingName": "测试IFC数据07",
                    "Latitude": 39.9126,
                    "Longitude": 116.36585,
                    "SpaceCode": "000072"
                },
                {
                    "Address": "北京市,东城区测试IFC数据04",
                    "BuildingId": "07771a01-2430-475a-9d93-456031710d95",
                    "BuildingName": "测试IFC数据04(1)(1)(1)(1)(1)(1)(1)(1)(1)(1)",
                    "Latitude": 39.92836,
                    "Longitude": 116.416336,
                    "SpaceCode": "000070"
                },
                {
                    "Address": "北京市,东城区测试IFC数据05",
                    "BuildingId": "d635e346-9660-495e-b6a4-522e97b8a985",
                    "BuildingName": "测试IFC数据05",
                    "Latitude": 39.92836,
                    "Longitude": 116.416336,
                    "SpaceCode": "000070"
                },
                {
                    "Address": "北京市,东城区测试IFC数据06",
                    "BuildingId": "c5279f0c-8d2a-4593-b1cf-eb24fc671e38",
                    "BuildingName": "测试IFC数据06(1)(1)(1)(1)(1)(1)(1)(1)(1)(1)(1)(1)(1)(1",
                    "Latitude": 39.92836,
                    "Longitude": 116.416336,
                    "SpaceCode": "000054"
                },
                {
                    "Address": "北京市,东城区测试IFC数据03",
                    "BuildingId": "7ccebedd-8f4c-40cd-8537-3c0ce8adf992",
                    "BuildingName": "测试IFC数据03",
                    "Latitude": 39.92836,
                    "Longitude": 116.416336,
                    "SpaceCode": "000033"
                },
                {
                    "Address": "北京市,东城区测试IFC数据01",
                    "BuildingId": "12b929ad-0974-4704-9b4b-90df4b7cf0cd",
                    "BuildingName": "测试IFC数据01",
                    "Latitude": 39.92836,
                    "Longitude": 116.416336,
                    "SpaceCode": "000031"
                },
                {
                    "Address": "北京市,朝阳区验证专用",
                    "BuildingId": "82d5fb5a-52d0-4636-a225-d46245e911ef",
                    "BuildingName": "验证专用",
                    "Latitude": 39.94446,
                    "Longitude": 116.50771,
                    "SpaceCode": "000030"
                },
                {
                    "Address": "北京市,朝阳区验证在线发布",
                    "BuildingId": "3d6ce0c9-7263-4287-88f1-c8d72e87968b",
                    "BuildingName": "验证在线发布",
                    "Latitude": 39.94446,
                    "Longitude": 116.50771,
                    "SpaceCode": "000021"
                },
                {
                    "Address": "江苏省,常州市,武进区测试楼层模型获取",
                    "BuildingId": "47f85a70-0317-4706-acfc-96b5a2e3a88e",
                    "BuildingName": "测试楼层模型获取",
                    "Latitude": 31.701252,
                    "Longitude": 119.942444,
                    "SpaceCode": "000012"
                },
                {
                    "Address": "广东省,深圳市,南山区测试建筑",
                    "BuildingId": "2e374df6-7ba7-45d2-a44d-2a92bb2a6668",
                    "BuildingName": "测试建筑",
                    "Latitude": 22.533192,
                    "Longitude": 113.93048,
                    "SpaceCode": "000003"
                }
            ]
        }
    }
}
```

**Example 2: 查询建筑列表示例-prod**

查询建筑列表示例-prod

Input: 

```
tccli weilingwith DescribeBuildingList --cli-unfold-argument  \
    --WorkspaceId 1109 \
    --ApplicationToken LMb6piRXpioR7nmwFhXpvZd4GC4wf0B4
```

Output: 
```
{
    "Response": {
        "RequestId": "16d8c7ac-449a-45d0-8181-15cf06a0e8e1",
        "Result": {
            "BuildingProfileList": [
                {
                    "Address": "999",
                    "BuildingId": "bef95f2a-9474-4635-8c66-3a0f0bf0e9b2",
                    "BuildingName": "999",
                    "Latitude": 39.902985,
                    "Longitude": 116.426636,
                    "SpaceCode": "000011"
                },
                {
                    "Address": "312",
                    "BuildingId": "a2284645-2c5f-4018-b20f-5e9298c2daec",
                    "BuildingName": "312",
                    "Latitude": 39.935,
                    "Longitude": 116.43041,
                    "SpaceCode": "000010"
                },
                {
                    "Address": "北京市,丰台区样例模型",
                    "BuildingId": "2da7d294-483e-4033-a99a-49f7323fd6ef",
                    "BuildingName": "样例模型1",
                    "Latitude": 39.927326,
                    "Longitude": 116.39177,
                    "SpaceCode": "000009"
                },
                {
                    "Address": "2322",
                    "BuildingId": "f54f2bd9-74ae-4bbf-bbf6-5b41c0d170e1",
                    "BuildingName": "2322",
                    "Latitude": 39.926315,
                    "Longitude": 116.34252,
                    "SpaceCode": "000008"
                },
                {
                    "Address": "1#楼",
                    "BuildingId": "dfad5b19-79d8-4e40-9a8c-8efa32a1f425",
                    "BuildingName": "1#楼",
                    "Latitude": 39.92442,
                    "Longitude": 116.38269,
                    "SpaceCode": "000007"
                },
                {
                    "Address": "32232",
                    "BuildingId": "3f25ef75-579b-4041-afcb-a328b106b99e",
                    "BuildingName": "32232",
                    "Latitude": 39.94474,
                    "Longitude": 116.34115,
                    "SpaceCode": "000006"
                },
                {
                    "Address": "3333dgn",
                    "BuildingId": "daeacc05-67e8-494f-8c7c-ff3678f490ad",
                    "BuildingName": "3333dgn",
                    "Latitude": 39.913147,
                    "Longitude": 116.39677,
                    "SpaceCode": "000005"
                },
                {
                    "Address": "912",
                    "BuildingId": "c4830dd5-d8b3-4d21-8179-17dd838ef221",
                    "BuildingName": "912",
                    "Latitude": 39.91262,
                    "Longitude": 116.35694,
                    "SpaceCode": "000381"
                },
                {
                    "Address": "",
                    "BuildingId": "c6a46ced-e0ea-4ab3-9c33-216defb26153",
                    "BuildingName": "空间编辑器我的建筑",
                    "Latitude": 0,
                    "Longitude": 0,
                    "SpaceCode": "000019"
                },
                {
                    "Address": "",
                    "BuildingId": "05d663eb-c96f-4c92-9bf8-9792d4df9cee",
                    "BuildingName": "场地",
                    "Latitude": 0,
                    "Longitude": 0,
                    "SpaceCode": "000004"
                },
                {
                    "Address": "",
                    "BuildingId": "6ac8db4a-af6e-4d5e-a8f4-a58e0c8b98e1",
                    "BuildingName": "建筑",
                    "Latitude": 0,
                    "Longitude": 0,
                    "SpaceCode": "000003"
                }
            ]
        }
    }
}
```

