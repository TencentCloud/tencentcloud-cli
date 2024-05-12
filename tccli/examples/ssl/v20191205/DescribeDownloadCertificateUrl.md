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
        "RequestId": "xxx-xxx-xxx-xxx",
        "DownloadCertificateUrl": "http://xxx.zip",
        "DownloadFilename": "xxx.com_nginx.zip"
    }
}
```

