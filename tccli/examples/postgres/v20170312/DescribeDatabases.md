**Example 1: Pulling database list**



Input: 

```
tccli postgres DescribeDatabases --cli-unfold-argument  \
    --DBInstanceId postgres-6bwgamo3
```

Output: 
```
{
    "Response": {
        "RequestId": "86eb714c-500f-412e-8090-3b3f76843d86",
        "Items": [
            "postgres",
            "testdatabase"
        ]
    }
}
```

