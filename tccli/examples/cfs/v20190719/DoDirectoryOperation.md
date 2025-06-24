**Example 1: 文件系统目录操作接口**

用于部分类型的文件系统目录操作

Input: 

```
tccli cfs DoDirectoryOperation --cli-unfold-argument  \
    --FileSystemId cfs-12345 \
    --OpetationType create \
    --DirectoryPath /user1/dir1/ \
    --Mode 0644
```

Output: 
```
{
    "Response": {
        "RequestId": "fjo8aejo-fjei-32eu-2je9-fhue83nd81",
        "Result": 1
    }
}
```

