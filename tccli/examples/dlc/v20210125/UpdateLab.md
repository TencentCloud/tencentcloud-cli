**Example 1: UpdateLab**

更新实验室配置

Input: 

```
tccli dlc UpdateLab --cli-unfold-argument  \
    --Name leionwu \
    --LabImage ccr.ccs.tencentyun.com/emr-image/tcray:2.55.1-py311-cpu-lab \
    --Description 测试测试测试 \
    --Image ccr.ccs.tencentyun.com/emr-image/tcray:2.55.1-py311-cpu \
    --ImagePullPolicy Always \
    --ResourceConfigId 11 \
    --GroupId rayclustergroup-tfh4u6-bcqz \
    --ResourcePartitionId dlc-p-bleurqnv \
    --Queue default \
    --ExampleId rayclustergroup-tfh4u6-bcqz \
    --CodeArchiveUrl https://common-job-packages-251233710.cos.ap-guangzhou.myqcloud.com/models/examples/example-001-ray-core-basics.zip \
    --LabImagePullPolicy Always \
    --Priority 7 \
    --EnableToken False \
    --PersistentWorkDir.Enabled False
```

Output: 
```
{
    "Response": {
        "AppId": 260200065,
        "CodeArchiveUrl": "https://common-job-packages-251233710.cos.ap-guangzhou.myqcloud.com/models/examples/example-001-ray-core-basics.zip",
        "Description": "测试测试测试",
        "EnableToken": false,
        "ExampleId": "rayclustergroup-tfh4u6-bcqz",
        "GroupId": "rayclustergroup-tfh4u6-bcqz",
        "Id": "raylab-20260602161511-uu7l",
        "Image": "ccr.ccs.tencentyun.com/emr-image/tcray:2.55.1-py311-cpu",
        "ImagePullPolicy": "Always",
        "LabImage": "ccr.ccs.tencentyun.com/emr-image/tcray:2.55.1-py311-cpu-lab",
        "LabImagePullPolicy": "Always",
        "Name": "leionwu",
        "PersistentWorkDir": {
            "Enabled": false
        },
        "Priority": 7,
        "Queue": "default",
        "ResourceConfig": "{\"Head\":null,\"Worker\":null}",
        "ResourceConfigId": "11",
        "ResourcePartitionId": "dlc-p-bleurqnv",
        "ResourcePartitionName": "test_andrewmao",
        "Services": [
            {
                "Key": "JUPYTER"
            }
        ],
        "Status": "FAILED",
        "Type": "RAY_CLUSTER",
        "Uin": "700002655693",
        "RequestId": "e403bf2d-7a6c-4a76-b609-26d7441e9ec6"
    }
}
```

