**Example 1: 错误示例**

人员库ID不存在

Input: 

```
tccli iai GetPersonListNum --cli-unfold-argument  \
    --GroupId Tencent \
    --Version 2018-03-01
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

**Example 2: 获取人员列表长度接口**

获取指定人员库中人员数量

Input: 

```
tccli iai GetPersonListNum --cli-unfold-argument  \
    --GroupId TencentShenZhenEmployee \
    --Version 2018-03-01
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

