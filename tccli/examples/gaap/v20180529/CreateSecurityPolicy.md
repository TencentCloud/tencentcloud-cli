**Example 1: Creating a Security Policy**



Input: 

```
tccli gaap CreateSecurityPolicy --cli-unfold-argument  \
    --ProxyId link-1234\
    --DefaultAction Accept
```

Output: 
```
{
    "Response": {
        "PolicyId": "pl-xxxx",
        "RequestId": "bdcb19c0-74db-47b1-a07c-bbe6985ef44c"
    }
}
```

