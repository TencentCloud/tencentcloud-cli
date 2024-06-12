**Example 1: 查询EMR任务运行详情状态**



Input: 

```
tccli emr DescribeClusterFlowStatusDetail --cli-unfold-argument  \
    --InstanceId abc \
    --FlowParam.FKey abc \
    --FlowParam.FValue abc \
    --NeedExtraDetail True
```

Output: 
```
{
    "Response": {
        "StageDetails": [
            {
                "Stage": "abc",
                "Name": "abc",
                "IsShow": true,
                "IsSubFlow": true,
                "SubFlowFlag": "abc",
                "Status": 0,
                "Desc": "abc",
                "Progress": 0,
                "Starttime": "2020-09-22 00:00:00",
                "Endtime": "2020-09-22 00:00:00",
                "HadWoodDetail": true,
                "WoodJobId": 1,
                "LanguageKey": "abc",
                "FailedReason": "abc",
                "TimeConsuming": "abc"
            }
        ],
        "FlowDesc": [
            {
                "PKey": "abc",
                "PValue": "abc"
            }
        ],
        "FlowName": "abc",
        "FlowTotalProgress": 0,
        "FlowTotalStatus": 0,
        "FlowExtraDetail": [
            {
                "Title": "abc",
                "Detail": [
                    {
                        "PKey": "abc",
                        "PValue": "abc"
                    }
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

