**Example 1: 获取项目列表**



Input: 

```
tccli tag DescribeProjects --cli-unfold-argument  \
    --Limit 1000 \
    --AllList 0 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Projects": [
            {
                "ProjectId": 1000101,
                "ProjectName": "test1",
                "CreatorUin": 100000012345,
                "ProjectInfo": "",
                "CreateTime": "2021-10-13 11:03:30"
            }
        ],
        "RequestId": "d75bbc07-f5bd-4020-b4bd-f877e9ccd1db"
    }
}
```

