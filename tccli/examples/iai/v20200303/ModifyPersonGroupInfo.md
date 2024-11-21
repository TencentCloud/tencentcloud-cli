**Example 1: 错误示例**

人员库ID不存在。

Input: 

```
tccli iai ModifyPersonGroupInfo --cli-unfold-argument  \
    --GroupId TencentShenZhenEmployee \
    --PersonId 1001 \
    --PersonExDescriptionInfos.0.PersonExDescriptionIndex 1 \
    --PersonExDescriptionInfos.0.PersonExDescription 人工智能实验室
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.GroupIdNotExist",
            "Message": "人员库ID不存在。"
        },
        "RequestId": "f944657d-6260-4a2e-a4d8-9c1845f39e56"
    }
}
```

**Example 2: 修改人员描述信息接口**

修改人员描述信息。

Input: 

```
tccli iai ModifyPersonGroupInfo --cli-unfold-argument  \
    --GroupId ZhuYuanDormitoryNo1 \
    --PersonId 2001 \
    --PersonExDescriptionInfos.0.PersonExDescriptionIndex 3 \
    --PersonExDescriptionInfos.0.PersonExDescription 3150108080
```

Output: 
```
{
    "Response": {
        "RequestId": "77e11a2d-0fc0-4fba-ab25-016e998221c3"
    }
}
```

**Example 3: 修改人员描述信息接口-2**

修改人员描述信息。

Input: 

```
tccli iai ModifyPersonGroupInfo --cli-unfold-argument  \
    --GroupId TencentShenZhenEmployee \
    --PersonId 1001 \
    --PersonExDescriptionInfos.0.PersonExDescriptionIndex 1 \
    --PersonExDescriptionInfos.0.PersonExDescription 大数据及人工智能产品中心
```

Output: 
```
{
    "Response": {
        "RequestId": "77e11a2d-0fc0-4fba-ab25-016e998221c3"
    }
}
```

