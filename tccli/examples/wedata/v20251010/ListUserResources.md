**Example 1: ListUserResources**

查询用户资源列表，移除用户时使用

Input: 

```
tccli wedata ListUserResources --cli-unfold-argument  \
    --SubUin 700002196961 \
    --WorkspaceId 17621416814092400 \
    --PageRequest.PageNumber 1 \
    --PageRequest.PageSize 5
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [],
            "PageResponse": {
                "PageNumber": 1,
                "PageSize": 5,
                "TotalCount": 0,
                "TotalPageNumber": 0
            }
        },
        "RequestId": "ca0e5de1-b994-4555-b881-5046eb9a9b18"
    }
}
```

