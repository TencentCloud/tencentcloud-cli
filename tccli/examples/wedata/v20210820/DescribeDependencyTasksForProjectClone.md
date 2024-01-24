**Example 1: 【任务模式克隆】获取依赖任务信息**



Input: 

```
tccli wedata DescribeDependencyTasksForProjectClone --cli-unfold-argument  \
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
                "SelectedTaskId": "abc",
                "SelectedTaskName": "abc",
                "DependencyTaskId": "abc",
                "DependencyTaskName": "abc",
                "CrossProject": true,
                "DependencyProjectId": "abc",
                "DependencyProjectName": "abc",
                "DependencyTaskVirtualFlag": true,
                "LinkDependency": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

**Example 2: 错误用例**

错误用例

Input: 

```
tccli wedata DescribeDependencyTasksForProjectClone --cli-unfold-argument  \
    --ProjectId 1470547050521227264 \
    --ConfigList.0.Type ccc \
    --ConfigList.0.Key ccc \
    --ConfigList.0.Value ccc
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InternalError",
            "Message": "内部服务错误，请稍后重试。"
        },
        "RequestId": "b2f67471-0eb4-45a4-a000-ec722b4cc3e5"
    }
}
```

