**Example 1: 查询实例SSL状态**

查询实例SSL状态

Input: 

```
tccli cynosdb DescribeSSLStatus --cli-unfold-argument  \
    --ClusterId cynosdbmysql-jd510000 \
    --InstanceId cynosdbmysql-ins-906n0000
```

Output: 
```
{
    "Response": {
        "DownloadUrl": "download_url",
        "IsOpenSSL": "yes",
        "RequestId": "baa4f39e-47c0-4400-bff2-1d6062b70748"
    }
}
```

