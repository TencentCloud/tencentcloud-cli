**Example 1: 修改账号主机**



Input: 

```
tccli cynosdb ModifyAccountHost --cli-unfold-argument  \
    --ClusterId cynosdbpg-on5xw0ni \
    --Account.AccountName admin \
    --Account.Host myHost \
    --NewHost xx
```

Output: 
```
{
    "Response": {
        "RequestId": "128046"
    }
}
```

