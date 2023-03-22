**Example 1: 生成解析记录**

正常回包

Input: 

```
tccli cdn CreateVerifyRecord --cli-unfold-argument  \
    --Domain www.qq.com
```

Output: 
```
{
    "Response": {
        "RequestId": "8518c99c-a8eb-4930-a7d0-eff586d9cc37",
        "SubDomain": "_cdnauth",
        "Record": "202009071516044acd018wf498457628cn75ba018ec9cv",
        "RecordType": "TXT",
        "FileVerifyUrl": "http://abc.com/verification.html",
        "FileVerifyDomains": [
            "abc.com"
        ],
        "FileVerifyName": "verification.html"
    }
}
```

