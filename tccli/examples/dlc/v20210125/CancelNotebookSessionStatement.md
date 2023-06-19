**Example 1: 取消session中执行的任务**

取消session中执行的任务

Input: 

```
tccli dlc CancelNotebookSessionStatement --cli-unfold-argument  \
    --SessionId d3018ad4-9a7e-4f64-a3f4-f38507c69742 \
    --StatementId d3018ad4-9a7e-4f64-a3dj-f38507c697dj
```

Output: 
```
{
    "Response": {
        "RequestId": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1"
    }
}
```

