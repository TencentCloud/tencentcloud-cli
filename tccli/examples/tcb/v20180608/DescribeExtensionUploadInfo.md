**Example 1: 获取上次文件的信息**



Input: 

```
tccli tcb DescribeExtensionUploadInfo --cli-unfold-argument  \
    --ExtensionFiles.0.FileType FUNCTION \
    --ExtensionFiles.0.FileName myfilename
```

Output: 
```
{
    "Response": {
        "FilesData": [
            {
                "CodeUri": "extension://ba883a90xxxxx.zip",
                "UploadUrl": "https://cloudaccess-code-123.cos.ap-shanghai.myqcloud.com/home%2Fz0anckEI.zip?sign=q-sign-algorithm%aa",
                "CustomKey": "xxxx",
                "MaxSize": 15
            }
        ],
        "RequestId": "d691f154-c2d5-4f48-833a-a408cdaadd9c"
    }
}
```

