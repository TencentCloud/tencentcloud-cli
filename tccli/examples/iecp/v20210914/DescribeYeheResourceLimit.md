**Example 1: 获取用户配置限制**



Input: 

```
tccli iecp DescribeYeheResourceLimit --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "5ebf13a2-f925-4ba7-adff-ddbc21d355e3",
        "Uin": "12345",
        "CreateNodeLimit": 3,
        "CreateClusterLimit": 2551,
        "EnablePermMonitor": false,
        "EnablePermAdminNode": false
    }
}
```

**Example 2: 获取用户限制列表**



Input: 

```
tccli iecp DescribeYeheResourceLimit --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "0c17c5e2-61a7-4428-8778-b9051e4ef042",
        "Uin": "600000559632",
        "CreateNodeLimit": 200,
        "CreateClusterLimit": 1,
        "EnablePermMonitor": false,
        "EnablePermAdminNode": false
    }
}
```

