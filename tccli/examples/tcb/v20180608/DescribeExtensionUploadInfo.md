**Example 1: 示例一**



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
                "UploadUrl": "https://cloudaccess-code-1258016615.cos.ap-shanghai.myqcloud.com/home%2F4ac1fc8cf53d4211991b65600d854456%2Fhuming-mp.zip_1597925893_z0anckEI.zip?sign=q-sign-algorithm%aa",
                "CustomKey": "5umhWq1gNR4kYOP3KXgY3lmhFlllutgb",
                "MaxSize": 15
            }
        ],
        "RequestId": "d691f154-c2d5-4f48-833a-a408cdaadd9c"
    }
}
```

