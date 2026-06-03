**Example 1: 调用 TWeSee 图片理解算法**



Input: 

```
tccli iotexplorer InvokeTWeSeeComprehension --cli-unfold-argument  \
    --InputURL https://****-test-125*****22.cos.ap-guangzhou.myqcloud.com/********.jpg \
    --ServiceType IMG_COMP \
    --WaitResultTimeout 20 \
    --CallbackId cb-n9sl1wur
```

Output: 
```
{
    "Response": {
        "ComprehensionResult": {
            "DetectedClassifications": [
                "cat"
            ],
            "Summary": "一只猫坐在吉他盒里，旁边有只小鸟飞过"
        },
        "CostAdvanced": 0,
        "CostBasic": 1,
        "Status": 3,
        "TaskId": "comp-12e89917-c932-c27d-977f-bd16cc5c3b92",
        "RequestId": "2063f9bf-ecad-499c-8f03-220c911385e9"
    }
}
```

**Example 2: 调用 TWeSee 视频理解算法**



Input: 

```
tccli iotexplorer InvokeTWeSeeComprehension --cli-unfold-argument  \
    --InputURL https://*********-125*******.cos.ap-guangzhou.tencentcos.cn/*******.mp4 \
    --ServiceType VID_COMP
```

Output: 
```
{
    "Response": {
        "ComprehensionResult": {
            "DetectedClassifications": [
                "person"
            ],
            "Summary": "穿浅色衣物的人在湿滑路边行走"
        },
        "CostAdvanced": 0,
        "CostBasic": 1,
        "Status": 3,
        "TaskId": "comp-8c47f42e-c9fd-3e6a-a0c5-64da344c013d",
        "RequestId": "2d126014-5991-490d-8f4a-75991ad5871e"
    }
}
```

**Example 3: 调用 TWeSee 视频理解算法（含高级功能）**

对该视频生效视频搜索高级功能

Input: 

```
tccli iotexplorer InvokeTWeSeeComprehension --cli-unfold-argument  \
    --InputURL https://kero-test-1255707222.cos.ap-guangzhou.tencentcos.cn/jiwei/4.mp4 \
    --ServiceType VID_COMP \
    --ComprehensionConfig.EnableSearch True
```

Output: 
```
{
    "Response": {
        "ComprehensionResult": {
            "DetectedClassifications": [
                "person"
            ],
            "Summary": "穿浅色衣物的人在雨后湿滑的路边行走"
        },
        "CostAdvanced": 1,
        "CostBasic": 1,
        "Status": 3,
        "TaskId": "comp-c01e4d7f-2bf5-3e6e-e865-bc495b954b23",
        "RequestId": "296e405d-fe5f-4ed0-a2c4-f34fd70f4ab2"
    }
}
```

