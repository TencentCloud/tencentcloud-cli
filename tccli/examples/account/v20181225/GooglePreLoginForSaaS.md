**Example 1: 预登录成功示例**



Input: 

```
tccli account GooglePreLoginForSaaS --cli-unfold-argument  \
    --ClientUA Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 \
    --Platform intlSaaSXXX \
    --Mail XXX@163.com \
    --UserIP 127.0.0.1 \
    --IdToken eyJhbGciOi******Zdet_hLgLJBLuSbNWFAIQAemfdfLt7fMIDyRzmaXysZFzw \
    --ClientType pcweb
```

Output: 
```
{
    "Response": {
        "ExpiredTime": "1745672752",
        "Key": "f63bd2d1358e3847db65daebffb1671d",
        "RequestId": "dfd8ca51-c947-4e31-ab1f-5b9bddbd2050",
        "Sid": "SaaSSid56852cc4-bcc8-7538-ff9d-299aaa6aa68a",
        "Uin": 450200011315
    }
}
```

