**Example 1: 查询Fileset通用配置**

查询Fileset通用配置

Input: 

```
tccli goosefs DescribeFilesetGeneralConfig --cli-unfold-argument  \
    --FileSystemId x-c60-gq019g3k
```

Output: 
```
{
    "Response": {
        "EnforceQuotaOnRoot": "yes",
        "RequestId": "ccec6e4e-0775-4af5-966c-788fa3215bd2",
        "Status": "active"
    }
}
```

