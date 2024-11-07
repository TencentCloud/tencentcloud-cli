**Example 1: 增加 projectType**



Input: 

```
tccli taop ListProjects --cli-unfold-argument  \
    --PageNumber 1 \
    --ProjectType 1 \
    --PageSize 30
```

Output: 
```
{
    "Response": {
        "Count": 0,
        "ProjectList": [],
        "RequestId": "8e8f4eef-bdd9-4964-90e8-0095e66270cd"
    }
}
```

**Example 2: 项目列表搜索**



Input: 

```
tccli taop ListProjects --cli-unfold-argument  \
    --PageNumber 4 \
    --ProjectType 0 \
    --PageSize 20 \
    --StudyCountOper -1
```

Output: 
```
{
    "Response": {
        "Count": 59,
        "ProjectList": [],
        "RequestId": "fcf1002e-dee5-4f80-bf79-74ab7171590b"
    }
}
```

**Example 3: 分页查询示例1**



Input: 

```
tccli taop ListProjects --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 2
```

Output: 
```
{
    "Response": {
        "Count": 0,
        "ProjectList": [],
        "RequestId": "3de3cacf-1bd4-4460-837f-fb71448e2d66"
    }
}
```

