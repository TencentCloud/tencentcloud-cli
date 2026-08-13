**Example 1: 获取导出下载链接接口**



Input: 

```
tccli csip DescribeEdrExportJobDownloadURL --cli-unfold-argument  \
    --JobId 3a419bbc-780b-4e8d-882a-9493b4473608
```

Output: 
```
{
    "Response": {
        "DownloadUrl": "https://*os.ap-guangzhou.myqcloud.com/*unjing-dev-1256299843/all-exp*rt/edr-alert/260108008/260108*08-edr-alert-20260513-1.xlsx?**Amz-Algorithm=AWS4-HMAC-SHA2*6&X-Amz-Credential=AKIDHMGvOb*QyHLDqIdVEixxkIdjZAVbJ7Yn%2F**260513%2Fap-guangzhou%2Fs3%**aws4_request&X-Amz-Date=202*0513T063236Z&X-Amz-Expires=7200&X-Amz-SignedHeaders=host&response-content-disposition=attachment&X-Amz-Signature=12918abedd1eee40cb29be2f21b809c1cd2b8744381fb3455c31a8353ca64a6a",
        "FileName": "260108008-edr-alert-20260513-1.xlsx",
        "RequestId": "02ed7fda-a617-4e82-895d-708509ca638c"
    }
}
```

