**Example 1: 通过 STS AssumeRole 接口判断指定服务角色是否存在**



Input: 

```
tccli dlc CheckRayOnDLCResourceRole --cli-unfold-argument  \
    --RoleName CheckRayOnDLCResourceRole
```

Output: 
```
{
    "Response": {
        "Granted": false,
        "RequestId": "89af137a-e6ee-4925-822c-aedf8ebaf5ae"
    }
}
```

