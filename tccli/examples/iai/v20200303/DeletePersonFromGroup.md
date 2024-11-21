**Example 1: 人员库删除人员成功示例**



Input: 

```
tccli iai DeletePersonFromGroup --cli-unfold-argument  \
    --PersonId 1001 \
    --GroupId TencentShenZhenEmployee
```

Output: 
```
{
    "Response": {
        "RequestId": "f9b22bbc-c94d-4287-a2ab-fa68f7bbbaf3"
    }
}
```

**Example 2: 人员库删除人员失败示例**



Input: 

```
tccli iai DeletePersonFromGroup --cli-unfold-argument  \
    --PersonId 3001 \
    --GroupId ZhuYuanDormitoryNo1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.GroupPersonMapNotExist",
            "Message": "组中不包含对应的人员Id。"
        },
        "RequestId": "b9d9641d-3de2-4a6f-a728-36a3b66e7bd0"
    }
}
```

