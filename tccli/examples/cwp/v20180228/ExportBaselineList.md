**Example 1: 基线列表导出接口**

导出列表信息或者详情信息

Input: 

```
tccli cwp ExportBaselineList --cli-unfold-argument  \
    --IfDetail 1
```

Output: 
```
{
    "Response": {
        "DownloadUrl": "https://cwp-1258344699.cos.ap-guangzhou.myqcloud.com/1256299843%2FbaselineDetailList-1b7649c2-d39f-44a1-8689-317b63054095.csv?q-sign-algorithm=sha1&q-ak=AKIDQftteKC6DFvMXWFlSQPB6w9E5fuEmacK&q-sign-time=1631520971%3B1631524571&q-key-time=1631520971%3B1631524571&q-header-list=host&q-url-param-list=&q-signature=3ecf2bdc85fa6908e2da0980e5eb0f0f47299660",
        "RequestId": "123456789",
        "TaskId": "123"
    }
}
```

