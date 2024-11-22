**Example 1: 获取人员库中人员数量成功示例**



Input: 

```
tccli iai GetPersonListNum --cli-unfold-argument  \
    --GroupId TencentShenZhenEmployee
```

Output: 
```
{
    "Response": {
        "PersonNum": 2,
        "FaceNum": 2,
        "RequestId": "18fb1e31-0d33-4371-9f41-b1fd59e0c781"
    }
}
```

**Example 2: 获取人员库中人员数量失败示例**



Input: 

```
tccli iai GetPersonListNum --cli-unfold-argument  \
    --GroupId Tencent
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.GroupIdNotExist",
            "Message": "人员库ID不存在。"
        },
        "RequestId": "2865a458-4db1-46bd-ae52-b7507c9f4e62"
    }
}
```

