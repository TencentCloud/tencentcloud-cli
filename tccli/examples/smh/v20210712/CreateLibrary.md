**Example 1: 创建媒体库**

创建媒体库

Input: 

```
tccli smh CreateLibrary --cli-unfold-argument  \
    --Name 测试媒体库 \
    --LibraryExtension.IsFileLibrary True \
    --LibraryExtension.IsMultiSpace True
```

Output: 
```
{
    "Response": {
        "AccessDomain": "smh3etdq8gpi2201.api.tencentmsh.cn",
        "LibraryId": "smh3etdq8gpi2201",
        "RequestId": "5cc1bd23-8ff1-4f7a-86f9-640c97266c15"
    }
}
```

