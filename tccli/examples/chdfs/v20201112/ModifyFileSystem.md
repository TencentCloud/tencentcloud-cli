**Example 1: 修改文件系统属性**

修改文件系统属性

Input: 

```
tccli chdfs ModifyFileSystem --cli-unfold-argument  \
    --FileSystemId f4mhaqkciq0 \
    --FileSystemName test \
    --Description test \
    --CapacityQuota 1073741824
```

Output: 
```
{
    "Response": {
        "RequestId": "61046a25-2eda-4495-b9b6-eab6edf41d79"
    }
}
```

