**Example 1: 提交SparkSubmit任务**

本接口用于提交SparkSubmit任务

Input: 

```
tccli dlc CreateSparkSubmitTask --cli-unfold-argument  \
    --TaskName test \
    --TaskType 1 \
    --DataEngineName testEngine \
    --PackagePath cosn://xxx.jar \
    --MainClass Main \
    --RoleArn 0 \
    --IsInherit 1 \
    --DriverSize small \
    --ExecutorSize small \
    --ExecutorNumbers 1 \
    --ExecutorMaxNumbers 1 \
    --CmdArgs.0.Key MAINARGS \
    --CmdArgs.0.Value xejalljhhlJFJLd1gl
```

Output: 
```
{
    "Response": {
        "BatchId": "2ade477a-9f72-44aa-9fd4-65cb739d6301",
        "TaskId": "2ae0ds7a-9f72-44aa-9fd4-65cb739d6301",
        "RequestId": "2ae4707a-9f72-44aa-9fd4-65cb739d6301"
    }
}
```

