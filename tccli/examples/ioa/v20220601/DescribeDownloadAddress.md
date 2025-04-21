**Example 1: DescribeDownloadAddress**



Input: 

```
tccli ioa DescribeDownloadAddress --cli-unfold-argument  \
    --OsType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "b4820dd8-cb40-40fc-bfbf-f77ceee7bd8d",
        "Data": {
            "WeakPasswordDownloadUrl": "https://dev.scs.gateway.tencent.com/store/CommonResource/TemplateFile/弱密码模板.txt"
        }
    }
}
```

