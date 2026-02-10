**Example 1: 重启实例**

重启CK节点

Input: 

```
tccli cdwch RestartInstance --cli-unfold-argument  \
    --InstanceId cdwch-xxxxxxx \
    --NodeType CK \
    --NodeIpList 10.xx.xx.1 10.xx.xx.2
```

Output: 
```
{
    "Response": {
        "FlowId": "16",
        "RequestId": "6f6d5b7b-8951-49c3-aa38-xxxxxxxxxxxx"
    }
}
```

