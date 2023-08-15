**Example 1: 删除人员接口**

删除指定人员信息

Input: 

```
tccli iai DeletePerson --cli-unfold-argument  \
    --PersonId 2001
```

Output: 
```
{
    "Response": {
        "RequestId": "4b609b7c-7a9a-4ea0-be8b-1fb638c2ceca"
    }
}
```

**Example 2: 错误示例**

人员ID不存在

Input: 

```
tccli iai DeletePerson --cli-unfold-argument  \
    --PersonId 3001
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "ResourceNotFound.ErrorPersonNotExisted",
            "Message": "个体不存在。"
        },
        "RequestId": "4b9c1bdc-86eb-413f-8c74-15bcf4466cd5"
    }
}
```

