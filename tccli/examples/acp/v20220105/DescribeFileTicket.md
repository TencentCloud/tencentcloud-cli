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
        "UploadUrl": "https://private-7****2.gz***d.tence***d.com/524***d35"
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
        "UploadUrl": "https://evi***c.qq.com/cos?nonce=8340****06012***58&secretId=K***NBeJ****HCa2RlN6dL&token=76b93***837ba70***1e3&ts=164***35",
        "UploadSign": "",
        "FildID": ""
    }
}
```

