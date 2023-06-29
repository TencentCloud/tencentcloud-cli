**Example 1: 隔离一个同步任务**

隔离一个正在计费的同步任务

Input: 

```
tccli dts IsolateSyncJob --cli-unfold-argument  \
    --JobId sync-kl5qyyf4
```

Output: 
```
{
    "Response": {
        "RequestId": "df239e4f-7359-473b-a073-144ab9964350"
    }
}
```

