**Example 1: 失败**

资源不存在

Input: 

```
tccli iss UpdateOrganization --cli-unfold-argument  \
    --OrganizationId 2000 \
    --Name 二级目录3
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "ResourceNotFound",
            "Message": "该资源不存在"
        },
        "RequestId": "0cb4f4cc-7968-49f2-82a0-10a3390971c6"
    }
}
```

**Example 2: 成功**

 

Input: 

```
tccli iss UpdateOrganization --cli-unfold-argument  \
    --OrganizationId 193 \
    --Name cloudapi5-new1
```

Output: 
```
{
    "Response": {
        "Data": {
            "AppId": 1300000000,
            "OrganizationId": "111111",
            "Level": 1,
            "Name": "cloudapi5-new1",
            "Online": 0,
            "ParentId": "0",
            "ParentIds": "0",
            "Total": 0
        },
        "RequestId": "3f588654-5b70-4ce5-a2e3-2a1596eb7c92"
    }
}
```

