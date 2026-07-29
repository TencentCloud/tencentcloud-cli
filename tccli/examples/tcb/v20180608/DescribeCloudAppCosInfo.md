**Example 1: 查询云应用cos信息**



Input: 

```
tccli tcb DescribeCloudAppCosInfo --cli-unfold-argument  \
    --EnvId env-xxx01 \
    --ServiceName vue \
    --DeployType static-hosting \
    --UnixTimestamp 1709500000 \
    --Suffix .zip \
    --NeedDownload False
```

Output: 
```
{
    "Response": {
        "DownloadHeaders": [],
        "DownloadUrl": "https://xxx.cos.xxxx.myqcloud.com/xxx/static.zip?q-signature=xxxxxxxxxxx01sjjdhsd1190",
        "UnixTimestamp": "1709500000",
        "UploadHeaders": [],
        "UploadUrl": "https://xxx.cos.xxxx.myqcloud.com/home/xxxx/static-0a94df-react-xxxx.zip?q-sign-algorithm=sha1&q-ak=xxxxxxx&q-sign-time=xxxxxx&q-key-time=177xxxxx&q-header-list=host&q-url-param-list=&q-signature=xxxxxxxxxxx01sjjdhsd1190",
        "RequestId": "08c88424-ce2c-4fa5-9306-a442307fba46"
    }
}
```

