**Example 1: ListApp**

获取企业下应用列表

Input: 

```
tccli lke ListApp --cli-unfold-argument  \
    --AppType knowledge_qa
```

Output: 
```
{
    "Response": {
        "Total": "1",
        "List": [
            {
                "AppType": "abc",
                "AppTypeDesc": "abc",
                "AppBizId": "abc",
                "Name": "abc",
                "Avatar": "abc",
                "Desc": "abc",
                "AppStatus": 1,
                "AppStatusDesc": "abc",
                "UpdateTime": "abc",
                "Operator": "abc",
                "ModelName": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

