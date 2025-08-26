**Example 1: 修改删除保护属性调用示例**

调用成功

Input: 

```
tccli mariadb ModifyInstanceProtectedProperty --cli-unfold-argument  \
    --InstanceId tdsql-cn1peun5 \
    --ProtectedProperty 1
```

Output: 
```
{
    "Response": {
        "RequestId": "8f6e63e1-ca64-42fa-bf67-021d78246dfc"
    }
}
```

