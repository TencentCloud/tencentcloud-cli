**Example 1: 初始化单个实例**

例如：初始化的实例Id为: postgres-6fego161

Input: 

```
tccli postgres InitDBInstances --cli-unfold-argument  \
    --DBInstanceIdSet postgres-6fego161 \
    --AdminName testuser \
    --AdminPassword testuser%40123 \
    --Charset UTF8
```

Output: 
```
{
    "Response": {
        "RequestId": "98fe67de-f7a7-4285-b1f2-40c2a2a3495e",
        "DBInstanceIdSet": [
            "postgres-6fego161"
        ]
    }
}
```

**Example 2: 初始化多个实例**

例如：同时初始化2个实例，实例Id分别为：postgres-6fego161、postgres-lnp6j617

Input: 

```
tccli postgres InitDBInstances --cli-unfold-argument  \
    --Version 2017-03-12 \
    --Region ap-guangzhou \
    --DBInstanceIdSet postgres-6fego161 postgres-lnp6j617 \
    --AdminName testuser \
    --AdminPassword testuser%40123 \
    --Charset UTF8
```

Output: 
```
{
    "Response": {
        "RequestId": "5b895b34-5448-4c55-9ad1-a61427c15837",
        "DBInstanceIdSet": [
            "postgres-6fego161",
            "postgres-lnp6j617"
        ]
    }
}
```

