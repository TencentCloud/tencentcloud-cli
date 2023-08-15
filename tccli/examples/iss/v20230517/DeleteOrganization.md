**Example 1: 成功**

 

Input: 

```
tccli iss DeleteOrganization --cli-unfold-argument  \
    --OrganizationId 193
```

Output: 
```
{
    "Response": {
        "RequestId": "cba701a7-608d-4785-a1d0-c45a2ec07a26"
    }
}
```

**Example 2: 组织不存在错误**

 

Input: 

```
tccli iss DeleteOrganization --cli-unfold-argument  \
    --OrganizationId 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "ResourceNotFound",
            "Message": "该资源不存在"
        },
        "RequestId": "4798f503-9cdb-418f-ad69-2d5632cff6b3"
    }
}
```

