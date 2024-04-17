**Example 1: 资源管理-批量删除资源**

批量删除资源

Input: 

```
tccli wedata DeleteResourceFiles --cli-unfold-argument  \
    --ProjectId 1470575647377821987 \
    --ResourceIds 7a4267f0-d7b0-4563-b4b4-34ac3291e488 \
    --FilePaths /datastudio/resource/demo/demo.zip \
    --UseStatus True
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "77b63b69-b3c5-48ea-809e-d1bbfc1b3da0"
    }
}
```

