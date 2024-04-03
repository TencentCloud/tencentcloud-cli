**Example 1: 错误示例-2**

返回数量不能大于1000

Input: 

```
tccli iai GetGroupList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1001
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.LimitExceed",
            "Message": "返回数量不在合法范围内。"
        },
        "RequestId": "a6bb57de-773b-45e4-9e1c-c30ef48eba85"
    }
}
```

**Example 2: 获取人员库列表接口**

获取人员库列表

Input: 

```
tccli iai GetGroupList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "GroupInfos": [
            {
                "GroupName": "腾讯深圳员工",
                "GroupId": "TencentShenZhenEmployee",
                "GroupExDescriptions": [
                    "事业群",
                    "部门名",
                    "组名"
                ],
                "Tag": "不含实习生",
                "FaceModelVersion": "3.0",
                "CreationTimestamp": 1592210245686
            },
            {
                "GroupName": "某某大学竹园宿舍楼1号楼",
                "GroupId": "ZhuYuanDormitoryNo1",
                "GroupExDescriptions": [
                    "学院名",
                    "专业",
                    "年级",
                    "学号"
                ],
                "Tag": "全是女生哦",
                "FaceModelVersion": "3.0",
                "CreationTimestamp": 1594552117118
            }
        ],
        "GroupNum": 2,
        "RequestId": "72102087-a18d-4225-9ae9-87ef49e9f63e"
    }
}
```

