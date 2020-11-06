**Example 1: Empower the cloud database account**



Input: 

```
tccli dcdb GrantAccountPrivileges --cli-unfold-argument  \
    --InstanceId dcdbt-fdpjf5zh \
    --UserName testuser1 \
    --Host 172.17.% \
    --DbName * \
    --Type * \
    --Privileges select update
```

Output: 
```
{
    "Response": {
        "RequestId": "87201772-351f-4fb5-9164-fe757fbadb79"
    }
}
```

