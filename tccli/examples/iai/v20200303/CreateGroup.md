**Example 1: 创建人员库成功示例**

创建人员库。

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

**Example 2: 创建人员库错误示例**



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

**Example 3: 创建人员库ID重复错误示例**



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

