**Example 1: 调用示例1**



Input: 

```
tccli trro DescribeAnnotationResults --cli-unfold-argument  \
    --TaskId 3uimegtqfkfv_1
```

Output: 
```
{
    "Response": {
        "CreateTime": "1788345644",
        "ErrorMsg": "",
        "FileName": "1qLIfbvfNo_0003.mp4",
        "FinishTime": "1788345702",
        "Result": "{\"schema\": \"fine4.semantic\", \"version\": \"1.0\", \"overview\": {\"video_id\": \"1qLIfbvfNo_0003\", \"video_path\": \"/data/ann_videos/3uimegtqfkfv_1/1qLIfbvfNo_0003.mp4\", \"task_goal\": \"检查并手动旋转自行车脚踏板以测试传动系统\", \"duration_s\": 8.133, \"fps\": 30.0, \"w\": 1280, \"h\": 720, \"n_subtasks\": 2, \"n_actions\": 3, \"n_atomic\": 4, \"n_scenes\": 1, \"key_objects\": [\"手\", \"工具\", \"自行车\", \"脚踏板\"], \"injected_context\": {\"task_goal\": \"标注视频中的手部操作动作\", \"key_objects\": [\"手\", \"工具\"], \"atomic_verbs\": [\"拿取\", \"放置\"]}, \"scenes\": [{\"scene_idx\": 0, \"start\": 0.0, \"end\": 8.133, \"start_frame\": 0, \"end_frame\": 244, \"n_frames\": 244}]}, \"subtasks\": [{\"idx\": 0, \"title\": \"伸手接近并接触自行车脚踏板\", \"start\": 0.0, \"end\": 0.8, \"actions\": [{\"idx\": 0, \"verb\": \"reach\", \"object_labels\": [\"脚踏板\"], \"desc_hand_centric\": \"右手快速伸向脚踏板，左手在旁辅助移动\", \"desc_object_centric\": \"手部接近静止的自行车脚踏板\", \"start\": 0.0, \"end\": 0.8, \"atomic_actions\": [{\"idx\": 0, \"start\": 0.0, \"end\": 0.8, \"verb\": \"reach\", \"object_labels\": [\"脚踏板\"], \"desc_hand_centric\": \"右手快速伸向脚踏板，左手在旁辅助移动\", \"desc_object_centric\": \"手部接近静止的自行车脚踏板\", \"relations\": [], \"relation_events\": []}]}]}, {\"idx\": 1, \"title\": \"抓握并旋转脚踏板进行测试\", \"start\": 0.8, \"end\": 8.133, \"actions\": [{\"idx\": 0, \"verb\": \"grasp\", \"object_labels\": [\"脚踏板\"], \"desc_hand_centric\": \"右手抓住脚踏板，左手在画面外或未参与\", \"desc_object_centric\": \"脚踏板被手抓握准备旋转\", \"start\": 0.8, \"end\": 4.0, \"atomic_actions\": [{\"idx\": 1, \"start\": 0.8, \"end\": 2.0, \"verb\": \"grasp\", \"object_labels\": [\"脚踏板\"], \"desc_hand_centric\": \"右手抓住脚踏板，左手在画面外或未参与\", \"desc_object_centric\": \"脚踏板被手抓握准备旋转\", \"relations\": [], \"relation_events\": []}, {\"idx\": 2, \"start\": 2.0, \"end\": 4.0, \"verb\": \"rotate\", \"object_labels\": [\"脚踏板\"], \"desc_hand_centric\": \"右手持续转动脚踏板，带动链条运动\", \"desc_object_centric\": \"脚踏板在手作用下旋转，后轮随之转动\", \"relations\": [], \"relation_events\": []}]}, {\"idx\": 1, \"verb\": \"rotate\", \"object_labels\": [\"脚踏板\"], \"desc_hand_centric\": \"右手持续转动脚踏板，带动链条运动\", \"desc_object_centric\": \"脚踏板在手作用下旋转，后轮随之转动\", \"start\": 4.0, \"end\": 8.133, \"atomic_actions\": [{\"idx\": 3, \"start\": 4.0, \"end\": 8.133, \"verb\": \"release\", \"object_labels\": [\"脚踏板\"], \"desc_hand_centric\": \"右手松开脚踏板，双手逐渐移出画面\", \"desc_object_centric\": \"脚踏板停止旋转，恢复静止状态\", \"relations\": [], \"relation_events\": []}]}]}]}",
        "ResultSize": 2741,
        "Status": 6,
        "TaskId": "3uimegtqfkfv_1",
        "RequestId": "3ec3f1d6-300d-4ef4-9d79-02ed43290167"
    }
}
```

**Example 2: 调用示例2**



Input: 

```
tccli trro DescribeAnnotationResults --cli-unfold-argument  \
    --TaskId 3ufx9vwq22ms_1
```

Output: 
```
{
    "Response": {
        "CreateTime": "1788182323",
        "ErrorMsg": "manual set for retry test",
        "FileName": "1qLIfbvfNo_0003.mp4",
        "FinishTime": "1788182330",
        "Result": "",
        "ResultSize": 0,
        "Status": 4,
        "TaskId": "3ufx9vwq22ms_1",
        "RequestId": "3588b486-116c-43cf-9267-b337c09465f0"
    }
}
```

