**Example 1: 错误示例**

错误示例

Input: 

```
tccli wedata DescribeProjectParamDsPage --cli-unfold-argument  \
    --ProjectId 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "UnauthorizedOperation",
            "Message": "未授权操作"
        },
        "RequestId": "43bf9eb0-ad97-4b94-86dd-bfe293be569c"
    }
}
```

**Example 2: 错误示例1**

错误示例1

Input: 

```
tccli wedata DescribeProjectParamDsPage --cli-unfold-argument  \
    --ProjectId 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "UnauthorizedOperation",
            "Message": "未授权操作"
        },
        "RequestId": "33bbf762-0b43-4582-9abe-9ded9ffbe05e"
    }
}
```

