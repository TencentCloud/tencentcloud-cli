**Example 1: 开通专业版应用存储**

开通专业版应用重庆地域存储。

Input: 

```
tccli vod CreateStorage --cli-unfold-argument  \
    --SubAppId 1020304056 \
    --StorageRegion ap-chongqing \
    --StorageName my-storage
```

Output: 
```
{
    "Response": {
        "BucketId": "bucketid123",
        "RequestId": "f13e691e-8df1-demo-b734-ac63af4b9a64"
    }
}
```

