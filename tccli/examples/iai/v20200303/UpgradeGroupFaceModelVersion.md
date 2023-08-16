**Example 1: 人员库升级**



Input: 

```
tccli iai UpgradeGroupFaceModelVersion --cli-unfold-argument  \
    --GroupId 1001 \
    --FaceModelVersion 3.0
```

Output: 
```
{
    "Response": {
        "JobId": "251007453_upgrade_group_qta_1596529493_gjwh07X7",
        "RequestId": "d1388dbb-c9f0-4b7a-8528-ebf61f718e67"
    }
}
```

**Example 2: 升级失败**

当人员库存在一些无法升级的人脸时，返回FailedOperation.GroupLostFaces错误，并返回一个Url查看具体的PersonId和FaceId，需要删除这些Person或Face，或者重新创建，才可以升级成功。
文件格式：
[{
            person_id: 丢失的人员ID,
            face_id: 丢失的人脸ID,
            type: 1    // 丢图类型，1. 未知原因，暂无其它类别
}]

Input: 

```
tccli iai UpgradeGroupFaceModelVersion --cli-unfold-argument  \
    --GroupId 1002 \
    --FaceModelVersion 3.0
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.GroupLostFaces",
            "Message": "人员库中人脸图片丢失，详情可参见https://iaiface-upgradegroup-failedface-1254418846.cos.ap-guangzhou.myqcloud.com/1253657503/1002.json"
        },
        "RequestId": "3ad7ccb4-29b5-46b4-adcd-69fd6728d530"
    }
}
```

