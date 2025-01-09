**Example 1: 调用示例**



Input: 

```
tccli aiart QueryMemeJob --cli-unfold-argument  \
    --JobId 251197749-1736402968-49025b63-ce50-11ef-9ce4-5254006b9705-0
```

Output: 
```
{
    "Response": {
        "JobErrorCode": "",
        "JobErrorMsg": "",
        "JobStatusCode": "5",
        "JobStatusMsg": "处理完成",
        "RequestId": "df0717c3-508e-4ba7-8537-e22500cf144c",
        "ResultImage": "https://aiart-xxx.cos.ap-guangzhou.myqcloud.com/xxx.jpg?q-sign-algorithm=sha1&q-ak=xxxxx&q-sign-time=1731574045;1731577645&q-key-time=1731574045;1731577645&q-header-list=host&q-url-param-list=&q-signature=31fe75c1c18c3d91db59508961209dd37aaf41c7"
    }
}
```

