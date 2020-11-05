**Example 1: Modifying a role’s login permissions**

This example shows you how to use a role ID.

Input: 

```
tccli cam UpdateRoleConsoleLogin --cli-unfold-argument  \
    --RoleId 10000000947212312\
    --ConsoleLogin 1
```

Output: 
```
{
    "Response": {
        "RequestId": "59e72a7a-1e49-4a73-a2db-8993c0334c57"
    }
}
```

