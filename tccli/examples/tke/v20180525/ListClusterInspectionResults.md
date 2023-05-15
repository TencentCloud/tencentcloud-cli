**Example 1: 获取集群巡检诊断结果示例1**

获取集群巡检诊断结果，不隐藏结果

Input: 

```
tccli tke ListClusterInspectionResults --cli-unfold-argument  \
    --ClusterIds cls-dsff \
    --Hide  \
    --Name default-123456
```

Output: 
```
{
    "Response": {
        "InspectionResults": [
            {
                "ClusterId": "cls-dsff",
                "Diagnostics": [
                    {
                        "Catalogues": [
                            {},
                            {}
                        ],
                        "Desc": "check master capacity",
                        "EndTime": "2022-11-11 06:41:23 +0000 UTC",
                        "Name": "master-capacity-update",
                        "Results": [
                            {
                                "Desc": "Master Capacity Check",
                                "Level": "failed",
                                "ObjInfo": [
                                    {}
                                ],
                                "ObjName": "pod-dsafasf",
                                "Proposal": "",
                                "Title": "Master Capacity Check"
                            }
                        ],
                        "StartTime": "2022-11-11 06:41:23 +0000 UTC",
                        "Statistics": [],
                        "Type": "master-capacity"
                    }
                ],
                "EndTime": "2022-11-11 06:31:23 +0000 UTC",
                "StartTime": "2022-11-11 06:41:23 +0000 UTC",
                "Statistics": [
                    {},
                    {},
                    {},
                    {}
                ]
            }
        ],
        "RequestId": "kubejarvis-test-case1"
    }
}
```

**Example 2: 获取集群巡检诊断结果示例2**

获取集群巡检诊断结果，隐藏结果

Input: 

```
tccli tke ListClusterInspectionResults --cli-unfold-argument  \
    --ClusterIds cls-dsff \
    --Hide results \
    --Name default-123456
```

Output: 
```
{
    "Response": {
        "InspectionResults": [
            {
                "ClusterId": "cls-dsff",
                "Diagnostics": [
                    {
                        "Catalogues": [
                            {},
                            {}
                        ],
                        "Desc": "check master capacity",
                        "EndTime": "2022-11-11 06:41:23 +0000 UTC",
                        "Name": "master-capacity-update",
                        "Results": null,
                        "StartTime": "2022-11-11 06:41:23 +0000 UTC",
                        "Statistics": [],
                        "Type": "master-capacity"
                    }
                ],
                "EndTime": "2022-11-11 06:31:23 +0000 UTC",
                "StartTime": "2022-11-11 06:41:23 +0000 UTC",
                "Statistics": [
                    {},
                    {},
                    {},
                    {}
                ]
            }
        ],
        "RequestId": "kubejarvis-test-case2"
    }
}
```

