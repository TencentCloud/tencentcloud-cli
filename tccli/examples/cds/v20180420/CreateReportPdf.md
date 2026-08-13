**Example 1: 下载报表PDF**

下载报表PDF

Input: 

```
tccli cds CreateReportPdf --cli-unfold-argument  \
    --Id 0
```

Output: 
```
{
    "Response": {
        "Url": "https://regionid.cds.tencent.com/path/数据安全审计报表_周期_语句_yyyyMMdd_hhmm.pdf?q-sign-algorithm=sha1&q-ak=AK_xxx&q-sign-time=timestamp;timestamp&q-key-time=timestamp;1730430057&q-header-list=host&q-url-param-list=&q-signature=7c86df8edf4b8ec8ac5b632f689295b18e0f3117",
        "RequestId": "8ad5a3f5-fd37-4d77-8448-ab680d513500"
    }
}
```

