**Example 1: 设置cos跨域请求**

设置cos跨域请求

Input: 

```
tccli gse UpdateBucketCORSOpt --cli-unfold-argument  \
    --AllowedOrigins * \
    --AllowedMethods GET \
    --AllowedHeaders x-cos-meta-test
```

Output: 
```
{
    "Response": {
        "RequestId": "s1609831145190946000"
    }
}
```

