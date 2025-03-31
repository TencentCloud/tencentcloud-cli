**Example 1: 开启云端录制**



Input: 

```
tccli trro CreateCloudRecording --cli-unfold-argument  \
    --DeviceId dev1 \
    --ProjectId m82k5408n123phvb \
    --OutputFormat 3 \
    --VideoStreamId 0 \
    --MaxMediaFileDuration 20 \
    --MaxIdleTime 20 \
    --CloudStorage.Vendor 0 \
    --CloudStorage.Bucket recording-1304123456 \
    --CloudStorage.Region ap-nanjing \
    --CloudStorage.AccessKey accesskey-test \
    --CloudStorage.SecretKey secretkey-test \
    --CloudStorage.FileNamePrefix 2024-12-24 dev1
```

Output: 
```
{
    "Response": {
        "TaskId": "-gCTFWtU7t7DUlo7A8IswFszO9z2O-rbERqJAoK-4pycoZXKjIAAnasdcasdOEycyX4CnzhIm4RAQ..",
        "RequestId": "71993312-6ab8-4768-9124-118e0a20c45f"
    }
}
```

