**Example 1: 返回成功**



Input: 

```
tccli ssl DescribeDownloadCertificateUrl --cli-unfold-argument  \
    --CertificateId sduwd123 \
    --ServiceType nginx
```

Output: 
```
{
    "Response": {
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456",
        "DownloadCertificateUrl": "http://****.zip",
        "DownloadFilename": "****.com_nginx.zip"
    }
}
```

