**Example 1: 更新实例超时时间**



Input: 

```
tccli ags UpdateSandboxInstance --cli-unfold-argument  \
    --InstanceId gw524aigytlvl2qwzsgw5yud5cjuiq3worjeir57 \
    --Timeout 30m
```

Output: 
```
{
    "Response": {
        "RequestId": "0846f2dc-f1d2-465a-93a2-d1873c66f715"
    }
}
```

**Example 2: 替换实例级访问策略**

完整替换当前实例的实例级访问策略。

Input: 

```
tccli ags UpdateSandboxInstance --cli-unfold-argument  \
    --InstanceId 953e15d3655e4daab120b885c908edf7
```

Output: 
```
{
    "Response": {
        "RequestId": "6f8be2d7-b47c-4f55-95c8-1739fcd4e7a1"
    }
}
```

**Example 3: 撤销实例级访问策略**

传入空对象撤销当前实例的实例级访问策略，实例随后仅受 Sandbox Tool 关联的访问策略约束。

Input: 

```
tccli ags UpdateSandboxInstance --cli-unfold-argument  \
    --InstanceId 953e15d3655e4daab120b885c908edf7
```

Output: 
```
{
    "Response": {
        "RequestId": "a2c491e8-6db5-4f02-96c3-f710ed025ba4"
    }
}
```

