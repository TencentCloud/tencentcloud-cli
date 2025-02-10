**Example 1: 停止云端录制**

停止SdkAppId 为 1400188366, TaskId 为 -m9-bVVU7gzdSqvsV***Y+QMYNee2QE. 的云端录制。

Input: 

```
tccli trtc DeleteCloudRecording --cli-unfold-argument  \
    --TaskId -m9-bVVU7gzdSqvsV***Y+QMYNee2QE. \
    --SdkAppId 1400188366
```

Output: 
```
{
    "Response": {
        "TaskId": "-m9-bVVU7gzdSqvsV***Y+QMYNee2QE.",
        "RequestId": "71993312-6ab8-4768-9124-118e0a20c45f"
    }
}
```

