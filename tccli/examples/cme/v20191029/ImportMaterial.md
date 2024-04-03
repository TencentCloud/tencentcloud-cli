**Example 1: 导入云点播媒体到团队**

 

Input: 

```
tccli cme ImportMaterial --cli-unfold-argument  \
    --Platform test \
    --SourceType VOD \
    --VodFileId 5285890796182734267 \
    --Owner.Id cmetid_37b1bb3bf8fb2eb3ba00e41dcca0ce \
    --Owner.Type TEAM \
    --Name 媒体名称 \
    --ClassPath /媒体 \
    --Operator user_id_0a54392053f84053942f930
```

Output: 
```
{
    "Response": {
        "MaterialId": "3dfd8ad3d628dc30001bd09dd6",
        "PreProcessTaskId": "",
        "RequestId": "0a543920-53f8-4053-942f-9308c49404d30"
    }
}
```

**Example 2: 导入云点播文件到个人**

 

Input: 

```
tccli cme ImportMaterial --cli-unfold-argument  \
    --Platform test \
    --SourceType VOD \
    --VodFileId 528589079618273426711 \
    --Owner.Id user_id_0a54392053f84053942f930 \
    --Owner.Type PERSON \
    --Name 媒体名称 \
    --ClassPath /媒体
```

Output: 
```
{
    "Response": {
        "MaterialId": "3dfd8ad3d628dc30001bd09dd5",
        "PreProcessTaskId": "",
        "RequestId": "0a543920-53f8-4053-942f-9308c49404d7"
    }
}
```

**Example 3: 导入外部媒体到个人并发起预处理**

导入一个  COS 桶中媒体到个人，且发起预处理。

Input: 

```
tccli cme ImportMaterial --cli-unfold-argument  \
    --Platform test \
    --SourceType EXTERNAL \
    --Owner.Id user_id_0a54392053f84053942f930 \
    --Owner.Type PERSON \
    --Name 媒体名称 \
    --ClassPath /媒体 \
    --ExternalMediaInfo.MediaKey example-folder/example-object.mp4 \
    --PreProcessDefinition 10 \
    --Operator user_id_0a54392053f84053942f930
```

Output: 
```
{
    "Response": {
        "MaterialId": "3dfd8ad3d628dc30001bd09dd9",
        "PreProcessTaskId": "125xxxxxxx9-tfusion-0a54392053f84053942f93089kji3d3",
        "RequestId": "0a543920-53f8-4053-942f-9308c49408kd8"
    }
}
```

**Example 4: 导入外部媒体到团队并发起预处理**

导入一个  COS 桶中媒体到团队，且发起预处理。

Input: 

```
tccli cme ImportMaterial --cli-unfold-argument  \
    --Platform test \
    --SourceType EXTERNAL \
    --Owner.Id cmetid_37b1bb3bf8fb2eb3ba00e41dcca0ce \
    --Owner.Type TEAM \
    --Name 媒体名称 \
    --ClassPath /媒体 \
    --ExternalMediaInfo.MediaKey example-folder/example-object.mp4 \
    --PreProcessDefinition 10 \
    --Operator user_id_0a54392053f84053942f930
```

Output: 
```
{
    "Response": {
        "MaterialId": "3dfd8ad3d628dc30001bd09da0",
        "PreProcessTaskId": "125xxxxxxx9-tfusion-0a54392053f84053942f93089kji3d4",
        "RequestId": "0a543920-53f8-4053-942f-9308c49409634"
    }
}
```

**Example 5: 导入云点播媒体到团队并发起预处理**

 

Input: 

```
tccli cme ImportMaterial --cli-unfold-argument  \
    --Platform test \
    --SourceType VOD \
    --VodFileId 5285890796182734267 \
    --Owner.Id cmetid_37b1bb3bf8fb2eb3ba00e41dcca0ce \
    --Owner.Type TEAM \
    --Name 媒体名称 \
    --ClassPath /媒体 \
    --PreProcessDefinition 10 \
    --Operator user_id_0a54392053f84053942f930
```

Output: 
```
{
    "Response": {
        "MaterialId": "3dfd8ad3d628dc30001bd09dd6",
        "PreProcessTaskId": "125xxxxxxx9-tfusion-0a54392053f84053942f9308978d3",
        "RequestId": "0a543920-53f8-4053-942f-9308c49404d30"
    }
}
```

**Example 6: 导入云点播文件到个人并发起预处理**

 

Input: 

```
tccli cme ImportMaterial --cli-unfold-argument  \
    --Platform test \
    --SourceType VOD \
    --VodFileId 528589079618273426711 \
    --Owner.Id user_id_0a54392053f84053942f930 \
    --Owner.Type PERSON \
    --Name 媒体名称 \
    --ClassPath /媒体 \
    --PreProcessDefinition 10 \
    --Operator user_id_0a54392053f84053942f930
```

Output: 
```
{
    "Response": {
        "MaterialId": "3dfd8ad3d628dc30001bd09dd6",
        "PreProcessTaskId": "125xxxxxxx9-tfusion-0a54392053f84053942f9308c49404d8",
        "RequestId": "0a738920-53f8-4053-942f-9308c494099dld"
    }
}
```

