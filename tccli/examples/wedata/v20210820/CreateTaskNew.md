**Example 1: 创建任务**

创建任务

Input: 

```
tccli wedata CreateTaskNew --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --WorkflowId c3ebf6b9-d34b-4dff-bc5d-334f8ce11ad1 \
    --TaskName test342342 \
    --TaskType 35 \
    --TaskExt.0.Key extraInfo \
    --TaskExt.0.Value eyJmcm9tTWFwcGluZyI6ZmFsc2V9 \
    --ProductName DATA_DEV \
    --LeftCoordinate 224 \
    --TopCoordinate 224 \
    --Content IyEvYmluL2Jhc2gKIyoqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKiMKIyNhdXRob3I6IGtldmlubmllCiMjY3JlYXRlIHRpbWU6IDIwMjQtMTEtMDcgMTA6NTQ6MzUKIyoqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKiMK
```

Output: 
```
{
    "Response": {
        "Data": "20241107105820356",
        "RequestId": "a8b7605c-c3d8-4f92-8e23-4bfb4a57cfd8"
    }
}
```

