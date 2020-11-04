**Example 1: 获取文件下载信息**

获取文件下载信息

Input: 

```
tccli tcb DescribeDownloadFile --cli-unfold-argument  \
    --CodeUri "abc.zip"
```

Output: 
```
{
    "Response": {
        "FilesData": [
            {
                "DownloadUrl": "https://cloudaccess-code-1258016615.cos.ap-shanghai.myqcloud.com/home%2F4ac1fc8cf53d4211991b65600d854456%2Fhuming-mp.zip_1597925893_z0anckEI.zip?sign=q-sign-algorithm%aa",
                "CustomKey": "5umhWq1gNR4kYOP3KXgY3lmhFlllutgb",
                "FilePath": "file"
            }
        ],
        "RequestId": "d691f154-c2d5-4f48-833a-a408cdaadd9c"
    }
}
```

