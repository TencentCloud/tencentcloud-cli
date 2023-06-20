**Example 1: 启动Spark作业**

启动Spark作业

Input: 

```
tccli dlc CreateSparkAppTask --cli-unfold-argument  \
    --JobName spark-app-test \
    --CmdArgs 10 test 20
```

Output: 
```
{
    "Response": {
        "RequestId": "2ae4707a-9f72-44aa-9fd4-65cb739d6301",
        "BatchId": "batch-9vsx3lh0",
        "TaskId": "4a7cad6bb86211ec9c616e6f30623d72"
    }
}
```

