**Example 1: Creating an instance account**



Input: 

```
tccli sqlserver CreateAccount --cli-unfold-argument  \
    --InstanceId mssql-njj2mtpl \
    --Accounts.0.UserName testuser \
    --Accounts.0.Password testpassword
```

Output: 
```
{
    "Response": {
        "RequestId": "8a61e500-aa33-454c-9ec2-da2a368c39ab",
        "FlowId": "30321"
    }
}
```

