**Example 1: 给云数据库账号赋权**



Input: 

```
tccli mariadb GrantAccountPrivileges --cli-unfold-argument  \
    --InstanceId tdsql-fdpjf5zh \
    --UserName testuser1 \
    --Host 172.17.% \
    --DbName product_db \
    --Type table \
    --Object prod_user_tbl \
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

