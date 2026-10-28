**Example 1: UpdateUserQuota**



Input: 

```
tccli goosefs UpdateUserQuota --cli-unfold-argument  \
    --FileSystemId x-c60-4lu862qo \
    --QuotaId quota_1754029660656 \
    --QuotaSizeLimit 20G \
    --QuotaFilesLimit 500000
```

Output: 
```
{
    "Response": {
        "RequestId": "cc66d787-9919-4bba-9ed7-ccd94812939e"
    }
}
```

