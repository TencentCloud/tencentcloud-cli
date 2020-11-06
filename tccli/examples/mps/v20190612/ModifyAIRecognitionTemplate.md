**Example 1: Enabling one recognition task while disabling another one**

This example shows you how to modify a custom video content recognition template to disable a full text recognition task and enable a text keyword recognition task.

Input: 

```
tccli mps ModifyAIRecognitionTemplate --cli-unfold-argument  \
    --Definition 30 \
    --OcrFullTextConfigure.Switch OFF \
    --OcrWordsConfigure.Switch ON
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

