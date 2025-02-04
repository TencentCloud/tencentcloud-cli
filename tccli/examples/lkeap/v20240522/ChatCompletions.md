**Example 1: 对话**

对话

Input: 

```
tccli lkeap ChatCompletions --cli-unfold-argument  \
    --Model deepseek-r1 \
    --Messages.0.Role user \
    --Messages.0.Content 你好 \
    --Stream False
```

Output: 
```
{
    "Response": {
        "RequestId": "26b3ed8b-960d-4d68-bc7f-098839f4b574"
    }
}
```

