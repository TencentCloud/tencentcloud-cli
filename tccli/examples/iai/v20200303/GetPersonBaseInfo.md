**Example 1: 获取人员基础信息接口**

获取指定人员的信息，包括姓名、性别、人脸等

Input: 

```
tccli iai GetPersonBaseInfo --cli-unfold-argument  \
    --PersonId 1001
```

Output: 
```
{
    "Response": {
        "PersonName": "EvanLiao",
        "Gender": 1,
        "FaceIds": [
            "2873640802022644880",
            "2875186538564559728"
        ],
        "RequestId": "9568a077-0710-40d2-9d6a-b9483d3f2051"
    }
}
```

**Example 2: 错误示例**

人员ID不存在

Input: 

```
tccli iai GetPersonBaseInfo --cli-unfold-argument  \
    --PersonId 1002
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.PersonIdNotExist",
            "Message": "人员ID不存在。"
        },
        "RequestId": "98b4a0bc-802b-4764-9701-bc0c6c544395"
    }
}
```

