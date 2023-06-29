**Example 1: 查询媒体库密钥**



Input: 

```
tccli smh DescribeLibrarySecret --cli-unfold-argument  \
    --LibraryId smh1jjexrwwoa9ok
```

Output: 
```
{
    "Response": {
        "LibraryId": "smh1jjexrwwoa9ok",
        "LibrarySecret": "5563cadd2dc2ad56********************************cb6a5d8abec16490",
        "RequestId": "61f8e8a2-964a-49d3-ad85-12f29d79ac23"
    }
}
```

