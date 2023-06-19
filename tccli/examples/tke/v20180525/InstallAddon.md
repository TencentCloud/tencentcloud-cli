**Example 1: 安装addon**

为目标集群安装一个addon

Input: 

```
tccli tke InstallAddon --cli-unfold-argument  \
    --ClusterId cls-123deabc \
    --AddonName cbs
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

