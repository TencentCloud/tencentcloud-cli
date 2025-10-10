**Example 1: 修改防护状态**



Input: 

```
tccli tcss ModifyDefendStatus --cli-unfold-argument  \
    --SwitchOn True \
    --InstanceType abc \
    --IsAll True \
    --InstanceIDs abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

