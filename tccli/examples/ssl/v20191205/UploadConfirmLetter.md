**Example 1: 上传证书确认函**



Input: 

```
tccli ssl UploadConfirmLetter --cli-unfold-argument  \
    --CertificateId flSFd6Fh \
    --ConfirmLetter UEsDBBQABgAIAAAAIQCM19MmCg......
```

Output: 
```
{
    "Response": {
        "RequestId": "15dc3823-4089-4fd6-81a6-ec8baf5ec330",
        "CertificateId": "flSFd6Fh",
        "IsSuccess": true
    }
}
```

