**Example 1: 设置域名的 Key 防盗链**



Input: 

```
tccli vod ModifyVodDomainConfig --cli-unfold-argument  \
    --Domain myexample.com \
    --UrlSignatureAuthPolicy.Status Enabled \
    --UrlSignatureAuthPolicy.EncryptedKey xxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4551-9d4b-5594145287e1"
    }
}
```

