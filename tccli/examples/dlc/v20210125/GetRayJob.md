**Example 1: 获取job详情**



Input: 

```
tccli dlc GetRayJob --cli-unfold-argument  \
    --Id rayjob-1773664701-twd4
```

Output: 
```
{
    "Response": {
        "AppId": 260090589,
        "Catalog": "{\"CFSVolumes\":[],\"COSVolumes\":[]}",
        "CreateTime": 1773664702002,
        "Entrypoint": "sleep1",
        "ErrorMessage": "Job entrypoint command failed with exit code 127, last available logs (truncated to 20,000 chars):\n2026-03-16 20:39:14,666\tINFO job_manager.py:587 -- Runtime env is setting up.\nRunning entrypoint for job rayjob-1773664701-twd4-v6tz8: sleep1\n/bin/sh: 1: sleep1: not found\n",
        "FinishTime": 1773664763806,
        "HistoryUrl": "https://test-history-server.tcray.woa.com/history/kuberay-system/rayjob-1773664701-twd4/",
        "Id": "rayjob-1773664701-twd4",
        "Image": "ccr.ccs.tencentyun.com/emr-image/tcray:3.0.0.dev0-py311-cpu",
        "ImagePullPolicy": "IfNotPresent",
        "JobName": "rayjob-1773664701-twd4",
        "Queue": "default",
        "ResourceConfig": "{\"Head\":{\"Name\":\"default-head\",\"PodCpu\":1,\"PodMem\":2,\"PodNum\":1,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[]},\"Worker\":[{\"Name\":\"default-worker\",\"PodCpu\":1,\"PodMem\":2,\"MinPodNum\":1,\"MaxPodNum\":1,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[]}]}",
        "ResourcePartitionId": "dlc-p-mock0001",
        "RunningTime": 61225,
        "Status": "FAILED",
        "SubAccountUin": "700002467852",
        "Uin": "700002467852",
        "RequestId": "4f003913-0bd8-452b-a0d8-c4965b42d455"
    }
}
```

