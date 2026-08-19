**Example 1: 1**



Input: 

```
tccli csip DescribeClusterContainerDetail --cli-unfold-argument  \
    --ContainerId 1ea61132******************a320a93772*****************2fd66091e4d \
    --MemberId mem-tencent-********2f66e429
```

Output: 
```
{
    "Response": {
        "AppID": 260083796,
        "ClusterCaMD5": "814fe16************f9129471e26ae",
        "Cmd": "",
        "ContainerId": "1ea611******************efa320a937724ebaca98fb413c6082fd66091e4d",
        "ContainerName": "yunjing-agent",
        "CreateTime": "2026-07-29T11:43:52+08:00",
        "ImageCreateTime": "2026-07-22T20:03:36+08:00",
        "ImageId": "sha256:94cc7bb42e2b7e536778b404262db678f09a4167773cc62ec4834a55dd625645",
        "ImageName": "ccr.ccs.tencentyun.com/yunjing_agent/agent:dev-latest",
        "ImageSize": "36.28MB",
        "IsolateStatus": "NORMAL",
        "Mounts": [],
        "NodeInstanceId": "eks-3pwtyur9",
        "NodeInternalIP": "172.16.0.224",
        "NodeName": "cls-pde9e0s0_np-7i5wo9qa-cwvq7",
        "NodeRunStatus": "Running",
        "NodeType": "WORKER",
        "NodeUniqueID": "ef616f81***************e824b4502",
        "RunStatus": "RUNNING",
        "RequestId": "680bbd5f-8f84-4b47-81fa-f6778b86dccc"
    }
}
```

