**Example 1: 获取项目列表示例**



Input: 

```
tccli trro DescribeProjectList --cli-unfold-argument  \
    --PageSize 10 \
    --PageNumber 0
```

Output: 
```
{
    "Response": {
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72",
        "Num": 2,
        "Total": 2,
        "Projects": [
            {
                "ModifyTime": "2022-03-22T13:08:04+08:00",
                "ProjectName": "mytest2",
                "ProjectId": "f3glr49r2nwpey5c",
                "ProjectDescription": "test2",
                "PolicyMode": "black"
            },
            {
                "ModifyTime": "2022-03-22T13:08:04+08:00",
                "ProjectName": "project1",
                "ProjectId": "f3glr49r3axn0fu2",
                "ProjectDescription": "test project",
                "PolicyMode": "black"
            }
        ]
    }
}
```

