**Example 1: 导入工作流xml文件**

导入工作流xml文件

Input: 

```
tccli wedata ImportWorkflowXml --cli-unfold-argument  \
    --ProjectId abc \
    --FolderId abc \
    --FileNames abc
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "abc"
    }
}
```

