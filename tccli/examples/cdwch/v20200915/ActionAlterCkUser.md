**Example 1: 新增、修改集群用户**



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
        "RequestId": "20a71202-27c4-4120-80c4-fb1a8e15dxxx",
        "ErrMsg": ""
    }
}
```

