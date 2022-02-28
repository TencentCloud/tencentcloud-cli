**Example 1: 拉取流程列表**



Input: 

```
tccli ess DescribeFlowBriefs --cli-unfold-argument  \
    --Operator.UserId 65fb0c591044be8a1f60aa382cc5ed0e \
    --Operator.ClientIp  \
    --Operator.Channel  \
    --Operator.OpenId  \
    --Operator.ProxyIp  \
    --FlowIds ce00a136469d1e634184bd44937d5810 23b242602fce2e9ec2789304116c6864
```

Output: 
```
{
    "Response": {
        "RequestId": "ce00a136469d1e634184bd44937d5810",
        "FlowBriefs": [
            {
                "FlowId": "ce00a136469d1e634184bd44937d5810",
                "FlowName": "160491079769864798616:33:18",
                "FlowDescription": "测试流程的描述信息",
                "FlowType": "合同",
                "FlowStatus": 1,
                "CreatedOn": 1604910798,
                "FlowMessage": ""
            },
            {
                "FlowId": "23b242602fce2e9ec2789304116c6864",
                "FlowName": "160491079769864798616:33:17",
                "FlowDescription": "测试流程的描述信息",
                "FlowType": "合同",
                "FlowStatus": 1,
                "CreatedOn": 1604910797,
                "FlowMessage": ""
            }
        ]
    }
}
```

