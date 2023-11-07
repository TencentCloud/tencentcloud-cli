**Example 1: 创建共享 CNAME**

在 ZoneId 为 zone-225qgrnvbi9w 的站点下，创建一个共享 CNAME 前缀为 test，描述为 For Service A 的共享 CNAME。

Input: 

```
tccli teo CreateSharedCNAME --cli-unfold-argument  \
    --SharedCNAMEPrefix test \
    --ZoneId zone-225qgrnvbi9w \
    --Description For Service A
```

Output: 
```
{
    "Response": {
        "SharedCNAME": "test.225qgrnvbi9w.share.dnse1.com",
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707"
    }
}
```

