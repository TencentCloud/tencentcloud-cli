**Example 1: 资源管理-批量删除资源**

批量删除资源

Input: 

```
tccli wedata DeleteResourceFiles --cli-unfold-argument  \
    --ProjectId abc \
    --ResourceIds abc \
    --FilePaths abc \
    --UseStatus True
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "abc"
    }
}
```

