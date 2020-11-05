**Example 1: Initializing one instance**

This example shows you how to initialize the instance whose ID is postgres-6fego161

Input: 

```
tccli postgres InitDBInstances --cli-unfold-argument  \
    --DBInstanceIdSet postgres-6fego161\
    --AdminName testuser\
    --AdminPassword testuser%40123\
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

**Example 2: Initializing multiple instances**

This example shows you how to simultaneously initialize two instances whose IDs are postgres-6fego161 and postgres-lnp6j617 respectively

Input: 

```
tccli postgres InitDBInstances --cli-unfold-argument  \
    --Version 2017-03-12\
    --Region ap-guangzhou\
    --DBInstanceIdSet postgres-6fego161 postgres-lnp6j617\
    --AdminName testuser\
    --AdminPassword testuser%40123\
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

