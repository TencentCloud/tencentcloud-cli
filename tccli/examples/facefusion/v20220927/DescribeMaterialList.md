**Example 1: 查询素材列表**

查询素材列表
目前每次拉取素材最多可支持拉取20条素材信息，如果需要拉取全部素材信息，可以分多次请求通过“偏移量”跟“拉取条数” 拉取全部素材信息。
参数填写示例：
第一次请求：Offset=0；Limit=20
第二次请求：Offset=20；Limit=20
第三次请求：Offset=40；Limit=20

Input: 

```
tccli facefusion DescribeMaterialList --cli-unfold-argument  \
    --ActivityId at_1582658911993147392 \
    --Offset 0 \
    --Limit 5
```

Output: 
```
{
    "Response": {
        "Count": 5,
        "MaterialInfos": [
            {
                "AuditResult": "审核成功",
                "CreateTime": "2022-11-29 18:46:34",
                "MaterialFaceList": [
                    {
                        "FaceId": "mt_1597542526641664000_1",
                        "FaceInfo": {
                            "Height": 167,
                            "Width": 128,
                            "X": 221,
                            "Y": 125
                        }
                    }
                ],
                "MaterialId": "mt_1597542526641664000",
                "MaterialName": "test1.png",
                "MaterialStatus": 0,
                "UpdateTime": "2022-11-29 18:46:34"
            },
            {
                "AuditResult": "审核成功",
                "CreateTime": "2022-12-15 14:19:51",
                "MaterialFaceList": [
                    {
                        "FaceId": "mt_1603273612711829504_1",
                        "FaceInfo": {
                            "Height": 167,
                            "Width": 128,
                            "X": 221,
                            "Y": 125
                        }
                    }
                ],
                "MaterialId": "mt_1603273612711829504",
                "MaterialName": "test2.png",
                "MaterialStatus": 0,
                "UpdateTime": "2022-12-15 14:19:51"
            },
            {
                "AuditResult": "审核成功",
                "CreateTime": "2022-11-10 10:28:10",
                "MaterialFaceList": [
                    {
                        "FaceId": "mt_1590531733435097088_1",
                        "FaceInfo": {
                            "Height": 167,
                            "Width": 128,
                            "X": 221,
                            "Y": 125
                        }
                    }
                ],
                "MaterialId": "mt_1590531733435097088",
                "MaterialName": "test3.png",
                "MaterialStatus": 1,
                "UpdateTime": "2022-12-07 17:10:54"
            },
            {
                "AuditResult": "审核成功",
                "CreateTime": "2022-12-07 16:13:41",
                "MaterialFaceList": [
                    {
                        "FaceId": "mt_1600403157392855040_1",
                        "FaceInfo": {
                            "Height": 236,
                            "Width": 177,
                            "X": 186,
                            "Y": 95
                        }
                    }
                ],
                "MaterialId": "mt_1600403157392855040",
                "MaterialName": "test4.png",
                "MaterialStatus": 3,
                "UpdateTime": "2022-12-07 16:13:52"
            },
            {
                "AuditResult": "审核成功",
                "CreateTime": "2022-12-15 14:20:21",
                "MaterialFaceList": [
                    {
                        "FaceId": "mt_1603273738050215936_1",
                        "FaceInfo": {
                            "Height": 129,
                            "Width": 119,
                            "X": 215,
                            "Y": 69
                        }
                    }
                ],
                "MaterialId": "mt_1603273738050215936",
                "MaterialName": "test5.jpg",
                "MaterialStatus": 3,
                "UpdateTime": "2022-12-15 14:25:28"
            }
        ],
        "RequestId": "3e93f5d5-415b-41bf-bde4-c4f97e9e0089"
    }
}
```

