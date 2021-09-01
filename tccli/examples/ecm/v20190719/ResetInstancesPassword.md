**Example 1: 重置实例密码**

重置实例密码

Input: 

```
tccli ecm ResetInstancesPassword --cli-unfold-argument  \
    --InstanceIdSet ein-356531dd ein-583021kl \
    --ForceStop false \
    --UserName root \
    --Password cptbtptpA@1095
```

Output: 
```
{
    "Response": {
        "RequestId": "2b719fb1-2f5f-4a2c-bd52-a80b7ca7984c"
    }
}
```

