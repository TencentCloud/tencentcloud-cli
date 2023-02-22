**Example 1: ModifyStorageSetting**

用于修改日志存储天数，或者清空日志；
修改日志存储天数StorageAction需要传入storagetime，StorageDay只能是特定的几个值，详情参考控制台下拉框；
清空日志StorageAction需要传入storagecount，StorageDay不传；

Input: 

```
tccli cfw ModifyStorageSetting --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "f5b034d5-da48-47a6-9d7c-5fb4a3cb7ea1"
    }
}
```

