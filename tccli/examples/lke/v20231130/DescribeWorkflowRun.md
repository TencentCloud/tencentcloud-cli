**Example 1: 查询工作流运行实例详情**

查询工作流运行实例详情

Input: 

```
tccli lke DescribeWorkflowRun --cli-unfold-argument  \
    --WorkflowRunId 1dcf5a21-6223-4358-b8a0-b4d6571
```

Output: 
```
{
    "Response": {
        "WorkflowRun": {
            "RunEnv": 1,
            "AppBizId": "1854548189164339200",
            "WorkflowRunId": "1dcf5a21-6223-4358-b8a0-b4d6",
            "WorkflowId": "412f5a21-6223-4358-b8a0-b4d6",
            "Name": "订酒店",
            "State": 1,
            "FailMessage": "",
            "TotalTokens": 100,
            "StartTime": "1672531200000",
            "EndTime": "1672531300000",
            "CreateTime": "1672531100000",
            "DialogJson": "{\"Workflows\": {\"WorkflowID\":\"1dcf5a21-6223-4358-b8a0-b4d65712f44c\",\"WorkflowName\":\"异步\",\"WorkflowDesc\":\"异步\",\"Nodes\":[{\"NodeID\":\"a2b6549c-85b6-b404-a736-3d738591f297\",\"NodeName\":\"开始\",\"NodeType\":\"START\",\"NodeDesc\":\"\",\"StartNodeData\":{},\"NextNodeIDs\":[\"bb004f48-eabd-4104-6cb1-1fb9f154c24d\"],\"Inputs\":[],\"NodeUI\":\"{\\\"data\\\":{\\\"content\\\":\\\"\\\",\\\"isHovering\\\":false,\\\"isParallel\\\":false,\\\"source\\\":false,\\\"target\\\":true,\\\"debug\\\":null,\\\"error\\\":false,\\\"output\\\":[]},\\\"position\\\":{\\\"x\\\":400,\\\"y\\\":282},\\\"targetPosition\\\":\\\"left\\\",\\\"sourcePosition\\\":\\\"right\\\",\\\"selected\\\":false,\\\"measured\\\":{\\\"width\\\":250,\\\"height\\\":84}}\"},{\"NodeID\":\"4710f3a1-fa47-d542-e3be-5b5ce38be1fe\",\"NodeName\":\"结束\",\"NodeType\":\"END\",\"NodeDesc\":\"\",\"EndNodeData\":{},\"NextNodeIDs\":[],\"Outputs\":[{\"Title\":\"Output\",\"Type\":\"OBJECT\",\"Required\":[],\"Properties\":[],\"Desc\":\"输出内容\"}],\"NodeUI\":\"{\\\"data\\\":{\\\"content\\\":\\\"\\\",\\\"isHovering\\\":false,\\\"isParallel\\\":false,\\\"source\\\":true,\\\"target\\\":false,\\\"debug\\\":null,\\\"error\\\":false,\\\"output\\\":[{\\\"label\\\":\\\"Output\\\",\\\"desc\\\":\\\"输出内容\\\",\\\"optionType\\\":\\\"REFERENCE_OUTPUT\\\",\\\"type\\\":\\\"OBJECT\\\",\\\"children\\\":[]}]},\\\"position\\\":{\\\"x\\\":1200,\\\"y\\\":282},\\\"targetPosition\\\":\\\"left\\\",\\\"sourcePosition\\\":\\\"right\\\",\\\"selected\\\":false,\\\"measured\\\":{\\\"width\\\":250,\\\"height\\\":84}}\"},{\"NodeID\":\"bb004f48-eabd-4104-6cb1-1fb9f154c24d\",\"NodeName\":\"代码1\",\"NodeType\":\"CODE_EXECUTOR\",\"NodeDesc\":\"\",\"CodeExecutorNodeData\":{\"Code\":\"CiMg6K+35L+d5a2Y5Ye95pWw5ZCN5Li6bWFpbizovpPlhaXovpPlh7rlnYfkuLpkaWN077yb5pyA57uI57uT5p6c5Lya5LulanNvbuWtl+espuS4suaWueW8j+i/lOWbnu+8jOivt+WLv+ebtOaOpei/lOWbnuS4jeaUr+aMgWpzb24uZHVtcHPnmoTlr7nosaEKZGVmIG1haW4ocGFyYW1zOiBkaWN0KSAtPiBkaWN0OgogICAgcmV0dXJuIHsKICAgICAgICAncmVzdWx0JzogcGFyYW1zLmdldCgnaW5wdXQnLCAwKQogICAgfQo=\",\"Language\":0},\"NextNodeIDs\":[\"4710f3a1-fa47-d542-e3be-5b5ce38be1fe\"],\"Inputs\":[],\"Outputs\":[{\"Title\":\"Output\",\"Type\":\"OBJECT\",\"Required\":[],\"Properties\":[{\"Title\":\"result\",\"Type\":\"STRING\",\"Required\":[],\"Properties\":[],\"Desc\":\"\"}],\"Desc\":\"输出内容\"}],\"NodeUI\":\"{\\\"data\\\":{\\\"content\\\":{\\\"outputs\\\":[\\\"Output\\\",\\\"Output.result\\\"],\\\"inputs\\\":[]},\\\"isHovering\\\":false,\\\"isParallel\\\":false,\\\"source\\\":true,\\\"target\\\":true,\\\"debug\\\":null,\\\"error\\\":false,\\\"output\\\":[{\\\"id\\\":\\\"b14d43a6-51ea-2df8-fcfc-759261cd5b1b\\\",\\\"value\\\":\\\"Output\\\",\\\"label\\\":\\\"Output\\\",\\\"type\\\":\\\"OBJECT\\\",\\\"children\\\":[{\\\"id\\\":\\\"e8a0a1f1-8bb4-892a-34ba-e020e3f48c99\\\",\\\"value\\\":\\\"result\\\",\\\"label\\\":\\\"result\\\",\\\"type\\\":\\\"STRING\\\",\\\"children\\\":[]}]}]},\\\"position\\\":{\\\"x\\\":700,\\\"y\\\":282},\\\"targetPosition\\\":\\\"left\\\",\\\"sourcePosition\\\":\\\"right\\\",\\\"selected\\\":true,\\\"measured\\\":{\\\"width\\\":250,\\\"height\\\":104}}\"}],\"Edge\":\"[{\\\"source\\\":\\\"a2b6549c-85b6-b404-a736-3d738591f297\\\",\\\"sourceHandle\\\":\\\"a2b6549c-85b6-b404-a736-3d738591f297-source\\\",\\\"target\\\":\\\"bb004f48-eabd-4104-6cb1-1fb9f154c24d\\\",\\\"type\\\":\\\"custom\\\",\\\"data\\\":{\\\"connectedNodeIsHovering\\\":false,\\\"error\\\":false,\\\"isHovering\\\":false},\\\"id\\\":\\\"xy-edge__a2b6549c-85b6-b404-a736-3d738591f297a2b6549c-85b6-b404-a736-3d738591f297-source-bb004f48-eabd-4104-6cb1-1fb9f154c24d\\\"},{\\\"source\\\":\\\"bb004f48-eabd-4104-6cb1-1fb9f154c24d\\\",\\\"sourceHandle\\\":\\\"bb004f48-eabd-4104-6cb1-1fb9f154c24d-source\\\",\\\"target\\\":\\\"4710f3a1-fa47-d542-e3be-5b5ce38be1fe\\\",\\\"targetHandle\\\":\\\"4710f3a1-fa47-d542-e3be-5b5ce38be1fe-target\\\",\\\"type\\\":\\\"custom\\\",\\\"data\\\":{\\\"connectedNodeIsHovering\\\":false,\\\"isHovering\\\":false,\\\"error\\\":false},\\\"id\\\":\\\"xy-edge__bb004f48-eabd-4104-6cb1-1fb9f154c24dbb004f48-eabd-4104-6cb1-1fb9f154c24d-source-4710f3a1-fa47-d542-e3be-5b5ce38be1fe4710f3a1-fa47-d542-e3be-5b5ce38be1fe-target\\\"}]\"}}",
            "Query": "我想订酒店",
            "MainModelName": "workflow-pro",
            "CustomVariables": []
        },
        "NodeRuns": [
            {
                "NodeRunId": "nf5a21-6223-4358-b8a789",
                "NodeId": "e60de932-b050-65ce-261e-027760e93d81",
                "WorkflowRunId": "1dcf5a21-6223-4358-b8a0-b4d6",
                "NodeName": "大模型节点",
                "NodeType": 3,
                "State": 1,
                "FailCode": "",
                "FailMessage": "",
                "CostMilliseconds": 1000,
                "TotalTokens": 100
            }
        ],
        "RequestId": "925208e7-46fa-43b3-a429-ddcbccad24f6"
    }
}
```

