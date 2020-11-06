**Example 1: 创建服务相关角色**



Input: 

```
tccli cam CreateServiceLinkedRole --cli-unfold-argument  \
    --QCSServiceName ccs.qcloud.com \
    --CustomSuffix forTest \
    --Description ccsLinkedRole
```

Output: 
```
{
    "Response": {
        "RoleId": "4611686018427411525",
        "RequestId": "c3da1c1c-df35-467d-9335-99c68d993e0a"
    }
}
```

