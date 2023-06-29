**Example 1: 新增、修改ck集群用户**



Input: 

```
tccli cdwch ActionAlterCkUser --cli-unfold-argument  \
    --UserInfo.InstanceId cdwch-1vud9x9x \
    --UserInfo.UserName admin \
    --UserInfo.PassWord base54加密 \
    --UserInfo.Describe 测试用户 \
    --ApiType AddSystemUser
```

Output: 
```
{
    "Response": {
        "RequestId": "123456",
        "ErrMsg": ""
    }
}
```

