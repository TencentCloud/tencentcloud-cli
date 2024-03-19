**Example 1: 查询批量撤销任务结果**

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

