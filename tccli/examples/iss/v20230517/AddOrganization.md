**Example 1: 成功1**

 

Input: 

```
tccli iss AddOrganization --cli-unfold-argument  \
    --Name 云api3-5 \
    --ParentId 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "AppId": 13000000001,
            "OrganizationId": "193",
            "Level": 1,
            "Name": "云api3-5",
            "Online": 0,
            "ParentId": "0",
            "ParentIds": "0",
            "Total": 0
        },
        "RequestId": "6243deef-a87a-4d5e-8c71-2ca237520df7"
    }
}
```

**Example 2: 父组织不存在错误**

 

Input: 

```
tccli iss AddOrganization --cli-unfold-argument  \
    --Name 云api3-6 \
    --ParentId ***
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "ResourceNotFound",
            "Message": "该资源不存在"
        },
        "RequestId": "df1d71c3-2389-4f04-9db8-36108be0c915"
    }
}
```

**Example 3: 组织名称重复错误**

 

Input: 

```
tccli iss AddOrganization --cli-unfold-argument  \
    --Name 云api3-5 \
    --ParentId ***
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.OrgNameRepeat",
            "Message": "组织名称不能重复"
        },
        "RequestId": "4847e307-e6ac-47b1-b6f8-bea39a66c8a9"
    }
}
```

