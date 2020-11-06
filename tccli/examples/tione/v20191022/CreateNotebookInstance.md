**Example 1: 创建一个Notebook实例**



Input: 

```
tccli tione CreateNotebookInstance --cli-unfold-argument  \
    --NotebookInstanceName test \
    --InstanceType TI.SMALL2.1core2g \
    --DirectInternetAccess Enabled \
    --RootAccess Enabled \
    --SubnetId subnet-xxx \
    --VolumeSizeInGB 10 \
    --LifecycleScriptsName abc
```

Output: 
```
{
    "Response": {
        "RequestId": "fe8f6fd2-1f51-4699-b19d-efa8b6efde8a",
        "NotebookInstanceName": "test"
    }
}
```

