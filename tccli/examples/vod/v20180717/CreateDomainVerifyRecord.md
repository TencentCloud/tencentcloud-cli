**Example 1: 生成域名解析记录**



Input: 

```
tccli vod CreateDomainVerifyRecord --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "DNSVerifyInfo": {
            "SubDomain": "abc",
            "Record": "abc",
            "RecordType": "abc"
        },
        "FileVerifyInfo": {
            "FileVerifyUrl": "abc",
            "FileVerifyDomains": [
                "abc"
            ],
            "FileVerifyName": "abc"
        },
        "RequestId": "abc"
    }
}
```

