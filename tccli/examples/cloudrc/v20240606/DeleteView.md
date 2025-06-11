**Example 1: 删除视图**



Input: 

```
tccli cloudrc DeleteView --cli-unfold-argument  \
    --ViewId vw-6wyborpx
```

Output: 
```
{
    "Response": {
        "RequestId": "7b315598-7273-41d1-ad4f-b6c20f0e9db7"
    }
}
```

**Example 2: 删除不存在的视图**



Input: 

```
tccli cloudrc DeleteView --cli-unfold-argument  \
    --ViewId vw-notexits
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "ResourceNotFound.ViewIdNotFound",
            "Message": "视图ID不存在"
        },
        "RequestId": "5517f978-f57f-471d-83f0-71472ac8b9a6"
    }
}
```

