**Example 1: 删除人员库接口**

删除指定人员库及包含的所有的人员

Input: 

```
tccli iai DeleteGroup --cli-unfold-argument  \
    --GroupId ZhuYuanDormitoryNo1
```

Output: 
```
{
    "Response": {
        "RequestId": "2ff7181c-ef20-4f02-b4ed-13924b381368"
    }
}
```

**Example 2: 错误示例**

人员库ID不存在

Input: 

```
tccli iai DeleteGroup --cli-unfold-argument  \
    --GroupId ZhuYuanDormitory
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.GroupIdNotExist",
            "Message": "人员库ID不存在。"
        },
        "RequestId": "878b225f-d3a4-4aa0-a849-3df415ac61a9"
    }
}
```

