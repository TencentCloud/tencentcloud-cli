**Example 1: 通过资源栈ID查询感兴趣的资源栈列表**



Input: 

```
tccli tic DescribeStacks --cli-unfold-argument  \
    --StackIds stk-ud52n3td stk-hz5vn3te stk-a9jwn3t3 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 3,
        "Stacks": [
            {
                "StackId": "stk-ud52n3td",
                "StackName": "awesome stack name 1",
                "Description": "a stack description",
                "Region": "ap-guangzhou",
                "Status": "VERSION_EDITING",
                "CreateTime": "2020-11-18T07:38:47.330Z"
            },
            {
                "StackId": "stk-hz5vn3te",
                "StackName": "awesome stack name 2",
                "Description": "a stack description",
                "Region": "ap-guangzhou",
                "Status": "VERSION_EDITING",
                "CreateTime": "2020-11-18T07:39:47.330Z"
            },
            {
                "StackId": "stk-a9jwn3t3",
                "StackName": "awesome stack name 3",
                "Description": "a stack description",
                "Region": "ap-guangzhou",
                "Status": "VERSION_EDITING",
                "CreateTime": "2020-11-18T07:40:47.330Z"
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

