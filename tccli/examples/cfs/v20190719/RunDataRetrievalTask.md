**Example 1: 启动数据检索任务**

执行数据检索任务。仅Turbo系列文件系统支持。

Input: 

```
tccli cfs RunDataRetrievalTask --cli-unfold-argument  \
    --DataRetrievalId dataretrieval-435de3cc
```

Output: 
```
{
    "Response": {
        "DataRetrievalTaskId": "dataretrievaltask-cc2f42e4",
        "RequestId": "3d6c5cf3-63b1-4e26-94d0-ef48dac81fdc"
    }
}
```

