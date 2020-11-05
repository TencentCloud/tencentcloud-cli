**Example 1: Creating a template that specifies multiple analysis tasks**

This example shows you how to create a custom video content analysis template to enable intelligent categorization and intelligent tagging tasks.

Input: 

```
tccli mps CreateAIAnalysisTemplate --cli-unfold-argument  \
    --Name 'Intelligent analysis template'\
    --Comment 'Template 2'\
    --ClassificationConfigure.Switch ON\
    --TagConfigure.Switch ON
```

Output: 
```
{
    "Response": {
        "Definition": 31,
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

**Example 2: Creating template with all content analysis tasks enabled**

This example shows you how to create a custom video content analysis template to enable all intelligent analysis tasks.

Input: 

```
tccli mps CreateAIAnalysisTemplate --cli-unfold-argument  \
    --Name 'Intelligent analysis template'\
    --Comment 'Template 3'\
    --ClassificationConfigure.Switch ON\
    --TagConfigure.Switch ON\
    --CoverConfigure.Switch NO\
    --FrameTagConfigure.Switch ON
```

Output: 
```
{
    "Response": {
        "Definition": 33,
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

**Example 3: Creating a template that specifies an analysis task**

This example shows you how to create a custom video content analysis template to enable an intelligent categorization task.

Input: 

```
tccli mps CreateAIAnalysisTemplate --cli-unfold-argument  \
    --Name 'Intelligent analysis template'\
    --Comment 'Template 1'\
    --ClassificationConfigure.Switch ON
```

Output: 
```
{
    "Response": {
        "Definition": 30,
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

