**Example 1: 更新**



Input: 

```
tccli cdwdoris UpdateDatabase --cli-unfold-argument  \
    --InstanceId cdwdoris-7da9fumk \
    --DbName demo1 \
    --Operation SET_QUOTA \
    --Quota 10T \
    --CatalogName internal
```

Output: 
```
{
    "Response": {
        "Success": true,
        "Message": "Database quota set successfully.",
        "RequestId": "xxxx-xxxx-xxxx-xxxx"
    }
}
```

