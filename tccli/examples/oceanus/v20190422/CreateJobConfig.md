**Example 1: 新建Jar作业配置示例**

创建一个Jar作业配置

Input: 

```
tccli oceanus CreateJobConfig --cli-unfold-argument  \
    --ProgramArgs 2000 \
    --EntrypointClass com.tencent.flink.test.WordCount \
    --JobId cql-n8yaia0y
```

Output: 
```
{
    "Response": {
        "Version": 2,
        "RequestId": "5f124d6f-b035-4d29-9467-dd62eccdbf23"
    }
}
```

**Example 2: 创建SQL作业配置示例**

创建SQL作业配置，
其中ProgramArgs参数包括了大量的入参，SqlCode 、Metadata 都采用了base64加密

Input: 

```
tccli oceanus CreateJobConfig --cli-unfold-argument  \
    --JobId cql-5kmc4o48 \
    --ProgramArgs {"CheckpointInterval":600,"Metadata":"eyJNZXRhZGF0YSI6eyJSZWZlcmVuY2VUYWJsZXMiOltdLCJWYXJpYWJsZXMiOltdfX0=","SqlCode":"CkNSRUFURSBUQUJMRSBgRGF0YV9JbnB1dGAgKCAtLeatpemqpCAxIO+8muWIm+W7uuaVsOaNrua6kOihqO+8iFNvdXJjZe+8iSBEYXRhX0lucHV0CiAgICBhZ2UgQklHSU5ULAogICAgc2NvcmUgQklHSU5UCikgV0lUSCAoCiAgICAnY29ubmVjdG9yJyA9ICdkYXRhZ2VuJywKICAgICdyb3dzLXBlci1zZWNvbmQnPScxMDAnLCAgICAgICAgICAtLSDmr4/np5LkuqfnlJ/nmoTmlbDmja7mnaHmlbAKCiAgICAnZmllbGRzLmFnZS5raW5kJz0ncmFuZG9tJywgICAgICAgLS0g5peg55WM55qE6ZqP5py65pWwCiAgICAnZmllbGRzLmFnZS5taW4nPScxJywgICAgICAgICAgIC0tIOmaj+acuuaVsOeahOacgOWwj+WAvAogICAgJ2ZpZWxkcy5hZ2UubWF4Jz0nMTAwJywgICAgICAgICAtLSDpmo/mnLrmlbDnmoTmnIDlpKflgLwKCiAgICAnZmllbGRzLnNjb3JlLmtpbmQnPSdyYW5kb20nLCAgICAgICAgLS0g5peg55WM55qE6ZqP5py65pWwCiAgICAnZmllbGRzLnNjb3JlLm1pbic9JzEnLCAgICAgICAgICAgICAgLS0g6ZqP5py65pWw55qE5pyA5bCP5YC8CiAgICAnZmllbGRzLnNjb3JlLm1heCc9JzEwMDAnICAgICAgICAgICAgLS0g6ZqP5py65pWw55qE5pyA5aSn5YC8Cik7CgpDUkVBVEUgVEFCTEUgYERhdGFfT3V0cHV0YCAoIC0t5q2l6aqkIDIg77ya5Yib5bu65pWw5o2u57uT5p6c6KGo77yIU2lua++8iSBEYXRhX091dHB1dAogICAgYGF2Z19hZ2VgIEJJR0lOVCwKICAgIGBhdmdfc2NvcmVgIEJJR0lOVAopIFdJVEggKAogICAgJ2Nvbm5lY3RvcicgPSAnYmxhY2tob2xlJwopOwoKSU5TRVJUIElOVE8gYERhdGFfT3V0cHV0YCAgIC0t5q2l6aqkIDMg77yaIOWwhuaVsOaNrua6kOihqO+8iFNvdXJjZe+8iSBEYXRhX0lucHV0IOS4reeahCBhZ2Ug5ZKMIHNjb3JlIOWPluW5s+Wdh+aVsOS5i+WQjuWtmOWCqOS6juaVsOaNrue7k+aenOihqO+8iFNpbmvvvIkgRGF0YV9PdXRwdXQKU0VMRUNUIEFWRyhhZ2UpLCBBVkcoc2NvcmUpIEZST00gYERhdGFfSW5wdXRgOwo="} \
    --Remark v2 \
    --DefaultParallelism 1 \
    --Properties.0.Key pipeline.max-parallelism \
    --Properties.0.Value 2048 \
    --LogCollect True \
    --ClsLogsetId 10981e21-aee9-4a01-9ed9-eadf5956fe3c \
    --ClsTopicId 544002e3-299b-41d2-b18f-19194fb0660b \
    --LogCollectType 2 \
    --WorkSpaceId space-1257058945ap-guangzhou \
    --LogLevel INFO \
    --AutoRecover 1 \
    --ExpertModeOn False \
    --TraceModeOn False \
    --CheckpointRetainedNum 0 \
    --EsServerlessIndex  \
    --EsServerlessSpace  \
    --FlinkVersion Flink-1.16 \
    --JobManagerCpu 1 \
    --JobManagerMem 4 \
    --TaskManagerCpu 1 \
    --TaskManagerMem 4
```

Output: 
```
{
    "Response": {
        "RequestId": "8f152cf4-9a43-40fa-a2ea-f28e74cd24ff",
        "Version": 3
    }
}
```

**Example 3: 创建Python作业配置示例**

创建python作业配置示例

Input: 

```
tccli oceanus CreateJobConfig --cli-unfold-argument  \
    --JobId cql-68w5vlip \
    --EntrypointClass com.tencent.cloud.oceanus.wordcount.WordCount \
    --ProgramArgs  \
    --Remark v1 \
    --ResourceRefs.0.ResourceId resource-lbi8h92t \
    --ResourceRefs.0.Version 1 \
    --ResourceRefs.0.Type 1 \
    --DefaultParallelism 1 \
    --Properties.0.Key pipeline.max-parallelism \
    --Properties.0.Value 2048 \
    --LogCollect True \
    --ClsLogsetId 10981e21-aee9-4a01-9ed9-eadf5956fe3c \
    --ClsTopicId 544002e3-299b-41d2-b18f-19194fb0660b \
    --LogCollectType 2 \
    --PythonVersion Python-3.7 \
    --WorkSpaceId space-1257058945ap-guangzhou \
    --LogLevel INFO \
    --AutoRecover 1 \
    --ExpertModeOn False \
    --TraceModeOn False \
    --CheckpointRetainedNum 0 \
    --EsServerlessIndex  \
    --EsServerlessSpace  \
    --FlinkVersion Flink-1.13 \
    --JobManagerCpu 0 \
    --JobManagerMem 0 \
    --TaskManagerCpu 0 \
    --TaskManagerMem 0
```

Output: 
```
{
    "Response": {
        "RequestId": "8b4433c9-3efc-4afc-a2bd-78d682f5c3dd",
        "Version": 2
    }
}
```

