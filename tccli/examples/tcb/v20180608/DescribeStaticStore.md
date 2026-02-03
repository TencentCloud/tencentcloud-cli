**Example 1: 查询静态托管资源状态**



Input: 

```
tccli tcb DescribeStaticStore --cli-unfold-argument  \
    --EnvId lotestapi100004
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "EnvId": "test-dfd",
                "CdnDomain": "test-fdfd-wretndg_fdadg",
                "Bucket": "test-dfdned-fd",
                "Region": "ap-shanghai",
                "Status": "online"
            }
        ],
        "RequestId": "5620b49e-a25a-4007-84ef-03c9035c584d"
    }
}
```

