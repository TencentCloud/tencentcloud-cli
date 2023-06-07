**Example 1: 普通IP转弹性IP**

普通IP转弹性IP。

Input: 

```
tccli vpc TransformAddress --cli-unfold-argument  \
    --InstanceId ins-3ea0qeu6
```

Output: 
```
{
    "Response": {
        "AddressId": "eip-fk2gmm9s",
        "TaskId": 345732,
        "RequestId": "070889cb-a42a-40a0-ac50-293ef36e0dfc"
    }
}
```

