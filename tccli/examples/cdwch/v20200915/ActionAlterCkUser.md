**Example 1: 新增、修改ck集群用户**



Input: 

```
tccli cdwch ActionAlterCkUser --cli-unfold-argument  \
    --UserInfo.InstanceId xx \
    --UserInfo.PassWord xx \
    --UserInfo.Describe xx \
    --ApiType xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "ErrMsg": "xx"
    }
}
```

