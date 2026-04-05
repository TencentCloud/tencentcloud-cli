**Example 1: 列出COS桶列表**



Input: 

```
tccli wedata ListCosBuckets --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "Buckets": [
                {
                    "CreationDate": "Sun Oct 26 00:31:41 CST 2025",
                    "Location": "ap-guangzhou",
                    "Name": "bucket-30-251436191",
                    "Owner": "700002164618"
                },
                {
                    "CreationDate": "Wed Nov 05 11:25:04 CST 2025",
                    "Location": "ap-guangzhou",
                    "Name": "wedata30-mlflow-251436191",
                    "Owner": "700002164618"
                }
            ]
        },
        "RequestId": "e10cc5d9-6d41-4050-9ddf-61bf59673efc"
    }
}
```

