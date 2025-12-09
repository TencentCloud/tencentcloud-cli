**Example 1: 查询工作流运行实例详情**

查询工作流运行实例详情

Input: 

```
tccli lke DescribeWorkflowRun --cli-unfold-argument  \
    --AppBizId 1963140753734418240 \
    --WorkflowRunId wfr-asaodefdu7pc
```

Output: 
```
{
    "Response": {
        "NodeRuns": [
            {
                "CostMilliseconds": 0,
                "FailCode": "",
                "FailMessage": "",
                "NodeId": "11a76786-2578-8f2e-ab4e-96fbe393b750",
                "NodeName": "开始",
                "NodeRunId": "nr-e0eecd24-7b19-40c6-b730-77b6f3c0b1c0",
                "NodeType": 1,
                "State": 2,
                "TotalTokens": 0,
                "WorkflowRunId": "wfr-asaodefdu7pc"
            },
            {
                "CostMilliseconds": 105,
                "FailCode": "",
                "FailMessage": "",
                "NodeId": "4bb28c02-c142-4885-958b-e700c88d05e1",
                "NodeName": "代码1",
                "NodeRunId": "nr-d1b55ca0-ca64-46af-8cd7-e59995abd7a4",
                "NodeType": 7,
                "State": 2,
                "TotalTokens": 0,
                "WorkflowRunId": "wfr-asaodefdu7pc"
            },
            {
                "CostMilliseconds": 2971,
                "FailCode": "",
                "FailMessage": "",
                "NodeId": "578d6b2e-d334-1df1-c512-551c358fb790",
                "NodeName": "代码2",
                "NodeRunId": "nr-9fd4a172-eaff-4b97-8479-46a6bc445163",
                "NodeType": 7,
                "State": 2,
                "TotalTokens": 0,
                "WorkflowRunId": "wfr-asaodefdu7pc"
            },
            {
                "CostMilliseconds": 0,
                "FailCode": "",
                "FailMessage": "",
                "NodeId": "88753333-e45b-fdd4-2aa3-7660998fbb91",
                "NodeName": "结束",
                "NodeRunId": "nr-66a33273-e14a-4cc4-b6d2-a76fd3378242",
                "NodeType": 16,
                "State": 2,
                "TotalTokens": 0,
                "WorkflowRunId": "wfr-asaodefdu7pc"
            }
        ],
        "RequestId": "8d785cd9-bf9e-465b-a311-0b765d328b31",
        "WorkflowRun": {
            "AppBizId": "1928404831808934976",
            "CreateTime": "1759142308976",
            "CustomVariables": [
                {
                    "Name": "is_show_tips",
                    "Value": "aaaa"
                }
            ],
            "WorkflowGraph": "{\"ProtoVersion\":\"V2_6\", \"WorkflowID\":\"47d7c1f7-501b-465a-aa6a-73846c92ca44\", \"WorkflowName\":\"代码\", \"WorkflowDesc\":\"代码\", \"Nodes\":[{\"NodeID\":\"11a76786-2578-8f2e-ab4e-96fbe393b750\", \"NodeName\":\"开始\", \"NodeDesc\":\"\", \"NodeType\":\"START\", \"StartNodeData\":{\"WorkflowParams\":[{\"Name\":\"obj\", \"Type\":\"OBJECT\", \"Desc\":\"\", \"IsRequired\":false, \"SubInputs\":[{\"Name\":\"aaa\", \"Type\":\"STRING\", \"Desc\":\"\", \"IsRequired\":false, \"SubInputs\":[], \"DefaultValue\":\"\", \"DefaultFileName\":\"\"}, {\"Name\":\"bb\", \"Type\":\"STRING\", \"Desc\":\"\", \"IsRequired\":false, \"SubInputs\":[], \"DefaultValue\":\"\", \"DefaultFileName\":\"\"}], \"DefaultValue\":\"{\\\"aaa\\\": \\\"AAA\\\", \\\"bb\\\": \\\"BBBB\\\"}\", \"DefaultFileName\":\"\"}, {\"Name\":\"arrarr\", \"Type\":\"ARRAY_ARRAY\", \"Desc\":\"\", \"IsRequired\":false, \"SubInputs\":[], \"DefaultValue\":\"[[1, 2,3]]\", \"DefaultFileName\":\"\"}]}, \"Inputs\":[], \"Outputs\":[], \"NextNodeIDs\":[\"4bb28c02-c142-4885-958b-e700c88d05e1\", \"578d6b2e-d334-1df1-c512-551c358fb790\"], \"NodeUI\":\"{\\\"data\\\":{\\\"content\\\":{\\\"inputs\\\":[]},\\\"isHovering\\\":false,\\\"isParallel\\\":false,\\\"source\\\":false,\\\"target\\\":true,\\\"debug\\\":null,\\\"error\\\":false,\\\"output\\\":[],\\\"schema\\\":null,\\\"checkDataError\\\":0},\\\"position\\\":{\\\"x\\\":434,\\\"y\\\":482},\\\"targetPosition\\\":\\\"left\\\",\\\"sourcePosition\\\":\\\"right\\\",\\\"selected\\\":false,\\\"measured\\\":{\\\"width\\\":250,\\\"height\\\":84},\\\"dragging\\\":false}\"}, {\"NodeID\":\"88753333-e45b-fdd4-2aa3-7660998fbb91\", \"NodeName\":\"结束\", \"NodeDesc\":\"\", \"NodeType\":\"END\", \"Inputs\":[], \"Outputs\":[{\"Title\":\"Output\", \"Type\":\"OBJECT\", \"Required\":[], \"Properties\":[], \"Desc\":\"输出内容\", \"AnalysisMethod\":\"COVER\"}], \"NextNodeIDs\":[], \"NodeUI\":\"{\\\"data\\\":{\\\"isHovering\\\":false,\\\"isParallel\\\":false,\\\"source\\\":true,\\\"target\\\":false,\\\"debug\\\":null,\\\"error\\\":false,\\\"output\\\":[],\\\"schema\\\":null,\\\"checkDataError\\\":0},\\\"position\\\":{\\\"x\\\":1041,\\\"y\\\":441},\\\"targetPosition\\\":\\\"left\\\",\\\"sourcePosition\\\":\\\"right\\\",\\\"selected\\\":false,\\\"measured\\\":{\\\"width\\\":250,\\\"height\\\":84},\\\"dragging\\\":false}\"}, {\"NodeID\":\"4bb28c02-c142-4885-958b-e700c88d05e1\", \"NodeName\":\"代码1\", \"NodeDesc\":\"\", \"NodeType\":\"CODE_EXECUTOR\", \"CodeExecutorNodeData\":{\"Code\":\"\\nfrom jinja2 import Template\\nimport json\\n\\ndef main(params: dict) -> dict:\\n    input = params.get('input', '{}')  # 获取用户输入的JSON字符串\\n    template = Template(\\\"\\\"\\\"\\n{{ input.name }}\\n{{ input.age }}\\n{{ input.occupation }}\\n    \\\"\\\"\\\")  # 解析JSON字符串，分别输出字段\\n    result = template.render(input=json.loads(input))  # 解析JSON字符串\\n    return {'result': result.splitlines()}  # 返回每个字段为单独的元素\\n\", \"Language\":\"PYTHON3\"}, \"Inputs\":[{\"Name\":\"input\", \"Type\":\"STRING\", \"Input\":{\"InputType\":\"USER_INPUT\", \"UserInputValue\":{\"Values\":[\"{\\\"name\\\": 3, \\\"age\\\": 3, \\\"occupation\\\": 1 }\"]}}, \"Desc\":\"\", \"IsRequired\":false, \"SubInputs\":[], \"DefaultValue\":\"\", \"DefaultFileName\":\"\"}], \"Outputs\":[{\"Title\":\"Output\", \"Type\":\"OBJECT\", \"Required\":[], \"Properties\":[{\"Title\":\"result\", \"Type\":\"STRING\", \"Required\":[], \"Properties\":[], \"Desc\":\"\", \"AnalysisMethod\":\"COVER\"}], \"Desc\":\"输出内容\", \"AnalysisMethod\":\"COVER\"}], \"NextNodeIDs\":[\"88753333-e45b-fdd4-2aa3-7660998fbb91\"], \"NodeUI\":\"{\\\"data\\\":{\\\"content\\\":{\\\"outputs\\\":[\\\"Output\\\",\\\"Output.result\\\"],\\\"inputs\\\":[\\\"input\\\"]},\\\"isHovering\\\":false,\\\"isParallel\\\":false,\\\"source\\\":true,\\\"target\\\":true,\\\"debug\\\":null,\\\"error\\\":false,\\\"output\\\":[{\\\"id\\\":\\\"21e93433-c30d-1fdc-b470-36275c437521\\\",\\\"value\\\":\\\"Output\\\",\\\"label\\\":\\\"Output\\\",\\\"_uiId\\\":\\\"baedb05d-0daf-9968-5947-e7bb0d878714\\\",\\\"type\\\":\\\"OBJECT\\\",\\\"children\\\":[{\\\"id\\\":\\\"da7598f7-4bea-bb2c-36db-8ea0908099f7\\\",\\\"value\\\":\\\"result\\\",\\\"label\\\":\\\"result\\\",\\\"_uiId\\\":\\\"b3f535b9-f76d-5bd4-849d-94d5b7aa9f20\\\",\\\"type\\\":\\\"STRING\\\",\\\"children\\\":[]}]}],\\\"schema\\\":null,\\\"checkDataError\\\":0},\\\"position\\\":{\\\"x\\\":725,\\\"y\\\":333},\\\"targetPosition\\\":\\\"left\\\",\\\"sourcePosition\\\":\\\"right\\\",\\\"selected\\\":true,\\\"measured\\\":{\\\"width\\\":250,\\\"height\\\":104},\\\"dragging\\\":false}\", \"ExceptionHandling\":{\"Switch\":\"OFF\", \"MaxRetries\":\"3\", \"RetryInterval\":\"1\", \"AbnormalOutputResult\":\"\", \"HandleMethod\":\"EXCEPTION_OUTPUT\", \"NextNodeIDs\":[]}}, {\"NodeID\":\"578d6b2e-d334-1df1-c512-551c358fb790\", \"NodeName\":\"代码2\", \"NodeDesc\":\"\", \"NodeType\":\"CODE_EXECUTOR\", \"CodeExecutorNodeData\":{\"Code\":\"\\n// 请保存函数名为main,输入输出均为object；最终结果会以json字符串方式返回\\nfunction main(params) {\\n    console.log(\\\"XXXXXXXXXXX\\\")\\n    return {\\n        'result': params.input || 0,\\n        'result2': 333,\\n        'arrarr': params.arrarr\\n    };\\n}\\n\", \"Language\":\"JS\"}, \"Inputs\":[{\"Name\":\"input\", \"Type\":\"OBJECT\", \"Input\":{\"InputType\":\"WORKFLOW_VARIABLE\", \"WorkflowParam\":{\"VarBizID\":\"\", \"JsonPath\":\"obj\"}}, \"Desc\":\"\", \"IsRequired\":false, \"SubInputs\":[], \"DefaultValue\":\"\", \"DefaultFileName\":\"\"}, {\"Name\":\"arrarr\", \"Type\":\"ARRAY_ARRAY\", \"Input\":{\"InputType\":\"WORKFLOW_VARIABLE\", \"WorkflowParam\":{\"VarBizID\":\"\", \"JsonPath\":\"arrarr\"}}, \"Desc\":\"\", \"IsRequired\":false, \"SubInputs\":[], \"DefaultValue\":\"\", \"DefaultFileName\":\"\"}], \"Outputs\":[{\"Title\":\"Output\", \"Type\":\"OBJECT\", \"Required\":[], \"Properties\":[{\"Title\":\"result\", \"Type\":\"OBJECT\", \"Required\":[], \"Properties\":[{\"Title\":\"aaa\", \"Type\":\"STRING\", \"Required\":[], \"Properties\":[], \"Desc\":\"\", \"AnalysisMethod\":\"COVER\"}, {\"Title\":\"bb\", \"Type\":\"STRING\", \"Required\":[], \"Properties\":[], \"Desc\":\"\", \"AnalysisMethod\":\"COVER\"}], \"Desc\":\"\", \"AnalysisMethod\":\"COVER\"}, {\"Title\":\"result2\", \"Type\":\"INT\", \"Required\":[], \"Properties\":[], \"Desc\":\"\", \"AnalysisMethod\":\"COVER\"}], \"Desc\":\"输出内容\", \"AnalysisMethod\":\"COVER\"}], \"NextNodeIDs\":[\"88753333-e45b-fdd4-2aa3-7660998fbb91\"], \"NodeUI\":\"{\\\"data\\\":{\\\"content\\\":{\\\"outputs\\\":[\\\"Output\\\",\\\"Output.result\\\",\\\"Output.result.aaa\\\",\\\"Output.result.bb\\\",\\\"Output.result2\\\"],\\\"inputs\\\":[\\\"input\\\",\\\"arrarr\\\"]},\\\"isHovering\\\":false,\\\"isParallel\\\":false,\\\"source\\\":true,\\\"target\\\":true,\\\"debug\\\":null,\\\"error\\\":false,\\\"output\\\":[{\\\"id\\\":\\\"3e79d81d-78e5-aeb0-5a85-567954684b11\\\",\\\"value\\\":\\\"Output\\\",\\\"label\\\":\\\"Output\\\",\\\"_uiId\\\":\\\"a12efcf2-18fe-98a4-fdd8-063f429de5d3\\\",\\\"type\\\":\\\"OBJECT\\\",\\\"children\\\":[{\\\"id\\\":\\\"c3e020aa-f147-27cc-64b9-ee795c5632fb\\\",\\\"value\\\":\\\"result\\\",\\\"label\\\":\\\"result\\\",\\\"_uiId\\\":\\\"09208fe5-368e-a02d-fd19-db6f6f764fbf\\\",\\\"type\\\":\\\"OBJECT\\\",\\\"children\\\":[{\\\"id\\\":\\\"4cba8343-a4ea-839a-de60-e043920351ec\\\",\\\"value\\\":\\\"aaa\\\",\\\"label\\\":\\\"aaa\\\",\\\"_uiId\\\":\\\"806dd385-0fdb-acbf-3844-f2567d46953d\\\",\\\"type\\\":\\\"STRING\\\",\\\"children\\\":[]},{\\\"id\\\":\\\"38ac6193-6b23-e50a-760e-cf64831c0b67\\\",\\\"value\\\":\\\"bb\\\",\\\"label\\\":\\\"bb\\\",\\\"_uiId\\\":\\\"0a8908cb-f21f-8904-df90-32c7fcd51aff\\\",\\\"type\\\":\\\"STRING\\\",\\\"children\\\":[]}]},{\\\"id\\\":\\\"c00d6733-c70d-5fa6-7121-e77f857256ed\\\",\\\"value\\\":\\\"result2\\\",\\\"label\\\":\\\"result2\\\",\\\"_uiId\\\":\\\"a111c802-bd28-5f6f-cefa-25e2fa198311\\\",\\\"type\\\":\\\"INT\\\",\\\"children\\\":[]}]}],\\\"schema\\\":null,\\\"checkDataError\\\":0},\\\"position\\\":{\\\"x\\\":776,\\\"y\\\":563},\\\"targetPosition\\\":\\\"left\\\",\\\"sourcePosition\\\":\\\"right\\\",\\\"selected\\\":false,\\\"measured\\\":{\\\"width\\\":250,\\\"height\\\":124},\\\"dragging\\\":false}\", \"ExceptionHandling\":{\"Switch\":\"OFF\", \"MaxRetries\":\"3\", \"RetryInterval\":\"1\", \"AbnormalOutputResult\":\"\", \"HandleMethod\":\"EXCEPTION_OUTPUT\", \"NextNodeIDs\":[]}}], \"Edge\":\"[{\\\"source\\\":\\\"11a76786-2578-8f2e-ab4e-96fbe393b750\\\",\\\"target\\\":\\\"4bb28c02-c142-4885-958b-e700c88d05e1\\\",\\\"sourceHandle\\\":\\\"11a76786-2578-8f2e-ab4e-96fbe393b750-source\\\",\\\"type\\\":\\\"custom\\\",\\\"data\\\":{\\\"connectedNodeIsHovering\\\":false,\\\"error\\\":false,\\\"isHovering\\\":false},\\\"id\\\":\\\"xy-edge__11a76786-2578-8f2e-ab4e-96fbe393b75011a76786-2578-8f2e-ab4e-96fbe393b750-source-4bb28c02-c142-4885-958b-e700c88d05e1\\\",\\\"animated\\\":false,\\\"selected\\\":false},{\\\"source\\\":\\\"4bb28c02-c142-4885-958b-e700c88d05e1\\\",\\\"sourceHandle\\\":\\\"4bb28c02-c142-4885-958b-e700c88d05e1-source\\\",\\\"target\\\":\\\"88753333-e45b-fdd4-2aa3-7660998fbb91\\\",\\\"targetHandle\\\":\\\"88753333-e45b-fdd4-2aa3-7660998fbb91-target\\\",\\\"type\\\":\\\"custom\\\",\\\"data\\\":{\\\"connectedNodeIsHovering\\\":false,\\\"error\\\":false,\\\"isHovering\\\":false},\\\"id\\\":\\\"xy-edge__4bb28c02-c142-4885-958b-e700c88d05e14bb28c02-c142-4885-958b-e700c88d05e1-source-88753333-e45b-fdd4-2aa3-7660998fbb9188753333-e45b-fdd4-2aa3-7660998fbb91-target\\\",\\\"animated\\\":false,\\\"selected\\\":false},{\\\"source\\\":\\\"11a76786-2578-8f2e-ab4e-96fbe393b750\\\",\\\"sourceHandle\\\":\\\"11a76786-2578-8f2e-ab4e-96fbe393b750-source\\\",\\\"target\\\":\\\"578d6b2e-d334-1df1-c512-551c358fb790\\\",\\\"targetHandle\\\":\\\"578d6b2e-d334-1df1-c512-551c358fb790-target\\\",\\\"type\\\":\\\"custom\\\",\\\"data\\\":{\\\"connectedNodeIsHovering\\\":false,\\\"error\\\":false,\\\"isHovering\\\":false},\\\"id\\\":\\\"xy-edge__11a76786-2578-8f2e-ab4e-96fbe393b75011a76786-2578-8f2e-ab4e-96fbe393b750-source-578d6b2e-d334-1df1-c512-551c358fb790578d6b2e-d334-1df1-c512-551c358fb790-target\\\",\\\"animated\\\":false,\\\"selected\\\":false},{\\\"source\\\":\\\"578d6b2e-d334-1df1-c512-551c358fb790\\\",\\\"sourceHandle\\\":\\\"578d6b2e-d334-1df1-c512-551c358fb790-source\\\",\\\"target\\\":\\\"88753333-e45b-fdd4-2aa3-7660998fbb91\\\",\\\"targetHandle\\\":\\\"88753333-e45b-fdd4-2aa3-7660998fbb91-target\\\",\\\"type\\\":\\\"custom\\\",\\\"data\\\":{\\\"connectedNodeIsHovering\\\":false,\\\"error\\\":false,\\\"isHovering\\\":false},\\\"id\\\":\\\"xy-edge__578d6b2e-d334-1df1-c512-551c358fb790578d6b2e-d334-1df1-c512-551c358fb790-source-88753333-e45b-fdd4-2aa3-7660998fbb9188753333-e45b-fdd4-2aa3-7660998fbb91-target\\\",\\\"animated\\\":false,\\\"selected\\\":false}]\", \"Mode\":\"NORMAL\", \"ReleaseTime\":\"\"}",
            "EndTime": "1759142312152",
            "FailMessage": "",
            "MainModelName": "cs-normal-70b",
            "Name": "代码",
            "Output": "{\"output\": 22}",
            "Query": "22",
            "RunEnv": 0,
            "StartTime": "1759142309058",
            "State": 2,
            "TotalTokens": 0,
            "WorkflowId": "47d7c1f7-501b-465a-aa6a-73846c92ca44",
            "WorkflowRunId": "wfr-asaodefdu7pc"
        }
    }
}
```

