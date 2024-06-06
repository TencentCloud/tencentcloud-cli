**Example 1: 示例**



Input: 

```
tccli clouddc GetTreeNode --cli-unfold-argument  \
    --Code HA000001
```

Output: 
```
{
    "Response": {
        "Data": {
            "Code": "abc",
            "Desc": "abc",
            "Name": "abc",
            "Level": 1,
            "DictId": 1,
            "NameEn": "abc",
            "Status": 1,
            "Creator": "abc",
            "Version": 1,
            "Managers": [
                "abc"
            ],
            "Modifier": "abc",
            "CenterIds": [
                1
            ],
            "CreateTime": "abc",
            "ProductNum": 1,
            "UpdateTime": "abc",
            "DepartmentIds": [
                "abc"
            ],
            "IntroPageStatus": 1,
            "ReportLevelList": [
                {
                    "Code": "abc",
                    "Name": "abc",
                    "Level": "abc",
                    "Status": "abc",
                    "Creator": "abc",
                    "Children": [
                        {
                            "Code": "abc",
                            "Name": "abc",
                            "Level": "abc",
                            "Status": "abc",
                            "Creator": "abc",
                            "Modifier": "abc",
                            "CreateTime": "abc",
                            "ParentCode": "abc",
                            "ParentName": "abc",
                            "UpdateTime": "abc"
                        }
                    ],
                    "HasChild": "abc",
                    "Modifier": "abc",
                    "CreateTime": "abc",
                    "UpdateTime": "abc"
                }
            ],
            "EffectProductNum": 1,
            "CalcStatusProducts": [
                {
                    "Num": 1,
                    "Status": "abc"
                }
            ],
            "ParentDepartmentIds": [
                1
            ]
        },
        "RequestId": "abc"
    }
}
```

