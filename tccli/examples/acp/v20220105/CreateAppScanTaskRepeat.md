**Example 1: 创建App隐私合规诊断重试任务**

原任务失败后，重新提交隐私合规诊断基础版任务

Input: 

```
tccli acp CreateAppScanTaskRepeat --cli-unfold-argument  \
    --AppPackage com.test.app \
    --Source 2 \
    --OrgTaskID 170143813*******360 \
    --Platform 0 \
    --TaskType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxxx",
        "Result": 0,
        "TaskID": "170143813*******360"
    }
}
```

**Example 2: 重新提交小程序基础版诊断任务**



Input: 

```
tccli acp CreateAppScanTaskRepeat --cli-unfold-argument  \
    --Platform 2 \
    --Source 0 \
    --OrgTaskID 267335492440166400 \
    --AppPackage wxec0b921a4d97c684 \
    --TaskType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "1c2cde1b-8226-4ab9-a6da-52edc66af0af",
        "Result": 0,
        "TaskID": "267340467379638272"
    }
}
```

**Example 3: 重新小程序基础诊断任务**



Input: 

```
tccli acp CreateAppScanTaskRepeat --cli-unfold-argument  \
    --Platform 2 \
    --Source 0 \
    --OrgTaskID 267340467379638272 \
    --AppPackage wxec0b921a4d97c684 \
    --TaskType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "eb9d4e07-11f6-4d04-8e55-d6121c72ad4c",
        "Result": 0,
        "TaskID": "269129073702211584"
    }
}
```

