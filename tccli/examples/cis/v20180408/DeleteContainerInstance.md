**Example 1: 删除容器实例cis-dev**



Input: 

```
tccli cis DeleteContainerInstance --cli-unfold-argument  \
    --InstanceName cis-dev
```

Output: 
```
{
    "Response": {
        "Msg": "cis-dev has beed deleted",
        "RequestId": "12345"
    }
}
```

