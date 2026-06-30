**Example 1: 查询全量撤销企业合同任务结果**

查询全量撤销企业合同任务结果

Input: 

```
tccli essbasic DescribeCancelFlowsTask --cli-unfold-argument  \
    --Agent.AppId yDwFoUUckpsomwx1UyhWGhIR2RkhOjw2 \
    --Agent.ProxyOrganizationOpenId ess_open_organization_1 \
    --Agent.ProxyOperator.OpenId kevinlcheng \
    --TaskId yD3POUUckpzme5ekUxM7lqE1ODrkqmYz \
    --CancelType 1
```

Output: 
```
{
    "Response": {
        "FailureFlows": [],
        "SuccessFlowIds": [
            "yD3POUUckpzx1mhdU1UuDSYM1xwPbeJL"
        ],
        "TaskId": "yD3POUUckpzme5ekUxM7lqE1ODrkqmYz",
        "TaskStatus": "END",
        "RequestId": "d3becccb-75e5-43fc-9be6-27ccf7bd4067"
    }
}
```

**Example 2: 查询批量撤销任务结果**

查询批量撤销任务结果

Input: 

```
tccli essbasic DescribeCancelFlowsTask --cli-unfold-argument  \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.AppId yDRS4UUgygqdcj8xUuO4zjEwOT7IN8Ec \
    --TaskId yDCVWUUckpwkjgiuUWGW8cRAzd84BVQa
```

Output: 
```
{
    "Response": {
        "FailureFlows": [
            {
                "FlowId": "yDCNGUUckpvjdelbUuyImI9pY8I5Mep9",
                "Reason": "合同当前状态不支持撤销"
            },
            {
                "FlowId": "yDw9jUUgyg34g2mdUxawbT61HrwMQ3gF",
                "Reason": "合同信息不存在或非本企业发起的合同"
            }
        ],
        "RequestId": "49f10eec-73af-4f1b-bc99-d36e9a60e631",
        "SuccessFlowIds": [
            "yDCN0UUckpvhnc6uUuyImI98ydIEe4bX"
        ],
        "TaskId": "yDCVWUUckpwkjgiuUWGW7cRAzd93BVQa",
        "TaskStatus": "END"
    }
}
```

