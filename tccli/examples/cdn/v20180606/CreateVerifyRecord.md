**Example 1: 生成解析记录**



Input: 

```
tccli cdn CreateVerifyRecord --cli-unfold-argument  \
    --Domain www.qq.com
```

Output: 
```
{
    "Response": {
        "RequestId": "b6926bb2-d0b5-42bc-b17f-e4402bdb9e9b",
        "Record": {
            "SubDomain": "_cdnauth",
            "Record": "20191225190958a7c80465432ff68a58d359e28ee6390f",
            "RecordType": "TXT"
        }
    }
}
```

