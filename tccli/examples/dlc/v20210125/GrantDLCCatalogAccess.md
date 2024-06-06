**Example 1: 授权访问DLC元数据**

授权访问DLC元数据

Input: 

```
tccli dlc GrantDLCCatalogAccess --cli-unfold-argument  \
    --VpcId vpc-1234 \
    --Product EMR \
    --Description EMR生产集群
```

Output: 
```
{
    "Response": {
        "RequestId": "1234-4567"
    }
}
```

