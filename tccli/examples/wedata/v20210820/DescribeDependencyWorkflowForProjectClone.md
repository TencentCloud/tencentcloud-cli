**Example 1: 项目克隆-查看依赖工作流信息**



Input: 

```
tccli wedata DescribeDependencyWorkflowForProjectClone --cli-unfold-argument  \
    --ProjectId abc \
    --ConfigList.0.Type abc \
    --ConfigList.0.Key abc \
    --ConfigList.0.Value abc \
    --ConfigList.0.SubInfo.0.Type abc \
    --ConfigList.0.SubInfo.0.Key abc \
    --ConfigList.0.SubInfo.0.Value abc \
    --ConfigList.0.SubInfo.0.ExtInfo abc
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "SelectedWorkflowId": "abc",
                "SelectedWorkflowName": "abc",
                "DependencyWorkflowId": "abc",
                "DependencyWorkflowName": "abc",
                "CrossProject": true,
                "DependencyProjectId": "abc",
                "DependencyProjectName": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

