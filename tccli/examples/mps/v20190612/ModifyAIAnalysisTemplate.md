**Example 1: Enabling one content analysis task and disabling another one at the same time**

This example shows you how to modify a custom video content analysis template to enable an intelligent tagging task and disable an intelligent cover generating task.

Input: 

```
tccli mps ModifyAIAnalysisTemplate --cli-unfold-argument  \
    --Definition 30\
    --TagConfigure.Switch ON\
    --CoverConfigure.Switch OFF
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

**Example 2: Enabling intelligent cover generating task**

This example shows you how to modify a custom video content analysis template to enable an intelligent cover generating task.

Input: 

```
tccli mps ModifyAIAnalysisTemplate --cli-unfold-argument  \
    --Definition 30\
    --CoverConfigure.Switch ON
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

**Example 3: Disabling intelligent cover generating task**

This example shows you how to modify a custom video content analysis template to disable an intelligent cover generating task.

Input: 

```
tccli mps ModifyAIAnalysisTemplate --cli-unfold-argument  \
    --Definition 30\
    --CoverConfigure.Switch OFF
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

