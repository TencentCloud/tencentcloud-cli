**Example 1: 获取App隐私诊断上传url**

获取灵鲲app隐私诊断上传url

Input: 

```
tccli acp DescribeFileTicket --cli-unfold-argument  \
    --Source 2 \
    --Platform 0
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxxx",
        "UploadSign": "",
        "Result": 0,
        "FildID": "",
        "UploadUrl": "https://private-7****2.gzc.vod.tencent-cloud.com/52423182d35"
    }
}
```

**Example 2: 获取App隐私诊断文件上传url**



Input: 

```
tccli acp DescribeFileTicket --cli-unfold-argument  \
    --Source 2 \
    --Platform 0
```

Output: 
```
{
    "Response": {
        "RequestId": "79fd20b9-211d-4121-b2ad-1929c047c17e",
        "Result": 0,
        "UploadUrl": "https://evid.urlsec.qq.com/cos?nonce=8340144340601255658&secretId=KLhXXcNBeJVvW4eHCa2RlN6dRkuLx2nL&token=76b936bbfda9e65e837ba7049fe531e3&ts=1641547235",
        "UploadSign": "",
        "FildID": ""
    }
}
```

