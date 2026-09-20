**Example 1: 同步 Stable 目标 Version**

从远端拉取到新内容时创建新 Version 并移动 Latest；Stable 保持不变。

Input: 

```
tccli ags SyncRegistryRecord --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "req-example"
    }
}
```

**Example 2: 远端未变化**

远端无变化时不创建 Version、不修改 Label。

Input: 

```
tccli ags SyncRegistryRecord --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "req-example"
    }
}
```

