**Example 1: 请求示例**



Input: 

```
tccli eiam DescribeOrgNode --cli-unfold-argument  \
    --OrgNodeId 7999987a-c9dc-4dd2-b3e2-b52f53317aa6 \
    --IncludeOrgNodeChildInfo true
```

Output: 
```
{
    "Response": {
        "LastModifiedDate": "2021-03-19T10:24:56.091+00:00",
        "RequestId": "b3040fd6-bb8f-438f-bb4a-adf25e373795",
        "ParentOrgNodeId": "94103aaa-79e2-49ee-a9cc-5aa90b30c2e5",
        "DisplayName": "字符串",
        "CreatedDate": "2021-03-19T10:23:29.104+00:00",
        "CustomizedOrgNodeId": "BB1",
        "OrgNodeId": "7999987a-c9dc-4dd2-b3e2-b52f53317aa6",
        "OrgNodeChildInfo": null,
        "Description": "测试机构",
        "DataSource": null
    }
}
```

