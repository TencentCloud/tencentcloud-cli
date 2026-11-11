**Example 1: 切换实时编辑场景**



Input: 

```
tccli live SwitchAvatarEditingScene --cli-unfold-argument  \
    --ChannelId vidu_s2_editing_test_2 \
    --EditingType virtual_tryon \
    --ImageUrl https://wsh-test-1303333058.cos.ap-guangzhou.myqcloud.com/change/1%E5%8F%A4%E9%A3%8E.png
```

Output: 
```
{
    "Response": {
        "ChannelId": "vidu_s2_editing_test_2",
        "LiveId": "1008224608114978816",
        "RequestId": "3bee3e96-48ab-46b8-ac6a-238467576596"
    }
}
```

