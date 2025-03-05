**Example 1: 重启实例**

用户在控制台主动发起重启实例

Input: 

```
tccli cdwpg RestartInstance --cli-unfold-argument  \
    --InstanceId cdwpg-13456 \
    --NodeTypes cn dn \
    --NodeIds 102 103
```

Output: 
```
{
    "Response": {
        "RequestId": "fdsfsd",
        "FlowId": 1,
        "ErrorMsg": "faile to restart intance"
    }
}
```

