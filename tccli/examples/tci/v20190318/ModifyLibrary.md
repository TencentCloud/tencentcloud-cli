**Example 1: 修改人员库名称**

修改人员库名称

Input: 

```
tccli tci ModifyLibrary --cli-unfold-argument  \
    --LibraryName xxx \
    --LibraryId libraryid_xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "cee066ee-ffff-4a95-ad04-577de598544f",
        "LibraryName": "xxx",
        "LibraryId": "library_155299991460001667993"
    }
}
```

