**Example 1: 创建共享CNAME**

创建共享CNAME

Input: 

```
tccli teo CreateSharedCNAME --cli-unfold-argument  \
    --SharedCNAMEPrefix test \
    --ZoneId zone-225qgrnvbi9w \
    --Description 用于业务A场景
```

Output: 
```
{
    "Response": {
        "SharedCNAME": "test.225qgrnvbi9w.share.eo.dnse1.com",
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707"
    }
}
```

