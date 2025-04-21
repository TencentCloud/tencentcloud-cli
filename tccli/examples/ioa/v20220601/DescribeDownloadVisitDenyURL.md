**Example 1: 示例1**

示例1

Input: 

```
tccli ioa DescribeDownloadVisitDenyURL --cli-unfold-argument  \
    --StartTime 1683703604000 \
    --EndTime 1685431604000 \
    --DenyAddrTopReq.From 0 \
    --DenyAddrTopReq.Size 10 \
    --DenyAddrTopReq.Sort desc \
    --DenyAppTopReq.From 0 \
    --DenyAppTopReq.Size 10 \
    --DenyAppTopReq.Sort desc \
    --DenyClientTopReq.From 0 \
    --DenyClientTopReq.Size 10 \
    --DenyClientTopReq.Sort desc
```

Output: 
```
{
    "Response": {
        "Data": {
            "DownloadToken": "",
            "DownloadURL": "https://ioa-yundun-dev-1-1258344699.cos.ap-guangzhou.myqcloud.com/1300055730/tmp/logcenter1302d7643c090ef5dffc92e359fe5ae4.csv?q-sign-algorithm=sha1&q-ak=AKIDf9PPAfv0qQs8BzXsxnNincCWbQzJNDo9&q-sign-time=1684316836%3B1686908836&q-key-time=1684316836%3B1686908836&q-header-list=host&q-url-param-list=&q-signature=73c84f20c71428fbb067c4b1aff98746d0566f2e",
            "ExpireAt": ""
        },
        "RequestId": "22349ee3-77fb-497c-8826-8676143fdc2b"
    }
}
```

**Example 2: DescribeDownloadVisitDenyURL**

DescribeDownloadVisitDenyURL

Input: 

```
tccli ioa DescribeDownloadVisitDenyURL --cli-unfold-argument  \
    --StartTime 1 \
    --EndTime 1 \
    --DenyAddrTopReq.From 1 \
    --DenyAddrTopReq.Size 1 \
    --DenyAddrTopReq.Sort 1 \
    --DenyAppTopReq.From 1 \
    --DenyAppTopReq.Size 1 \
    --DenyAppTopReq.Sort 1 \
    --DenyClientTopReq.From 1 \
    --DenyClientTopReq.Size 1 \
    --DenyClientTopReq.Sort 1 \
    --Department 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "AuthFailure.SignatureFailure",
            "Message": "请求签名验证失败，请检查您的签名计算是否正确。"
        },
        "RequestId": "8d84e512-dba9-49c2-bd71-eb8fa8c42a8f"
    }
}
```

