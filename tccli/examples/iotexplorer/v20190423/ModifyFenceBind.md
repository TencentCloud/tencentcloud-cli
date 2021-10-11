**Example 1: ModifyFenceBind**

更新围栏绑定信息

Input: 

```
tccli iotexplorer ModifyFenceBind --cli-unfold-argument  \
    --FenceId 1 \
    --Items.0.ProductId X4912BAIVR \
    --Items.0.Devices.0.DeviceName dev1 \
    --Items.0.Devices.0.AlertCondition InOrOut \
    --Items.0.Devices.0.FenceEnable True \
    --Items.0.Devices.0.Method AppInform
```

Output: 
```
{
    "Response": {
        "RequestId": "1e99faaf-a0f0-4c49-9d85-7f09f2b7f74e"
    }
}
```

