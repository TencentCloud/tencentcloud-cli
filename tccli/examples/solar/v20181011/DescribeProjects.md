**Example 1: DescribeProjects**



Input: 

```
tccli solar DescribeProjects --cli-unfold-argument  \
    --PageNo 1 \
    --PageSize 2 \
    --Filters.Type 0
```

Output: 
```
{
    "Response": {
        "ProjectList": [
            {
                "CreateTime": "2020-01-16 15:32:34",
                "ProjectBudget": 10,
                "ProjectId": "testprj-fjypzt0ne0",
                "ProjectIntroduction": "小星星",
                "ProjectName": "小星星",
                "ProjectOrg": "开发测试中心",
                "ProjectOrgId": "661594418817667072",
                "ProjectStatus": "编辑中"
            },
            {
                "CreateTime": "2020-01-16 15:25:47",
                "ProjectBudget": 1111,
                "ProjectId": "testprj-8fgl6bile6",
                "ProjectIntroduction": "111",
                "ProjectName": "lhjtest",
                "ProjectOrg": "研发部",
                "ProjectOrgId": "651831291142082560",
                "ProjectStatus": "运营中"
            }
        ],
        "RequestId": "b81ee8cc-9c08-41bd-95ee-d6f97d5899b8",
        "TotalCount": 158
    }
}
```

