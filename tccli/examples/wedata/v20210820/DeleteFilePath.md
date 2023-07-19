**Example 1: 开发空间-批量删除目录和文件**

开发空间-批量删除目录和文件

Input: 

```
tccli wedata DeleteFilePath --cli-unfold-argument  \
    --ProjectId 1486804694126882816 \
    --ResourceIds 5b4a1a4c-4e8c-4a0b-a952-29fb417d84b9 \
    --UseStatus true
```

Output: 
```
{
    "Response": {
        "RequestId": "0487b757-35ab-4853-9d8f-6c39bd24f28c",
        "UserFileList": []
    }
}
```

