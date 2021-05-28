**Example 1: 生成解析记录**



Input: 

```
tccli ecdn CreateVerifyRecord --cli-unfold-argument  \
    --Domain www.qq.com
```

Output: 
```
{
    "Response": {
        "RequestId": "8518c99c-a8eb-4930-a7d0-eff586d9cc37",
        "SubDomain": "_cdnauth",
        "Record": "202009071516044acd018wf498457628cn75ba018ec9cv",
        "RecordType": "TXT"
    }
}
```

