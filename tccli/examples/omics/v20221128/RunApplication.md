**Example 1: 单例运行应用**

单例运行应用，生成的任务批次中有一个任务。

Input: 

```
tccli omics RunApplication --cli-unfold-argument  \
    --ApplicationId app-sweet-cerulean-frog-569111 \
    --ProjectId prj-peaceful-pink-bird-631828 \
    --Name test \
    --Description test \
    --EnvironmentId env-05d0g0w2 \
    --InputBase64 e30K \
    --CacheClearDelay 0 \
    --Option.FailureMode NoNewCalls \
    --Option.UseCallCache True \
    --Option.UseErrorOnHold True
```

Output: 
```
{
    "Response": {
        "RequestId": "2f867f15-a2a6-4d42-b6e0-6e06010782ac",
        "RunGroupId": "run-ashamed-turquoise-rooster-131773"
    }
}
```

**Example 2: 批量运行应用**

使用表格功能批量运行应用，生成的任务批次中有多个任务。

Input: 

```
tccli omics RunApplication --cli-unfold-argument  \
    --ApplicationId app-sweet-cerulean-frog-569111 \
    --ProjectId prj-peaceful-pink-bird-631828 \
    --Name test \
    --Description test \
    --EnvironmentId env-05d0g0w2 \
    --InputBase64 e30K \
    --TableId tab-rapid-si̇lver-gerbil-971422 \
    --TableRowUuids df909e9b-1edf-4369-a9d4-71a733770034 3c5f7840-3689-44f2-b6ae-9e223b996f83 \
    --CacheClearDelay 0 \
    --Option.FailureMode NoNewCalls \
    --Option.UseCallCache True \
    --Option.UseErrorOnHold True
```

Output: 
```
{
    "Response": {
        "RequestId": "2f867f15-a2a6-4d42-b6e0-6e06010782ac",
        "RunGroupId": "run-ashamed-turquoise-rooster-131773"
    }
}
```

