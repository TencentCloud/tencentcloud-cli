**Example 1: 上传证书吊销确认函**



Input: 

```
tccli ssl UploadRevokeLetter --cli-unfold-argument  \
    --CertificateId a91hoLqi \
    --RevokeLetter base64content
```

Output: 
```
{
    "Response": {
        "RequestId": "15dc3823-4089-4fd6-81a6-ec8baf5ec330",
        "CertificateId": "a91hoLqi",
        "IsSuccess": true
    }
}
```

