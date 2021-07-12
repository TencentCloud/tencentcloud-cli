**Example 1: 设置自动续费标志**



Input: 

```
tccli cynosdb SetRenewFlag --cli-unfold-argument  \
    --ResourceIds cynosdbmysql-ins-xxxxxxx \
    --AutoRenewFlag 1
```

Output: 
```
{
    "Response": {
        "Count": 1,
        "RequestId": 123123123
    }
}
```

