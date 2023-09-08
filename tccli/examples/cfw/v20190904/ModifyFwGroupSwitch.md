**Example 1: 修改防火墙组开关状态**

修改防火墙组开关状态

Input: 

```
tccli cfw ModifyFwGroupSwitch --cli-unfold-argument  \
    --Enable 0 \
    --SwitchList.0.SwitchMode 1 \
    --SwitchList.0.SwitchId cfws-xxxaaacs \
    --AllSwitch 0
```

Output: 
```
{
    "Response": {
        "RequestId": "0752de63-570c-4c2e-bbd2-78574e22a1ae"
    }
}
```

