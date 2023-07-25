**Example 1: 修改自学习模型状态**

修改状态

Input: 

```
tccli asr ModifyCustomizationState --cli-unfold-argument  \
    --ModelId aa6f402f263f12ea856fc81fbecfd0sd \
    --ToState 1
```

Output: 
```
{
    "Response": {
        "ModelId": "aa6f402f263f12ea856fc81fbecfd0sd",
        "RequestId": "3290cfb2-91a7-4989-91de-d1d624a77c12"
    }
}
```

