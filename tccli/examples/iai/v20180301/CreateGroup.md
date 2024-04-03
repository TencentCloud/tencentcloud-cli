**Example 1: 错误示例**

人员库ID不支持中文

Input: 

```
tccli iai CreateGroup --cli-unfold-argument  \
    --GroupName 腾讯深圳员工库 \
    --GroupId 腾讯深圳员工库
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.GroupIdIllegal",
            "Message": "人员库ID包含非法字符。人员库ID只支持英文、数字、-%@#&_。"
        },
        "RequestId": "8125dda4-2905-4e02-88bd-79a93a660ad2"
    }
}
```

**Example 2: 错误示例-2**

人员库ID不可重复

Input: 

```
tccli iai CreateGroup --cli-unfold-argument  \
    --GroupName 腾讯深圳员工库 \
    --GroupId TencentShenZhenEmployee
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.GroupIdAlreadyExist",
            "Message": "人员库ID已经存在。人员库ID不可重复。"
        },
        "RequestId": "76ec6e41-37d6-4ab9-abef-48ef0c6ab175"
    }
}
```

**Example 3: 创建人员库接口**



Input: 

```
tccli iai CreateGroup --cli-unfold-argument  \
    --GroupName 某某大学竹园宿舍楼1号楼 \
    --GroupId ZhuYuanDormitoryNo1 \
    --FaceModelVersion 3.0 \
    --Tag 全是女生哦 \
    --GroupExDescriptions 学院名 专业 年级 学号
```

Output: 
```
{
    "Response": {
        "FaceModelVersion": "3.0",
        "RequestId": "1695f3dd-b668-479e-8b87-f37de371a8ec"
    }
}
```

**Example 4: 创建人员库接口-2**

创建人员库

Input: 

```
tccli iai CreateGroup --cli-unfold-argument  \
    --GroupName 腾讯深圳员工库 \
    --FaceModelVersion 3.0 \
    --GroupId TencentShenZhenEmployee \
    --Tag 不含实习生 \
    --GroupExDescriptions 事业群 部门名 组名
```

Output: 
```
{
    "Response": {
        "FaceModelVersion": "3.0",
        "RequestId": "e53ee4ec-9099-4b35-a129-21dd4820ff85"
    }
}
```

