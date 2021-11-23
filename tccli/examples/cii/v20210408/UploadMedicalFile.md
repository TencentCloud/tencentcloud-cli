**Example 1: 上传医疗影像文件接口示例**



Input: 

```
tccli cii UploadMedicalFile --cli-unfold-argument  \
    --FileURL https://dss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/searchbox/nicon-2x-6258e1cf13.png
```

Output: 
```
{
    "Response": {
        "RequestId": "9317f6e4-6636-41a0-bf24-89ad9e4877f2",
        "FileKey": "6540556601/original_upload_dir/6540556601_9317f6e4-6636-41a0-bf24-89ad9e4877f2.png"
    }
}
```

