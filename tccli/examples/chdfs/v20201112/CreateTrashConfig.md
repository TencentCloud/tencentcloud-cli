**Example 1: 创建chdfs回收站**



Input: 

```
tccli chdfs CreateTrashConfig --cli-unfold-argument  \
    --FileSystemId f14mxo5jafhd \
    --ReservedDays 1 \
    --Status 1 \
    --Path /user/*/.Trash
```

Output: 
```
{
    "Response": {
        "RequestId": "cc6fa375-cd99-478c-aa60-5d582d9276b2"
    }
}
```

