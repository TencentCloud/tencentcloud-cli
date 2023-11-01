**Example 1: 示例**



Input: 

```
tccli drm DescribeDRMLicense --cli-unfold-argument  \
    --DrmType NORMALAES \
    --ContentId jackehantest100 \
    --Tracks SD \
    --ContentType LIVEVIDEO
```

Output: 
```
{
    "Response": {
        "ContentId": "jackehantest100",
        "TXEncryptionToken": "ZW5jTW9kZT0xJmVuY0tleT1lODRlODVmM2JkMjY1Mzg1MDFjZDYyYzM3ZGNmYTBmMyZlbmNJVj03ZjRlNDJiZWYxMTVlZmZhMzM0ZTUyN2VmZDlkODdlMQ==",
        "RequestId": "59fd1904-489c-4e3f-889e-1a384174b79f"
    }
}
```

