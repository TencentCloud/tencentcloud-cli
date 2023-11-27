**Example 1: 创建注册码-带参数**

创建注册码-带参数。

Input: 

```
tccli tat CreateRegisterCode --cli-unfold-argument  \
    --Description test \
    --InstanceNamePrefix test \
    --RegisterLimit 0 \
    --EffectiveTime 0 \
    --IpAddressRange 192.168.10.1/10
```

Output: 
```
{
    "Response": {
        "RegisterCodeId": "9b5rb72b-418f-4a81-b32e-f8bc80eef678",
        "RegisterCodeValue": "21e9b871e123427dbee18b0cf3e0d766f91d81a9902843b7b046d7b9ffb9d45a",
        "RequestId": "3f5bf8de-a51a-4ac0-8d95-ad56702cab1f"
    }
}
```

**Example 2: 创建注册码-无参数**

创建注册码-无参数。

Input: 

```
tccli tat CreateRegisterCode --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RegisterCodeId": "9b5rb72b-418f-4a81-b32e-f8bc80eef678",
        "RegisterCodeValue": "21e9b871e123427dbee18b0cf3e0d766f91d81a9902843b7b046d7b9ffb9d45a",
        "RequestId": "2e8bf8de-a51a-4ac0-8d95-ad56702cab1f"
    }
}
```

