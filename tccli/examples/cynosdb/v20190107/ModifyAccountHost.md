**Example 1: 修改账号主机**

修改账号主机

Input: 

```
tccli cynosdb ModifyAccountHost --cli-unfold-argument  \
    --ClusterId abc \
    --NewHost abc \
    --Account.AccountName abc \
    --Account.Host abc
```

Output: 
```
{
    "Response": {
        "RequestId": "128046"
    }
}
```

