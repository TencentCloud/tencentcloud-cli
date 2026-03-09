**Example 1: 修改etcd实例属性**



Input: 

```
tccli cetcd ModifyEtcdAttribute --cli-unfold-argument  \
    --InstanceId etcd-1234abcd \
    --Name test \
    --Description example
```

Output: 
```
{
    "Response": {
        "RequestId": "abcdefg"
    }
}
```

