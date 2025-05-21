**Example 1: 创建FIleset**

创建FIleset

Input: 

```
tccli goosefs CreateFileset --cli-unfold-argument  \
    --FileSystemId x-c60-gq019g3k \
    --FsetName fset_test_006 \
    --FsetDir /fset_test_006/ \
    --QuotaSizeLimit 1024G \
    --QuotaFilesLimit 1024 \
    --AuditState enable
```

Output: 
```
{
    "Response": {
        "FsetId": "fset_1745742041947",
        "RequestId": "1c44ae43-f00d-460f-a093-469c407b6fb5"
    }
}
```

