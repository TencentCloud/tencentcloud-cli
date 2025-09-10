**Example 1: 导出软件信息列表**



Input: 

```
tccli ioa ExportSoftwareInformationList --cli-unfold-argument  \
    --Mid 1
```

Output: 
```
{
    "Response": {
        "RequestId": "0c1f66e2-90aa-4253-8e32-4abddb044170",
        "Data": {
            "DownloadURL": "https://ioa-dev-1-1258344699.cos-internal.ap-guangzhou.tencentcos.cn/software-open-api/software/ygM3Vgff7j-%E8%BD%AF%E4%BB%B6%E7%BB%9F%E8%AE%A1-%E6%8C%89%E7%BB%88%E7%AB%AF%E6%9F%A5%E7%9C%8B-%E8%BD%AF%E4%BB%B6%E5%88%97%E8%A1%A82022-11-10%2018%3A15%3A07.csv?q-sign-algorithm=sha1&q-ak=AKID******&q-sign-time=1668075307%3B1668078907&q-key-time=1668075307%3B1668078907&q-header-list=host&q-url-param-list=&q-signature=9b2cf4e463a138d9b29dcee9aceb1e21aa8ecffd"
        }
    }
}
```

**Example 2: 测试下载**

测试下载

Input: 

```
tccli ioa ExportSoftwareInformationList --cli-unfold-argument  \
    --Mid 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "DownloadURL": "http://xxx",
            "TaskId": 0
        },
        "RequestId": "e36ff231-6bbc-475d-9e26-dd0d59260b55"
    }
}
```

