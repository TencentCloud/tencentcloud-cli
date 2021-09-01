**Example 1: 修改人员库接口**



Input: 

```
tccli iai ModifyGroup --cli-unfold-argument  \
    --GroupId ZhuYuanDormitoryNo1 \
    --GroupName 某某大学竹园1号宿舍楼 \
    --Tag 研究生入住 \
    --GroupExDescriptionInfos.0.GroupExDescriptionIndex 0 \
    --GroupExDescriptionInfos.0.GroupExDescription 学院
```

Output: 
```
{
    "Response": {
        "RequestId": "da051f16-0400-49d4-9832-2cfd3b51866f"
    }
}
```

**Example 2: 修改人员库接口-2**

修改人员库名称、备注、自定义描述字段名称

Input: 

```
tccli iai ModifyGroup --cli-unfold-argument  \
    --GroupId TencentShenZhenEmployee \
    --GroupName 腾讯深圳在职人员库 \
    --Tag 包含实习生 \
    --GroupExDescriptionInfos.0.GroupExDescriptionIndex 1 \
    --GroupExDescriptionInfos.0.GroupExDescription 部门 \
    --GroupExDescriptionInfos.1.GroupExDescriptionIndex 2 \
    --GroupExDescriptionInfos.1.GroupExDescription 项目组
```

Output: 
```
{
    "Response": {
        "RequestId": "98381738-509f-4749-8a66-dbf54247333d"
    }
}
```

**Example 3: 错误示例**



Input: 

```
tccli iai ModifyGroup --cli-unfold-argument  \
    --GroupId TencentShenZhenEmployee \
    --GroupExDescriptionInfos.0.GroupExDescriptionIndex 0 \
    --GroupExDescriptionInfos.0.GroupExDescription 部门
```

Output: 
```
{
    "Response": {
        "RequestId": "4b483679-3f08-4a7c-b827-4a6332dc030f"
    }
}
```

**Example 4: 错误示例-2**

人员库名称不可重复

Input: 

```
tccli iai ModifyGroup --cli-unfold-argument  \
    --GroupId TencentShenZhenEmployee \
    --GroupName 某某大学竹园1号宿舍楼
```

Output: 
```
{
    "Response": {
        "RequestId": "2dcce170-30cf-4078-9b3c-309362fbad21"
    }
}
```

