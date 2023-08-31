**Example 1: 查询资源列表**

查询资源列表

Input: 

```
tccli weilingwith DescribeResources --cli-unfold-argument  \
    --PageNumber 0 \
    --PageSize 0 \
    --Keyword abc \
    --StartTime abc \
    --EndTime abc \
    --Status abc \
    --ProjectId abc \
    --ResourceType abc
```

Output: 
```
{
    "Response": {
        "ResourceList": [
            {
                "ProductName": "abc",
                "ResourceId": "abc",
                "ResourceType": "abc",
                "CreateTime": "abc",
                "Status": "abc",
                "BigDealId": "abc",
                "ProjectId": "abc",
                "TimeSpan": "abc",
                "RenewFlag": true
            }
        ],
        "TotalRow": 0,
        "TotalPage": 0,
        "RequestId": "abc"
    }
}
```

