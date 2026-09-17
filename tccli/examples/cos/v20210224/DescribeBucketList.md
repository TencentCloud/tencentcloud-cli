**Example 1: 正常结构**



Input: 

```
tccli cos DescribeBucketList --cli-unfold-argument  \
    --Limit 3 \
    --NextToken direct-ofs-maz-billing-bandwidth-quota-1251668577
```

Output: 
```
{
    "Response": {
        "Data": {
            "Buckets": [
                {
                    "AppId": 1251668577,
                    "Bucket": "direct-ofs-saz-billing-bandwidth-quota",
                    "CreateTime": "2024-08-19T11:54:12+08:00",
                    "Uin": "2779643970"
                }
            ],
            "Count": 3,
            "NextToken": "adcd-static-gjihgjncgyfhtvhv-4fh0foredc03e79-1300041554"
        },
        "RequestId": "3696dd0b-7118-4864-9367-93ab63a00265"
    }
}
```

