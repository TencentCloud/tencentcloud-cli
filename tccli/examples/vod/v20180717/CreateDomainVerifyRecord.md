**Example 1: 生成域名解析记录**



Input: 

```
tccli vod CreateDomainVerifyRecord --cli-unfold-argument  \
    --Domain abc.explame.com
```

Output: 
```
{
    "Response": {
        "DNSVerifyInfo": {
            "SubDomain": "_cdnauth",
            "Record": "20241211104123bab0a442ce4c4618209f",
            "RecordType": "TXT"
        },
        "FileVerifyInfo": {
            "FileVerifyUrl": "http://explame.com/verification.html",
            "FileVerifyDomains": [
                "explame.com",
                "abc.explame.com"
            ],
            "FileVerifyName": "verification.html"
        },
        "RequestId": "bffb15f07530b57bc1aabb01fac74bcb"
    }
}
```

