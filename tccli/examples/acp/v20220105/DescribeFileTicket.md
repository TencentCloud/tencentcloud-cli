**Example 1: 获取App隐私诊断上传url**

获取app隐私诊断上传url

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
        "UploadUrl": "https://priva***d35"
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
        "UploadUrl": "https://evi***s?non***58&secr***N6dL&token=76b***1e3&ts=164***35",
        "UploadSign": "",
        "FildID": ""
    }
}
```

