**Example 1: 设置自动续费标识**



Input: 

```
tccli lighthousedb SetRenewFlag --cli-unfold-argument  \
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

