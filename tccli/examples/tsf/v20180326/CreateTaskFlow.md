**Example 1: 创建工作流**

创建工作流

Input: 

```
tccli tsf CreateTaskFlow --cli-unfold-argument  \
    --FlowName exec-6g4rq8z6 \
    --TriggerRule {} \
    --FlowEdges [] \
    --TimeOut 3000
```

Output: 
```
{
    "Reponse": {
        "Result": "flow-kw2sk8"
    }
}
```

