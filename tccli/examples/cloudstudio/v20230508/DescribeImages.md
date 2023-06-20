**Example 1: 获取工作空间镜像列表**

获取工作空间镜像列表

Input: 

```
tccli cloudstudio DescribeImages --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "9cb384b0-eb60-44e3-a7eb-a7cc1709b94d",
        "Images": [
            {
                "Name": "All in one",
                "Repository": "cloudstudio-devops-docker.pkg.coding.net/artifacts/workspace/full-1.0.0",
                "Tags": [
                    "2023-04-25.0943"
                ]
            }
        ]
    }
}
```

